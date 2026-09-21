"""
UF2404 - Ejercicio 9
Sistema de préstamos de biblioteca
"""


class Libro:
    def __init__(self, isbn, titulo):
        if not isinstance(isbn, str) or not isbn.strip():
            raise ValueError("El ISBN debe ser un texto no vacío.")
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título debe ser un texto no vacío.")
        self.isbn = isbn.strip()
        self.titulo = titulo.strip()
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} | ISBN: {self.isbn} | {estado}"


class Usuario:
    def __init__(self, id_usuario, nombre):
        if not isinstance(id_usuario, str) or not id_usuario.strip():
            raise ValueError("El identificador debe ser un texto no vacío.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        self.id_usuario = id_usuario.strip()
        self.nombre = nombre.strip()

    def __str__(self):
        return f"{self.nombre} ({self.id_usuario})"


class Prestamo:
    def __init__(self, libro, usuario):
        if not isinstance(libro, Libro):
            raise TypeError("El préstamo debe recibir un objeto Libro.")
        if not isinstance(usuario, Usuario):
            raise TypeError("El préstamo debe recibir un objeto Usuario.")
        self.libro = libro
        self.usuario = usuario
        self.activo = True

    def finalizar(self):
        if not self.activo:
            raise ValueError("El préstamo ya estaba finalizado.")
        self.activo = False
        self.libro.disponible = True

    def __str__(self):
        estado = "Activo" if self.activo else "Finalizado"
        return f"{self.libro.titulo} -> {self.usuario.nombre} [{estado}]"


class Biblioteca:
    def __init__(self):
        self.__libros = {}
        self.__usuarios = {}
        self.__prestamos = []

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("Solo se pueden agregar objetos Libro.")
        if libro.isbn in self.__libros:
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}.")
        self.__libros[libro.isbn] = libro

    def registrar_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("Solo se pueden registrar objetos Usuario.")
        if usuario.id_usuario in self.__usuarios:
            raise ValueError(f"Ya existe un usuario con ID {usuario.id_usuario}.")
        self.__usuarios[usuario.id_usuario] = usuario

    def prestar(self, isbn, id_usuario):
        if isbn not in self.__libros:
            raise KeyError(f"No existe ningún libro con ISBN {isbn}.")
        if id_usuario not in self.__usuarios:
            raise KeyError(f"No existe ningún usuario con ID {id_usuario}.")
        libro = self.__libros[isbn]
        usuario = self.__usuarios[id_usuario]
        if not libro.disponible:
            raise ValueError("El libro ya está prestado.")
        if self.__prestamos_activos_usuario(usuario) >= 3:
            raise ValueError("El usuario ya tiene 3 libros prestados.")
        prestamo = Prestamo(libro, usuario)
        libro.disponible = False
        self.__prestamos.append(prestamo)
        return prestamo

    def devolver(self, isbn):
        if isbn not in self.__libros:
            raise KeyError(f"No existe ningún libro con ISBN {isbn}.")
        for prestamo in self.__prestamos:
            if prestamo.libro.isbn == isbn and prestamo.activo:
                prestamo.finalizar()
                return
        raise ValueError("Ese libro no tiene ningún préstamo activo.")

    def prestamos_activos(self):
        return [prestamo for prestamo in self.__prestamos if prestamo.activo]

    def __prestamos_activos_usuario(self, usuario):
        return sum(1 for prestamo in self.__prestamos if prestamo.usuario is usuario and prestamo.activo)


def main():
    biblioteca = Biblioteca()
    libro1 = Libro("978-001", "Python básico")
    libro2 = Libro("978-002", "POO con Python")
    libro3 = Libro("978-003", "Bases de datos")
    libro4 = Libro("978-004", "Algoritmos")
    usuario1 = Usuario("U001", "Ana")
    usuario2 = Usuario("U002", "Marc")
    for libro in (libro1, libro2, libro3, libro4):
        biblioteca.agregar_libro(libro)
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    biblioteca.prestar("978-001", "U001")
    biblioteca.prestar("978-002", "U001")
    biblioteca.prestar("978-003", "U001")
    print("PRÉSTAMOS ACTIVOS DE LA BIBLIOTECA")
    for prestamo in biblioteca.prestamos_activos():
        print("-", prestamo)
    try:
        biblioteca.prestar("978-004", "U001")
    except ValueError as error:
        print("\nError:", error)
    try:
        biblioteca.prestar("978-001", "U002")
    except ValueError as error:
        print("Error:", error)
    biblioteca.devolver("978-001")
    print("\nDESPUÉS DE DEVOLVER 'PYTHON BÁSICO'")
    for prestamo in biblioteca.prestamos_activos():
        print("-", prestamo)
    biblioteca.prestar("978-001", "U002")
    print("\nESTADO FINAL")
    for prestamo in biblioteca.prestamos_activos():
        print("-", prestamo)


if __name__ == "__main__":
    main()
