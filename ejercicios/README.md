# Ejercicios UF2404

Los diez archivos de este directorio son independientes y pueden ejecutarse directamente con Python.

## Ejercicio 1 — Reparar un diseño defectuoso

**Archivo:** `ejercicio_01_reparar_diseno.py`

Conceptos:

- parámetros mutables;
- `self`;
- atributo de instancia;
- atributo de clase.

Idea clave: cada `Usuario` debe tener su propia lista, mientras `Usuario.total` es compartido.

## Ejercicio 2 — Reserva de plazas

**Archivo:** `ejercicio_02_reserva_plazas.py`

Conceptos:

- encapsulación;
- validación;
- `__len__()`.

Idea clave: las reservas deben pasar por los métodos de `Evento` para respetar aforo y duplicados.

## Ejercicio 3 — Figuras

**Archivo:** `ejercicio_03_figuras_polimorfismo.py`

Conceptos:

- polimorfismo;
- herencia;
- reutilización.

Idea clave: `imprimir_informe()` no cambia aunque reciba distintas figuras.

## Ejercicio 4 — Historial bancario

**Archivo:** `ejercicio_04_historial_bancario.py`

Conceptos:

- encapsulación;
- validación;
- historial;
- interacción entre objetos.

Idea clave: una transferencia actualiza correctamente origen, destino e historial.

## Ejercicio 5 — Refactorización de descuentos

**Archivo:** `ejercicio_05_refactorizacion_descuentos.py`

Conceptos:

- polimorfismo;
- herencia;
- principio abierto/cerrado.

Idea clave: `Pedido` no contiene una cadena de `if/elif` por tipo de cliente.

## Ejercicio 6 — Inventario

**Archivo:** `ejercicio_06_sistema_inventario.py`

Conceptos:

- composición;
- encapsulación;
- diccionario de objetos;
- control de stock.

Idea clave: `Inventario` localiza productos y `Producto` controla su propio stock.

## Ejercicio 7 — Sistema de cursos

**Archivo:** `ejercicio_07_sistema_cursos.py`

Conceptos:

- herencia;
- composición;
- validación de tipos;
- `__str__()`.

Idea clave: `Alumno` y `Profesor` son `Persona`; un `Curso` contiene profesor y alumnos.

## Ejercicio 8 — MRO y `super()`

**Archivo:** `ejercicio_08_mro_super.py`

Conceptos:

- herencia múltiple;
- MRO;
- `super()`.

Resultados principales:

```text
D(B, C) → DBCA
D(C, B) → DCBA
```

Idea clave: `super()` continúa con la siguiente clase del MRO.

## Ejercicio 9 — Biblioteca y préstamos

**Archivo:** `ejercicio_09_sistema_prestamos.py`

Conceptos:

- composición;
- relaciones entre objetos;
- reglas de negocio;
- préstamos activos.

Idea clave: `Prestamo` guarda objetos `Libro` y `Usuario`, no simples identificadores.

## Ejercicio 10 — Sistema extensible de pedidos

**Archivo:** `ejercicio_10_sistema_extensible_pedidos.py`

Conceptos:

- herencia;
- polimorfismo;
- extensibilidad;
- principio abierto/cerrado.

Idea clave: `Pedido.calcular_total()` llama a `producto.precio_final()` y no necesita `if type(...)`.

## Ejecución

Ejemplo desde la raíz del proyecto:

```powershell
python ejercicios\ejercicio_03_figuras_polimorfismo.py
```

## Defensa

Para preguntas, decisiones de diseño y cambios posibles, consultar:

```text
..\EXPLICACION_PROFESOR.md
```
