"""
UF2404 - Ejercicio 2
Reserva de plazas

El ejercicio pide crear una clase Evento con:
- reservar(persona)
- cancelar(persona)
- plazas_disponibles()
- len(evento)

Reglas:
- Una persona no puede reservar dos veces.
- No se puede superar la capacidad máxima.
- No se puede cancelar una reserva inexistente.
- La colección interna de inscritos no debe poder modificarse directamente desde fuera.
"""


class Evento:
    def __init__(self, nombre, plazas_maximas):
        if not isinstance(plazas_maximas, int) or isinstance(plazas_maximas, bool):
            raise TypeError("Las plazas máximas deben ser un número entero.")
        if plazas_maximas <= 0:
            raise ValueError("Las plazas máximas deben ser mayores que cero.")
        self.nombre = nombre
        self.plazas_maximas = plazas_maximas
        self.__inscritos = []

    def reservar(self, persona):
        if persona in self.__inscritos:
            raise ValueError(f"{persona} ya tiene una reserva.")
        if self.plazas_disponibles() == 0:
            raise ValueError("No quedan plazas disponibles.")
        self.__inscritos.append(persona)

    def cancelar(self, persona):
        if persona not in self.__inscritos:
            raise ValueError(f"{persona} no tiene ninguna reserva.")
        self.__inscritos.remove(persona)

    def plazas_disponibles(self):
        return self.plazas_maximas - len(self.__inscritos)

    def __len__(self):
        return len(self.__inscritos)


def main():
    evento = Evento("Curso de Python", 2)
    print("Evento:", evento.nombre)
    print("Plazas disponibles al inicio:", evento.plazas_disponibles())
    evento.reservar("Ana")
    evento.reservar("Marc")
    print("Personas inscritas:", len(evento))
    print("Plazas disponibles:", evento.plazas_disponibles())
    try:
        evento.reservar("Ana")
    except ValueError as error:
        print("Error:", error)
    try:
        evento.reservar("Lucía")
    except ValueError as error:
        print("Error:", error)
    evento.cancelar("Ana")
    print("Después de cancelar a Ana:")
    print("Personas inscritas:", len(evento))
    print("Plazas disponibles:", evento.plazas_disponibles())
    evento.reservar("Lucía")
    print("Después de reservar Lucía:")
    print("Personas inscritas:", len(evento))
    print("Plazas disponibles:", evento.plazas_disponibles())
    try:
        evento.cancelar("Pedro")
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
