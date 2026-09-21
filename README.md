# UF2404 · Programación Orientada a Objetos en Python

Proyecto de evaluación de la **UF2404 · Principios de la programación orientada a objetos**, correspondiente al módulo **MF0227_3 · Programación orientada a objetos**.

El repositorio contiene los **10 ejercicios Python** de la prueba y un **laboratorio web local** diseñado para estudiar, ejecutar, modificar parámetros y explicar paso a paso el comportamiento de cada solución.

## Objetivos

El proyecto está orientado a demostrar no solo que el código funciona, sino que se comprenden y pueden defender los principios aplicados:

- clases, objetos e instancias;
- atributos de clase y de instancia;
- encapsulación;
- herencia;
- composición;
- polimorfismo;
- `super()` y MRO;
- validación y gestión de errores;
- reutilización y reducción de duplicación;
- extensibilidad y principio abierto/cerrado;
- capacidad de predecir, explicar y modificar el código.

## Estructura del repositorio

```text
curso_python_interactivo/
│
├── README.md
├── EXPLICACION_PROFESOR.md
├── README.txt
├── requirements.txt
├── .gitignore
├── .gitattributes
│
├── index.html
├── server.py
├── lab_runner.py
├── iniciar.bat
│
├── assets/
│   ├── README.md
│   ├── styles.css
│   └── app.js
│
├── ejercicios/
│   ├── README.md
│   ├── ejercicio_01_reparar_diseno.py
│   ├── ejercicio_02_reserva_plazas.py
│   ├── ejercicio_03_figuras_polimorfismo.py
│   ├── ejercicio_04_historial_bancario.py
│   ├── ejercicio_05_refactorizacion_descuentos.py
│   ├── ejercicio_06_sistema_inventario.py
│   ├── ejercicio_07_sistema_cursos.py
│   ├── ejercicio_08_mro_super.py
│   ├── ejercicio_09_sistema_prestamos.py
│   └── ejercicio_10_sistema_extensible_pedidos.py
│
└── docs/
    ├── README.md
    ├── INSTALACION.md
    ├── GUIA_USO.md
    ├── ARQUITECTURA.md
    ├── CRITERIOS_EVALUACION.md
    └── GIT_GITHUB.md
```

## Puesta en marcha rápida

En Windows, situar el proyecto por ejemplo en:

```text
C:\curso_python\curso_python_interactivo
```

Después ejecutar:

```text
iniciar.bat
```

O manualmente:

```powershell
cd C:\curso_python\curso_python_interactivo
python server.py
```

El navegador abrirá:

```text
http://127.0.0.1:8765
```

Para detener el servidor, volver a la consola y pulsar `Ctrl + C`.

> El proyecto utiliza únicamente la biblioteca estándar de Python. No necesita Flask, Django ni paquetes externos.

## Laboratorio interactivo

La web permite:

1. seleccionar cualquiera de los 10 ejercicios;
2. modificar valores de entrada;
3. ejecutar escenarios de prueba;
4. observar el resultado;
5. seguir una explicación paso a paso;
6. identificar el concepto POO implicado;
7. consultar el código `.py` original;
8. editarlo desde la interfaz;
9. guardarlo y ejecutarlo;
10. restaurar una copia `.bak` si una modificación no funciona.

La interfaz **no reescribe los ejercicios en JavaScript**. Las clases y cálculos siguen ejecutándose con Python real mediante `server.py` y `lab_runner.py`.

## Resumen de ejercicios

| Nº | Ejercicio | Conceptos principales |
|---:|---|---|
| 1 | Reparar un diseño defectuoso | atributos de clase/instancia, parámetros mutables |
| 2 | Reserva de plazas | encapsulación, validación, `__len__()` |
| 3 | Figuras | polimorfismo, herencia, reutilización |
| 4 | Historial bancario | encapsulación, estado, historial, validación |
| 5 | Refactorización de descuentos | polimorfismo, principio abierto/cerrado |
| 6 | Sistema de inventario | composición, encapsulación, diccionarios |
| 7 | Sistema de cursos | herencia, composición, `__str__()` |
| 8 | Código desconocido | MRO, herencia múltiple, `super()` |
| 9 | Sistema de préstamos | composición, relaciones entre objetos, reglas de negocio |
| 10 | Sistema extensible de pedidos | polimorfismo, extensibilidad, principio abierto/cerrado |

La explicación detallada de cada ejercicio está en [ejercicios/README.md](ejercicios/README.md).

## Defensa ante el profesor

La guía de preparación oral está en:

**[EXPLICACION_PROFESOR.md](EXPLICACION_PROFESOR.md)**

Incluye para cada ejercicio:

- objetivo;
- clases y responsabilidades;
- decisiones de diseño;
- conceptos POO utilizados;
- casos límite;
- preguntas probables;
- pequeñas modificaciones que podrían pedirse en directo;
- predicción del resultado antes de ejecutar.

## Documentación

- [Instalación](docs/INSTALACION.md)
- [Guía de uso](docs/GUIA_USO.md)
- [Arquitectura](docs/ARQUITECTURA.md)
- [Criterios de evaluación](docs/CRITERIOS_EVALUACION.md)
- [Guía Git y GitHub](docs/GIT_GITHUB.md)
- [Índice completo de documentación](docs/README.md)

## Tecnologías

- **Python 3** — lógica de los ejercicios y servidor local.
- **HTML5** — interfaz del laboratorio.
- **CSS3** — presentación visual.
- **JavaScript** — interacción del navegador y llamadas a la API local.
- **Git / GitHub** — control de versiones y entrega del proyecto.

## Diseño del sistema

Flujo general:

```text
Navegador
   │
   ▼
HTML + CSS + JavaScript
   │
   ▼
server.py
   │
   ▼
lab_runner.py
   │
   ▼
ejercicios/*.py
```

El servidor escucha exclusivamente en `127.0.0.1:8765`, por lo que está pensado para uso local.

## Estado

- [x] 10 ejercicios implementados.
- [x] 10 ejercicios comprobados.
- [x] Laboratorio web local.
- [x] Variables modificables desde la interfaz.
- [x] Explicación paso a paso.
- [x] Editor de los `.py`.
- [x] Copia de seguridad `.bak` al editar.
- [x] Documentación técnica.
- [x] Guía de defensa.
- [x] Estructura preparada para Git.
- [ ] Crear el repositorio remoto en GitHub.
- [ ] Realizar `git push` del proyecto final.

## Autor

**Xavier Royes**

Proyecto académico de la UF2404.
