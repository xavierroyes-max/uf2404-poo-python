"""
UF2404 - Ejercicio 6
Sistema de inventario
"""


class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código debe ser un texto no vacío.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        if not isinstance(precio, (int, float)) or isinstance(precio, bool):
            raise TypeError("El precio debe ser numérico.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if not isinstance(stock, int) or isinstance(stock, bool):
            raise TypeError("El stock debe ser un número entero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.__precio = float(precio)
        self.__stock = stock

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def vender(self, cantidad):
        self.__validar_cantidad(cantidad)
        if cantidad > self.__stock:
            raise ValueError(f"Stock insuficiente de {self.nombre}. Disponible: {self.__stock}.")
        self.__stock -= cantidad

    def reponer(self, cantidad):
        self.__validar_cantidad(cantidad)
        self.__stock += cantidad

    def valor_stock(self):
        return self.__precio * self.__stock

    def __validar_cantidad(self, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

    def __str__(self):
        return f"{self.codigo} - {self.nombre} | Precio: {self.precio:.2f} € | Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos Producto.")
        if producto.codigo in self.__productos:
            raise ValueError(f"Ya existe un producto con el código {producto.codigo}.")
        self.__productos[producto.codigo] = producto

    def eliminar_producto(self, codigo):
        if codigo not in self.__productos:
            raise KeyError(f"No existe ningún producto con el código {codigo}.")
        del self.__productos[codigo]

    def buscar(self, codigo):
        if codigo not in self.__productos:
            raise KeyError(f"No existe ningún producto con el código {codigo}.")
        return self.__productos[codigo]

    def vender(self, codigo, cantidad):
        self.buscar(codigo).vender(cantidad)

    def reponer(self, codigo, cantidad):
        self.buscar(codigo).reponer(cantidad)

    def valor_total(self):
        return sum(producto.valor_stock() for producto in self.__productos.values())


def main():
    inventario = Inventario()
    teclado = Producto("P001", "Teclado", 25.50, 10)
    raton = Producto("P002", "Ratón", 15.00, 5)
    monitor = Producto("P003", "Monitor", 180.00, 3)
    for producto in (teclado, raton, monitor):
        inventario.agregar_producto(producto)
    print("Producto encontrado:")
    print(inventario.buscar("P001"))
    print("\nVendemos 2 teclados...")
    inventario.vender("P001", 2)
    print(inventario.buscar("P001"))
    print("\nReponemos 4 ratones...")
    inventario.reponer("P002", 4)
    print(inventario.buscar("P002"))
    print(f"\nValor total del inventario: {inventario.valor_total():.2f} €")


if __name__ == "__main__":
    main()
