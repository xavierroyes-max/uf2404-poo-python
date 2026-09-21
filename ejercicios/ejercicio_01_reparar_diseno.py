"""
UF2404 - Ejercicio 1
Reparar un diseño defectuoso

Objetivos:
- Corregir errores de ejecución y de diseño.
- Conseguir que cada Usuario tenga su propia lista de cursos.
- Conseguir que Usuario.total cuente correctamente los usuarios creados.

Puntos que el alumno debe saber explicar:
1. Por qué no usamos cursos=[] como valor por defecto.
2. Por qué usamos self.cursos dentro de los métodos.
3. Por qué total es un atributo de clase.
4. Por qué incrementamos Usuario.total y no una variable llamada total.
"""


class Usuario:
    # Atributo de clase: es compartido por todas las instancias.
    total = 0

    def __init__(self, nombre, cursos=None):
        self.nombre = nombre

        # No usamos cursos=[] como parámetro por defecto.
        # Si no se recibe ninguna lista, creamos una nueva para este usuario.
        if cursos is None:
            self.cursos = []
        else:
            # Hacemos una copia para que la lista interna del usuario
            # no dependa de una lista externa.
            self.cursos = list(cursos)

        # total pertenece a la clase Usuario.
        Usuario.total += 1

    def agregar_curso(self, curso):
        # self.cursos es la lista del usuario concreto.
        self.cursos.append(curso)


def main():
    # Creamos dos usuarios distintos.
    u1 = Usuario("Ana")
    u2 = Usuario("Marc")

    # Solo Ana se matricula en Python.
    u1.agregar_curso("Python")

    print("Cursos de Ana:", u1.cursos)
    print("Cursos de Marc:", u2.cursos)
    print("Total de usuarios:", Usuario.total)


if __name__ == "__main__":
    main()
