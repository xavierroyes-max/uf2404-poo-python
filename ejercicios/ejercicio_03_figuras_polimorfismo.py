"""
UF2404 - Ejercicio 3
Figuras sin modificar la función
"""

from math import pi, sqrt


def imprimir_informe(figuras):
    for figura in figuras:
        print(figura.nombre(), round(figura.area(), 2), round(figura.perimetro(), 2))


class Rectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")
        self.base = base
        self.altura = altura

    def nombre(self):
        return "Rectángulo"

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        self.radio = radio

    def nombre(self):
        return "Círculo"

    def area(self):
        return pi * self.radio ** 2

    def perimetro(self):
        return 2 * pi * self.radio


class TrianguloRectangulo:
    def __init__(self, cateto1, cateto2):
        if cateto1 <= 0 or cateto2 <= 0:
            raise ValueError("Los catetos deben ser mayores que cero.")
        self.cateto1 = cateto1
        self.cateto2 = cateto2

    def nombre(self):
        return "Triángulo rectángulo"

    def area(self):
        return (self.cateto1 * self.cateto2) / 2

    def perimetro(self):
        hipotenusa = sqrt(self.cateto1 ** 2 + self.cateto2 ** 2)
        return self.cateto1 + self.cateto2 + hipotenusa


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def nombre(self):
        return "Cuadrado"


def main():
    figuras = [Rectangulo(4, 3), Circulo(2), TrianguloRectangulo(3, 4), Cuadrado(5)]
    imprimir_informe(figuras)


if __name__ == "__main__":
    main()
