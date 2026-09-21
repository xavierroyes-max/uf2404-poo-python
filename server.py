from __future__ import annotations

import json
import mimetypes
import subprocess
import sys
import webbrowser
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from lab_runner import FILES, get_path, run_lab

BASE_DIR = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8765

META = {
    1: {"title":"Reparar un diseño defectuoso","concepts":"atributos de clase, atributos de instancia, parámetros mutables"},
    2: {"title":"Reserva de plazas","concepts":"encapsulación, validación, __len__"},
    3: {"title":"Figuras sin modificar la función","concepts":"polimorfismo, herencia, reutilización"},
    4: {"title":"Historial bancario","concepts":"encapsulación, estado, historial"},
    5: {"title":"Refactorización","concepts":"polimorfismo, Open/Closed"},
    6: {"title":"Sistema de inventario","concepts":"composición, encapsulación, diccionarios"},
    7: {"title":"Clases que funcionan juntas","concepts":"herencia, composición, __str__"},
    8: {"title":"Código desconocido","concepts":"MRO, herencia múltiple, super()"},
    9: {"title":"Sistema de préstamos","concepts":"composición, reglas de negocio"},
    10:{"title":"Sistema extensible de pedidos","concepts":"polimorfismo, extensibilidad, Open/Closed"},
}

FORMS = {
1:[("nombre1","Nombre usuario 1","Ana","text"),("nombre2","Nombre usuario 2","Marc","text"),("curso","Curso","Python","text")],
2:[("evento","Evento","Curso de Python","text"),("plazas","Plazas máximas",2,"number"),("persona1","Persona 1","Ana","text"),("persona2","Persona 2","Marc","text"),("extra","Persona extra","Lucía","text")],
3:[("base","Base rectángulo",4,"number"),("altura","Altura rectángulo",3,"number"),("radio","Radio círculo",2,"number"),("cateto1","Cateto 1",3,"number"),("cateto2","Cateto 2",4,"number"),("lado","Lado cuadrado",5,"number")],
4:[("saldo_ana","Saldo Ana",100,"number"),("saldo_marc","Saldo Marc",50,"number"),("ingreso","Ingreso",40,"number"),("retirada","Retirada",30,"number"),("transferencia","Transferencia",20,"number")],
5:[("precio","Precio unitario",100,"number"),("cantidad","Cantidad",2,"number")],
6:[("precio","Precio producto",25.5,"number"),("stock","Stock inicial",10,"number"),("venta","Cantidad a vender",2,"number"),("reposicion","Cantidad a reponer",4,"number")],
7:[("capacidad","Capacidad máxima",2,"number"),("profesor","Profesor","Laura","text"),("alumno1","Alumno 1","Ana","text"),("alumno2","Alumno 2","Marc","text"),("alumno3","Alumno 3","Lucía","text")],
8:[("orden","Orden de herencia","BC","select",[("BC","D(B, C)"),("CB","D(C, B)")])],
9:[("usuario","Usuario","Ana","text"),("numero_prestamos","Intentos de préstamo",3,"number")],
10:[("fisico","Precio físico",80,"number"),("envio","Envío",5,"number"),("digital","Precio digital",40,"number"),("suscripcion","Precio mensual",10,"number"),("meses","Meses",6,"number"),("descuento_base","Precio con descuento",50,"number"),("descuento","% descuento",20,"number")],
}

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def send_json(self, obj, status=200):
        data=json.dumps(obj,ensure_ascii=False).encode("utf-8")
        self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data)

    def do_GET(self):
        parsed=urlparse(self.path)
        if parsed.path == "/api/exercises":
            data=[]
            for i in range(1,11):
                item={"id":i,**META[i],"file":FILES[i],"form":FORMS[i]}
                data.append(item)
            return self.send_json(data)
        if parsed.path == "/api/code":
            try:
                i=int(parse_qs(parsed.query).get("id",[0])[0]); code=get_path(i).read_text(encoding="utf-8")
                return self.send_json({"id":i,"code":code})
            except Exception as ex:
                return self.send_json({"error":str(ex)},400)
        path = BASE_DIR / ("index.html" if parsed.path in ("/","") else parsed.path.lstrip("/"))
        try:
            path=path.resolve()
            if BASE_DIR not in path.parents and path != BASE_DIR: raise FileNotFoundError
            data=path.read_bytes(); mime=mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            self.send_response(200); self.send_header("Content-Type",mime); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data)
        except Exception:
            self.send_error(404)

    def do_POST(self):
        try:
            length=int(self.headers.get("Content-Length","0")); payload=json.loads(self.rfile.read(length) or b"{}")
            if self.path == "/api/run":
                i=int(payload["id"]); return self.send_json(run_lab(i,payload.get("params",{})))
            if self.path == "/api/save-code":
                i=int(payload["id"]); path=get_path(i); backup=path.with_suffix(path.suffix+".bak")
                if not backup.exists(): backup.write_text(path.read_text(encoding="utf-8"),encoding="utf-8")
                path.write_text(payload.get("code",""),encoding="utf-8")
                return self.send_json({"ok":True,"message":f"Guardado {path.name}. Copia original: {backup.name}"})
            if self.path == "/api/restore-code":
                i=int(payload["id"]); path=get_path(i); backup=path.with_suffix(path.suffix+".bak")
                if not backup.exists(): return self.send_json({"error":"No existe copia .bak"},400)
                path.write_text(backup.read_text(encoding="utf-8"),encoding="utf-8")
                return self.send_json({"ok":True,"message":"Código original restaurado"})
            if self.path == "/api/run-original":
                i=int(payload["id"]); path=get_path(i)
                proc=subprocess.run([sys.executable,"-I",str(path)],capture_output=True,text=True,timeout=5,cwd=str(path.parent))
                return self.send_json({"stdout":proc.stdout,"stderr":proc.stderr,"returncode":proc.returncode})
            self.send_error(404)
        except subprocess.TimeoutExpired:
            self.send_json({"error":"La ejecución superó 5 segundos y se detuvo."},400)
        except Exception as ex:
            self.send_json({"error":f"{type(ex).__name__}: {ex}"},400)


def main():
    url=f"http://{HOST}:{PORT}"
    print(f"Laboratorio UF2404 disponible en {url}")
    print("Para cerrar: Ctrl+C")
    try: webbrowser.open(url)
    except Exception: pass
    ThreadingHTTPServer((HOST,PORT),Handler).serve_forever()

if __name__ == "__main__":
    main()
