# Instalación y puesta en marcha

## 1. Requisitos

- Windows 10/11, Linux o macOS.
- Python 3 instalado.
- Navegador web moderno.

No se requieren paquetes externos de Python.

## 2. Comprobar Python en Windows

Abrir PowerShell y ejecutar:

```powershell
python --version
```

Si Windows utiliza el lanzador `py`:

```powershell
py --version
```

## 3. Ubicación recomendada

```text
C:\curso_python\curso_python_interactivo
```

## 4. Arranque automático en Windows

Hacer doble clic en:

```text
iniciar.bat
```

El script inicia el servidor y abre el navegador.

## 5. Arranque manual

```powershell
cd C:\curso_python\curso_python_interactivo
python server.py
```

Después abrir:

```text
http://127.0.0.1:8765
```

## 6. Cerrar el servidor

En la ventana de consola:

```text
Ctrl + C
```

## 7. Ejecutar un ejercicio directamente

Ejemplo:

```powershell
python ejercicios\ejercicio_08_mro_super.py
```

Cada ejercicio es independiente de la interfaz web.

## 8. Puerto ocupado

Si aparece un error indicando que `8765` está ocupado, comprobar si ya hay otra instancia del laboratorio abierta.

En PowerShell puede consultarse:

```powershell
netstat -ano | findstr :8765
```

## 9. Dependencias

`requirements.txt` no contiene librerías externas porque el proyecto usa la biblioteca estándar de Python.
