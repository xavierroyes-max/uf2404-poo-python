# Arquitectura del proyecto

## Visión general

```text
┌─────────────────────────────┐
│ Navegador                   │
│ index.html + app.js + CSS   │
└──────────────┬──────────────┘
               │ HTTP / JSON
               ▼
┌─────────────────────────────┐
│ server.py                   │
│ 127.0.0.1:8765              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ lab_runner.py               │
│ carga módulos y escenarios  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ ejercicios/*.py             │
│ clases evaluadas            │
└─────────────────────────────┘
```

## `index.html`

Define la estructura visual principal del laboratorio.

No contiene la implementación POO de los ejercicios.

## `assets/app.js`

Se encarga de:

- consultar la lista de ejercicios;
- generar formularios;
- enviar parámetros a Python;
- mostrar resultados;
- cargar código;
- guardar código;
- restaurar copias;
- solicitar la ejecución directa de un ejercicio.

## `assets/styles.css`

Contiene exclusivamente la presentación visual.

## `server.py`

Usa `ThreadingHTTPServer` de la biblioteca estándar.

Funciones principales:

- servir archivos estáticos;
- `/api/exercises`: metadatos y formularios;
- `/api/code`: cargar el código;
- `/api/run`: ejecutar un escenario interactivo;
- `/api/save-code`: guardar una modificación;
- `/api/restore-code`: restaurar la copia `.bak`;
- `/api/run-original`: ejecutar el `.py` real.

La ejecución directa se realiza con:

```python
subprocess.run(..., timeout=5)
```

## `lab_runner.py`

Importa dinámicamente el ejercicio solicitado mediante `importlib`.

Los escenarios interactivos reutilizan las clases reales de cada archivo. No existe una segunda implementación de las soluciones en JavaScript.

## Directorio `ejercicios/`

Contiene las soluciones evaluables.

La web es una herramienta auxiliar; cada `.py` puede ejecutarse por separado.

## Encapsulación de responsabilidades

La arquitectura también aplica separación de responsabilidades:

- HTML: estructura;
- CSS: presentación;
- JavaScript: interacción;
- servidor Python: transporte y operaciones de archivo;
- `lab_runner.py`: adaptación para el laboratorio;
- ejercicios: lógica POO objeto de la evaluación.
