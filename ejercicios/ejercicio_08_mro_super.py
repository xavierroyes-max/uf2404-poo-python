"""
UF2404 - Ejercicio 8
Código desconocido: MRO, herencia múltiple y super()

OBJETIVOS
1. Predecir el resultado antes de ejecutar.
2. Explicar por qué se obtiene ese resultado.
3. Ejecutar y comprobar.
4. Cambiar únicamente el orden de herencia de D.
5. Explicar qué hace realmente super().

PREDICCIÓN ORIGINAL
-------------------
Para:

    class D(B, C):

El MRO será:

    D -> B -> C -> A -> object

Por tanto:

    D.metodo()
    "D" + B.metodo()
    "D" + "B" + C.metodo()
    "D" + "B" + "C" + A.metodo()

Resultado esperado:

    DBCA

Si cambiamos únicamente el orden a:

    class D(C, B):

el MRO será:

    D -> C -> B -> A -> object

Resultado esperado:

    DCBA
"""


class A:
    def metodo(self):
        return "A"


class B(A):
    def metodo(self):
        return "B" + super().metodo()


class C(A):
    def metodo(self):
        return "C" + super().metodo()


class D(B, C):
    def metodo(self):
        return "D" + super().metodo()


def mostrar_mro(clase):
    """Muestra los nombres de las clases que forman el MRO."""
    return " -> ".join(clase.__name__ for clase in clase.mro())


def prueba_original():
    print("=== ORDEN ORIGINAL: class D(B, C) ===")
    obj = D()
    print("Resultado de obj.metodo():", obj.metodo())
    print("MRO:", mostrar_mro(D))


class DOrdenInvertido(C, B):
    def metodo(self):
        return "D" + super().metodo()


def prueba_orden_invertido():
    print("\n=== ORDEN INVERTIDO: class D(C, B) ===")
    obj = DOrdenInvertido()
    print("Resultado de obj.metodo():", obj.metodo())
    print("MRO:", mostrar_mro(DOrdenInvertido))


def main():
    prueba_original()
    prueba_orden_invertido()


if __name__ == "__main__":
    main()
