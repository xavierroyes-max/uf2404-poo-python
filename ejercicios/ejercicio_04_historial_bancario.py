"""
UF2404 - Ejercicio 4
Historial bancario
"""


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.titular = titular
        self.__saldo = saldo_inicial
        self.__historial = []
        if saldo_inicial > 0:
            self.__historial.append(f"INGRESO +{saldo_inicial:.2f}")

    def _validar_cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

    def ingresar(self, cantidad):
        self._validar_cantidad(cantidad)
        self.__saldo += cantidad
        self.__historial.append(f"INGRESO +{cantidad:.2f}")

    def retirar(self, cantidad):
        self._validar_cantidad(cantidad)
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= cantidad
        self.__historial.append(f"RETIRADA -{cantidad:.2f}")

    def transferir(self, cuenta_destino, cantidad):
        if not isinstance(cuenta_destino, CuentaBancaria):
            raise TypeError("La cuenta destino debe ser una CuentaBancaria.")
        if cuenta_destino is self:
            raise ValueError("No se puede transferir a la misma cuenta.")
        self._validar_cantidad(cantidad)
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar la transferencia.")
        self.__saldo -= cantidad
        self.__historial.append(f"TRANSFERENCIA -{cantidad:.2f} a {cuenta_destino.titular}")
        cuenta_destino.__saldo += cantidad
        cuenta_destino.__historial.append(f"TRANSFERENCIA +{cantidad:.2f} de {self.titular}")

    def obtener_saldo(self):
        return self.__saldo

    def obtener_historial(self):
        return list(self.__historial)


def main():
    cuenta_ana = CuentaBancaria("Ana", 100)
    cuenta_marc = CuentaBancaria("Marc", 50)
    cuenta_ana.ingresar(40)
    cuenta_ana.retirar(30)
    cuenta_ana.transferir(cuenta_marc, 20)
    print("Saldo de Ana:", cuenta_ana.obtener_saldo())
    print("Saldo de Marc:", cuenta_marc.obtener_saldo())
    print("\nHistorial de Ana:")
    for operacion in cuenta_ana.obtener_historial():
        print("-", operacion)
    print("\nHistorial de Marc:")
    for operacion in cuenta_marc.obtener_historial():
        print("-", operacion)


if __name__ == "__main__":
    main()
