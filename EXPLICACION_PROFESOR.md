# UF2404 · Guía de defensa ante el profesor

**Alumno:** Xavier Royes  
**Proyecto:** 10 ejercicios de Programación Orientada a Objetos en Python + laboratorio web interactivo

## Presentación general

> He resuelto los diez ejercicios en archivos Python independientes. Además, he creado un laboratorio web local que importa esos ejercicios y permite cambiar parámetros, ejecutar escenarios y visualizar paso a paso por qué se produce cada resultado. La web no sustituye el código Python: sirve para probarlo, comprenderlo y preparar modificaciones durante la defensa.

La aplicación está dividida en:

- los archivos `.py` de los ejercicios;
- `lab_runner.py`, que crea escenarios interactivos utilizando las clases reales;
- `server.py`, que comunica Python con el navegador;
- `index.html`, `styles.css` y `app.js`, que forman la interfaz.

---

## Ejercicio 1 · Reparar un diseño defectuoso

### Idea principal
Cada `Usuario` debe tener su propia lista de cursos, mientras `Usuario.total` debe compartirse entre todas las instancias.

### Conceptos
- atributo de instancia;
- atributo de clase;
- parámetro mutable;
- `self`.

### Pregunta probable
**¿Cuál es la diferencia entre `self.cursos` y `Usuario.total`?**

> `self.cursos` pertenece a cada instancia concreta. `Usuario.total` pertenece a la clase y se comparte entre todos los usuarios.

### Cambio posible
Añadir un método que devuelva el número de cursos de un usuario.

---

## Ejercicio 2 · Reserva de plazas

### Idea principal
`Evento` protege su lista de inscritos y obliga a que las modificaciones pasen por `reservar()` y `cancelar()`.

### Conceptos
- encapsulación;
- validación;
- `__len__()`.

### Pregunta probable
**¿Por qué no dejas pública la lista de inscritos?**

> Porque desde fuera podrían añadirse personas sin comprobar duplicados ni capacidad. La encapsulación obliga a pasar por los métodos que mantienen las reglas del objeto.

### Cambio posible
Añadir `esta_inscrito(persona)`.

---

## Ejercicio 3 · Figuras

### Idea principal
Todas las figuras ofrecen:

```python
nombre()
area()
perimetro()
```

La función que imprime el informe no necesita conocer la clase concreta.

### Conceptos
- polimorfismo;
- herencia;
- reutilización.

### Pregunta probable
**¿Dónde está el polimorfismo?**

> En que la misma llamada `figura.area()` o `figura.perimetro()` funciona sobre objetos de clases diferentes y ejecuta la implementación correspondiente.

`Cuadrado` hereda de `Rectangulo` para reutilizar área y perímetro.

---

## Ejercicio 4 · Historial bancario

### Idea principal
`CuentaBancaria` controla saldo e historial. Una transferencia modifica dos objetos y registra la operación en ambos.

### Conceptos
- encapsulación;
- validación;
- estado;
- interacción entre objetos.

### Pregunta probable
**¿Por qué `obtener_historial()` devuelve una copia?**

> Para que el código externo no pueda modificar el historial interno real.

---

## Ejercicio 5 · Refactorización

### Idea principal
Cada tipo de cliente calcula su propio precio. `Pedido` ya no necesita una cadena de `if/elif`.

### Conceptos
- herencia;
- polimorfismo;
- principio abierto/cerrado.

### Pregunta probable
**¿Cómo añadirías un nuevo descuento?**

> Crearía una nueva subclase de `Cliente` que implemente `calcular_precio()`. `Pedido` no tendría que modificarse.

---

## Ejercicio 6 · Inventario

### Idea principal
`Producto` controla su propio stock. `Inventario` organiza, busca y coordina productos.

### Conceptos
- composición;
- encapsulación;
- diccionarios;
- separación de responsabilidades.

### Pregunta probable
**¿Por qué un diccionario en lugar de una lista?**

> Porque la búsqueda se realiza por código y un diccionario relaciona directamente código con objeto Producto.

---

## Ejercicio 7 · Sistema de cursos

### Herencia

```text
Persona
├── Alumno
└── Profesor
```

`Alumno` y `Profesor` **son** personas.

### Composición

Un `Curso` **tiene**:

- un profesor;
- varios alumnos.

### Pregunta probable
**¿Diferencia entre herencia y composición en este ejercicio?**

> Alumno es una Persona: herencia. Curso tiene un Profesor y Alumnos: composición.

---

## Ejercicio 8 · MRO y super()

### Caso original

```python
class D(B, C):
```

MRO:

```text
D → B → C → A → object
```

Resultado:

```text
DBCA
```

### Orden invertido

```python
class D(C, B):
```

Resultado:

```text
DCBA
```

### Idea clave

> En herencia múltiple, `super()` continúa con la siguiente clase del MRO. No significa simplemente «llamar al padre escrito en la definición de la clase».

---

## Ejercicio 9 · Sistema de préstamos

### Clases

```text
Libro
Usuario
Prestamo
Biblioteca
```

### Idea principal

`Prestamo` relaciona directamente objetos:

```python
self.libro = libro
self.usuario = usuario
```

### Reglas
- ISBN único;
- usuario con identificador único;
- un libro prestado no puede prestarse de nuevo;
- máximo 3 préstamos simultáneos;
- devolver un libro finaliza su préstamo activo.

### Pregunta probable
**¿Por qué no guardas solo ISBN e ID dentro del préstamo?**

> Porque el ejercicio pide relaciones entre objetos y porque el préstamo puede acceder directamente a los datos y comportamiento del libro y del usuario relacionados.

---

## Ejercicio 10 · Sistema extensible de pedidos

### Jerarquía

```text
Producto
├── ProductoFisico
├── ProductoDigital
├── Suscripcion
└── ProductoDescuento
```

### Idea principal
Todos implementan:

```python
precio_final()
```

`Pedido.calcular_total()` no utiliza `if type(...)`; simplemente llama:

```python
producto.precio_final()
```

Esto permite añadir nuevos productos sin modificar la lógica principal.

---

# Cómo explicar la web interactiva

La web es una herramienta auxiliar de estudio y demostración.

```text
Navegador
   ↓
HTML + CSS + JavaScript
   ↓
server.py
   ↓
lab_runner.py
   ↓
ejercicios/*.py
```

El navegador no sustituye las clases Python. JavaScript solo gestiona la interfaz; las clases y cálculos siguen ejecutándose con Python real.

El servidor escucha exclusivamente en:

```text
127.0.0.1:8765
```

La ejecución directa de un ejercicio tiene un límite de 5 segundos.

---

# Preguntas generales

## ¿Qué es self?
Es la referencia a la instancia concreta sobre la que se está ejecutando el método.

## ¿Qué es encapsulación?
Controlar el acceso y modificación del estado interno de un objeto mediante sus métodos.

## ¿Qué es herencia?
Crear una clase especializada reutilizando una clase más general.

## ¿Qué es composición?
Construir un objeto utilizando otros objetos como partes de su estado o funcionamiento.

## ¿Qué es polimorfismo?
Permitir que objetos de clases diferentes respondan a la misma operación con su implementación propia.

## ¿Por qué validar antes de modificar?
Para que una operación no válida no deje el objeto en un estado incoherente.

---

# Estrategia ante una modificación en directo

1. Repetir con palabras qué pide el profesor.
2. Identificar qué clase tiene esa responsabilidad.
3. Localizar el método que debe modificarse o extenderse.
4. Predecir qué ocurrirá.
5. Modificar solo lo necesario.
6. Ejecutar.
7. Comparar el resultado con la predicción.
8. Explicar cualquier diferencia.

---

# Resumen rápido

| Ejercicio | Idea esencial |
|---:|---|
| 1 | `self.cursos` es individual; `Usuario.total` es compartido |
| 2 | encapsulación de inscritos y `__len__()` |
| 3 | polimorfismo de figuras |
| 4 | saldo e historial protegidos; transferencia entre dos objetos |
| 5 | descuentos mediante polimorfismo |
| 6 | Inventario tiene Productos |
| 7 | Alumno/Profesor son Persona; Curso tiene ambos |
| 8 | `super()` sigue el MRO |
| 9 | Prestamo relaciona objetos Libro y Usuario |
| 10 | cada Producto calcula `precio_final()`; Pedido permanece extensible |

## Cierre sugerido

> El criterio que he intentado mantener en todos los ejercicios es que cada objeto sea responsable de su propio estado y de las operaciones que le corresponden. Cuando varios tipos comparten una operación he usado polimorfismo para evitar condicionales por tipo, y cuando un objeto contiene a otros he utilizado composición. La web me permite demostrar estos comportamientos cambiando valores y ejecutando casos límite sin sustituir el código Python original.
