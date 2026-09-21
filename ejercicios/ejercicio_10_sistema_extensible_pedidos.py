"""
UF2404 - Ejercicio 10
Sistema extensible de pedidos
"""


class Producto:
    def __init__(self, id_producto, nombre, precio_base):
        if not isinstance(id_producto, str) or not id_producto.strip():
            raise ValueError("El id del producto debe ser un texto no vacío.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool):
            raise TypeError("El precio base debe ser numérico.")
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")
        self.id = id_producto.strip()
        self.nombre = nombre.strip()
        self.precio_base = float(precio_base)

    def precio_final(self):
        raise NotImplementedError("Cada tipo de producto debe implementar precio_final().")


class ProductoFisico(Producto):
    def __init__(self, id_producto, nombre, precio_base, coste_envio):
        super().__init__(id_producto, nombre, precio_base)
        if not isinstance(coste_envio, (int, float)) or isinstance(coste_envio, bool):
            raise TypeError("El coste de envío debe ser numérico.")
        if coste_envio < 0:
            raise ValueError("El coste de envío no puede ser negativo.")
        self.coste_envio = float(coste_envio)

    def precio_final(self):
        return self.precio_base + self.coste_envio


class ProductoDigital(Producto):
    def precio_final(self):
        return self.precio_base


class Suscripcion(Producto):
    def __init__(self, id_producto, nombre, precio_base, meses):
        super().__init__(id_producto, nombre, precio_base)
        if not isinstance(meses, int) or isinstance(meses, bool):
            raise TypeError("Los meses deben ser un número entero.")
        if meses <= 0:
            raise ValueError("Los meses deben ser mayores que cero.")
        self.meses = meses

    def precio_final(self):
        return self.precio_base * self.meses


class ProductoDescuento(Producto):
    def __init__(self, id_producto, nombre, precio_base, porcentaje_descuento):
        super().__init__(id_producto, nombre, precio_base)
        if not isinstance(porcentaje_descuento, (int, float)) or isinstance(porcentaje_descuento, bool):
            raise TypeError("El porcentaje de descuento debe ser numérico.")
        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self.porcentaje_descuento = float(porcentaje_descuento)

    def precio_final(self):
        return self.precio_base * (1 - self.porcentaje_descuento / 100)


class Pedido:
    def __init__(self):
        self.__productos = {}

    def agregar(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos Producto.")
        if producto.id in self.__productos:
            raise ValueError(f"Ya existe un producto con el id {producto.id}.")
        self.__productos[producto.id] = producto

    def eliminar(self, id_producto):
        if id_producto not in self.__productos:
            raise KeyError(f"No existe ningún producto con el id {id_producto}.")
        del self.__productos[id_producto]

    def calcular_total(self):
        return sum(producto.precio_final() for producto in self.__productos.values())

    def obtener_productos(self):
        return list(self.__productos.values())


def main():
    pedido = Pedido()
    productos = [
        ProductoFisico("P001", "Teclado mecánico", 80, 5),
        ProductoDigital("P002", "Curso de Python", 40),
        Suscripcion("P003", "Servicio Premium", 10, 6),
        ProductoDescuento("P004", "Libro de programación", 50, 20),
    ]
    for producto in productos:
        pedido.agregar(producto)
        print(f"{producto.nombre}: {producto.precio_final():.2f} €")
    print(f"TOTAL: {pedido.calcular_total():.2f} €")


if __name__ == "__main__":
    main()
