"""
UF2404 - Ejercicio 7
Clases que deben funcionar juntas
"""


class Persona:
    def __init__(self, nombre, identificador):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador debe ser un texto no vacío.")
        self.nombre = nombre.strip()
        self.identificador = identificador.strip()

    def __str__(self):
        return f"{self.nombre} ({self.identificador})"


class Alumno(Persona):
    pass


class Profesor(Persona):
    pass


class Curso:
    def __init__(self, nombre, profesor, capacidad_maxima):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del curso debe ser un texto no vacío.")
        if not isinstance(profesor, Profesor):
            raise TypeError("El profesor del curso debe ser un objeto Profesor.")
        if not isinstance(capacidad_maxima, int) or isinstance(capacidad_maxima, bool):
            raise TypeError("La capacidad máxima debe ser un número entero.")
        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que cero.")
        self.nombre = nombre.strip()
        self.__profesor = profesor
        self.__alumnos = []
        self.capacidad_maxima = capacidad_maxima

    def matricular(self, alumno):
        if not isinstance(alumno, Alumno):
            raise TypeError("Solo se pueden matricular objetos Alumno.")
        if alumno in self.__alumnos:
            raise ValueError(f"{alumno.nombre} ya está matriculado.")
        if len(self.__alumnos) >= self.capacidad_maxima:
            raise ValueError("No quedan plazas disponibles en el curso.")
        self.__alumnos.append(alumno)

    def desmatricular(self, alumno):
        if alumno not in self.__alumnos:
            raise ValueError("El alumno no está matriculado en este curso.")
        self.__alumnos.remove(alumno)

    def cambiar_profesor(self, profesor):
        if not isinstance(profesor, Profesor):
            raise TypeError("Solo un objeto Profesor puede impartir el curso.")
        self.__profesor = profesor

    def obtener_profesor(self):
        return self.__profesor

    def obtener_alumnos(self):
        return list(self.__alumnos)

    def __str__(self):
        alumnos_texto = ", ".join(alumno.nombre for alumno in self.__alumnos) or "Sin alumnos"
        return (
            f"Curso: {self.nombre}\n"
            f"Profesor: {self.__profesor.nombre}\n"
            f"Alumnos: {alumnos_texto}\n"
            f"Capacidad: {len(self.__alumnos)}/{self.capacidad_maxima}"
        )


def main():
    profesor1 = Profesor("Laura", "PROF001")
    profesor2 = Profesor("Carlos", "PROF002")
    alumno1 = Alumno("Ana", "ALU001")
    alumno2 = Alumno("Marc", "ALU002")
    alumno3 = Alumno("Lucía", "ALU003")
    curso = Curso("Programación Python", profesor1, 2)
    curso.matricular(alumno1)
    curso.matricular(alumno2)
    print("ESTADO INICIAL DEL CURSO")
    print(curso)
    curso.desmatricular(alumno2)
    curso.matricular(alumno3)
    curso.cambiar_profesor(profesor2)
    print("\nESTADO FINAL DEL CURSO")
    print(curso)


if __name__ == "__main__":
    main()
