from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EXERCISES_DIR = BASE_DIR / "ejercicios"

FILES = {
    1: "ejercicio_01_reparar_diseno.py",
    2: "ejercicio_02_reserva_plazas.py",
    3: "ejercicio_03_figuras_polimorfismo.py",
    4: "ejercicio_04_historial_bancario.py",
    5: "ejercicio_05_refactorizacion_descuentos.py",
    6: "ejercicio_06_sistema_inventario.py",
    7: "ejercicio_07_sistema_cursos.py",
    8: "ejercicio_08_mro_super.py",
    9: "ejercicio_09_sistema_prestamos.py",
    10: "ejercicio_10_sistema_extensible_pedidos.py",
}

def get_path(exercise_id: int) -> Path:
    if exercise_id not in FILES:
        raise ValueError("Ejercicio no válido")
    return EXERCISES_DIR / FILES[exercise_id]

def load_module(exercise_id: int):
    path = get_path(exercise_id)
    module_name = f"curso_python_ejercicio_{exercise_id}_{path.stat().st_mtime_ns}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("No se pudo cargar el ejercicio")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def val(params, name, default, cast=str):
    raw = params.get(name, default)
    if raw == "" or raw is None:
        raw = default
    return cast(raw)

def run_lab(exercise_id: int, params: dict) -> dict:
    module = load_module(exercise_id)
    return globals()[f"run_{exercise_id}"](module, params)

def result(output, steps, notes=None):
    return {"output": output, "steps": steps, "notes": notes or []}

def run_1(m, p):
    m.Usuario.total = 0
    n1,n2,curso=val(p,"nombre1","Ana"),val(p,"nombre2","Marc"),val(p,"curso","Python")
    u1,u2=m.Usuario(n1),m.Usuario(n2);u1.agregar_curso(curso)
    return result(f"Cursos de {n1}: {u1.cursos}\nCursos de {n2}: {u2.cursos}\nTotal de usuarios: {m.Usuario.total}",[
        {"title":"Crear usuarios","why":"Cada instancia crea su propia lista.","state":f"{n1}.cursos={u1.cursos}; {n2}.cursos={u2.cursos}"},
        {"title":"Agregar curso","why":"self.cursos modifica solo la instancia indicada.","state":f"{n1}.cursos={u1.cursos}"},
        {"title":"Contador de clase","why":"Usuario.total es compartido.","state":f"Usuario.total={m.Usuario.total}"}])

def run_2(m,p):
    e=m.Evento(val(p,"evento","Curso de Python"),val(p,"plazas",2,int));logs=[];steps=[]
    for person in [val(p,"persona1","Ana"),val(p,"persona2","Marc"),val(p,"extra","Lucía")]:
        try:
            e.reservar(person);logs.append(f"Reserva OK: {person}");steps.append({"title":f"Reservar {person}","why":"Se validan duplicado y aforo.","state":f"inscritos={len(e)}, libres={e.plazas_disponibles()}"})
        except Exception as ex:
            logs.append(f"Error: {ex}")
    return result("\n".join(logs)+f"\nInscritos: {len(e)}\nPlazas libres: {e.plazas_disponibles()}",steps)

def run_3(m,p):
    figs=[m.Rectangulo(val(p,"base",4,float),val(p,"altura",3,float)),m.Circulo(val(p,"radio",2,float)),m.TrianguloRectangulo(val(p,"cateto1",3,float),val(p,"cateto2",4,float)),m.Cuadrado(val(p,"lado",5,float))]
    lines=[];steps=[]
    for f in figs:
        lines.append(f"{f.nombre()}: área={f.area():.2f}, perímetro={f.perimetro():.2f}")
        steps.append({"title":f.nombre(),"why":"Misma interfaz, distinta implementación.","state":f"área={f.area():.2f}; perímetro={f.perimetro():.2f}"})
    return result("\n".join(lines),steps,["Cuadrado hereda de Rectangulo."])

def run_4(m,p):
    a,b=m.CuentaBancaria("Ana",val(p,"saldo_ana",100,float)),m.CuentaBancaria("Marc",val(p,"saldo_marc",50,float));steps=[];logs=[]
    for title,action in [("Ingreso",lambda:a.ingresar(val(p,"ingreso",40,float))),("Retirada",lambda:a.retirar(val(p,"retirada",30,float))),("Transferencia",lambda:a.transferir(b,val(p,"transferencia",20,float)))]:
        try: action();logs.append(f"{title}: OK");steps.append({"title":title,"why":"La clase valida antes de modificar.","state":f"Ana={a.obtener_saldo():.2f}; Marc={b.obtener_saldo():.2f}"})
        except Exception as ex: logs.append(f"{title}: ERROR - {ex}")
    return result("\n".join(logs),steps)

def run_5(m,p):
    precio,cantidad=val(p,"precio",100,float),val(p,"cantidad",2,int);lines=[];steps=[]
    for c in [m.ClienteNormal(),m.ClienteVIP(),m.Empleado(),m.ClientePremium(),m.ClienteEstudiante()]:
        total=m.Pedido(c).calcular_precio(precio,cantidad);name=c.__class__.__name__;lines.append(f"{name}: {total:.2f} €");steps.append({"title":name,"why":"Pedido delega el cálculo al cliente.","state":f"total={total:.2f} €"})
    return result("\n".join(lines),steps)

def run_6(m,p):
    inv=m.Inventario();prod=m.Producto("P001","Teclado",val(p,"precio",25.5,float),val(p,"stock",10,int));inv.agregar_producto(prod);lines=[f"Inicial: {prod}"];steps=[]
    try: inv.vender("P001",val(p,"venta",2,int));lines.append(f"Después de vender: {prod}");steps.append({"title":"Venta","why":"Producto controla su stock.","state":f"stock={prod.stock}"})
    except Exception as ex: lines.append(f"ERROR: {ex}")
    try: inv.reponer("P001",val(p,"reposicion",4,int));lines.append(f"Después de reponer: {prod}")
    except Exception as ex: lines.append(f"ERROR: {ex}")
    lines.append(f"Valor total: {inv.valor_total():.2f} €");return result("\n".join(lines),steps)

def run_7(m,p):
    cap=val(p,"capacidad",2,int);prof=m.Profesor(val(p,"profesor","Laura"),"PROF001");curso=m.Curso("Programación Python",prof,cap);steps=[];lines=[]
    for i,name in enumerate([val(p,"alumno1","Ana"),val(p,"alumno2","Marc"),val(p,"alumno3","Lucía")],1):
        a=m.Alumno(name,f"A{i}")
        try: curso.matricular(a);lines.append(f"Matriculado: {name}");steps.append({"title":f"Matricular {name}","why":"Valida tipo, duplicado y capacidad.","state":f"{len(curso.obtener_alumnos())}/{cap}"})
        except Exception as ex: lines.append(f"No matriculado {name}: {ex}")
    lines+=["",str(curso)];return result("\n".join(lines),steps)

def run_8(m,p):
    orden=val(p,"orden","BC");cls=m.D if orden=="BC" else m.DOrdenInvertido;obj=cls();value=obj.metodo();mro=" -> ".join(c.__name__ for c in cls.mro())
    return result(f"Orden elegido: {orden}\nResultado: {value}\nMRO: {mro}",[
        {"title":"Resolver MRO","why":"Python construye el orden de búsqueda.","state":mro},
        {"title":"Seguir super()","why":"super() avanza a la siguiente clase del MRO.","state":value}])

def run_9(m,p):
    usuario=val(p,"usuario","Ana");intentos=max(1,min(4,val(p,"numero_prestamos",3,int)));b=m.Biblioteca();u=m.Usuario("U001",usuario);b.registrar_usuario(u);steps=[];lines=[]
    libros=[m.Libro(f"978-00{i}",t) for i,t in enumerate(["Python básico","POO con Python","Bases de datos","Algoritmos"],1)]
    for l in libros:b.agregar_libro(l)
    for l in libros[:intentos]:
        try: pr=b.prestar(l.isbn,"U001");lines.append(str(pr));steps.append({"title":f"Prestar {l.titulo}","why":"Prestamo relaciona Libro y Usuario.","state":f"activos={len(b.prestamos_activos())}"})
        except Exception as ex: lines.append(f"ERROR: {ex}")
    return result("\n".join(lines),steps)

def run_10(m,p):
    productos=[m.ProductoFisico("P001","Teclado",val(p,"fisico",80,float),val(p,"envio",5,float)),m.ProductoDigital("P002","Curso",val(p,"digital",40,float)),m.Suscripcion("P003","Premium",val(p,"suscripcion",10,float),val(p,"meses",6,int)),m.ProductoDescuento("P004","Libro",val(p,"descuento_base",50,float),val(p,"descuento",20,float))]
    pedido=m.Pedido();steps=[]
    for prod in productos: pedido.agregar(prod);steps.append({"title":f"Agregar {prod.nombre}","why":"Pedido acepta cualquier subclase compatible.","state":f"precio_final={prod.precio_final():.2f} €"})
    total=pedido.calcular_total();lines=[f"{x.nombre}: {x.precio_final():.2f} €" for x in productos]+[f"TOTAL: {total:.2f} €"];return result("\n".join(lines),steps)
