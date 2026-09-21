"""
UF2404 - Ejercicio 5
Refactorización de descuentos con POO
"""


class Cliente:
    def calcular_precio(self, precio, cantidad):
        raise NotImplementedError("Las subclases deben implementar calcular_precio().")


class ClienteNormal(Cliente):
    def calcular_precio(self, precio, cantidad):
        return precio * cantidad


class ClienteVIP(Cliente):
    def calcular_precio(self, precio, cantidad):
        return precio * cantidad * 0.80


class Empleado(Cliente):
    def calcular_precio(self, precio, cantidad):
        return precio * cantidad * 0.50


class ClientePremium(Cliente):
    def calcular_precio(self, precio, cantidad):
        return precio * cantidad * 0.70


class ClienteEstudiante(Cliente):
    def calcular_precio(self, precio, cantidad):
        return precio * cantidad * 0.85


class Pedido:
    def __init__(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("El cliente debe ser un objeto de tipo Cliente.")
        self.cliente = cliente

    def calcular_precio(self, precio, cantidad):
        if not isinstance(precio, (int, float)) or isinstance(precio, bool):
            raise TypeError("El precio debe ser numérico.")
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número entero.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        return self.cliente.calcular_precio(precio, cantidad)


def main():
    precio = 100
    cantidad = 2
    clientes = [ClienteNormal(), ClienteVIP(), Empleado(), ClientePremium(), ClienteEstudiante()]
    for cliente in clientes:
        pedido = Pedido(cliente)
        total = pedido.calcular_precio(precio, cantidad)
        print(f"{cliente.__class__.__name__}: {total:.2f} €")


if __name__ == "__main__":
    main()
