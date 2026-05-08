from excepciones import ErrorReserva
from cliente import Cliente
from servicio import Servicio

class Reserva:
    """
    Clase encargada de gestionar las reservas.
    """
    def _init_(self, id, cliente, servicio, horas):
        # Validar cliente
        if not isinstance(cliente, Cliente):
            raise ErrorReserva("Cliente inválido")

        # Validar servicio
        if not isinstance(servicio, Servicio):
            raise ErrorReserva("Servicio inválido")

        # Validar horas
        if horas <= 0:
            raise ErrorReserva("Las horas deben ser mayores a cero")

        self.id = id
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas

        # Estado inicial
        self.estado = "pendiente"

        # Calcular costo total
        self.costo = servicio.calcular_costo(horas) # Asumiendo que servicio tiene un método 'calcular_costo'

    def confirmar(self):
        """
        Confirma una reserva.
        """
        if self.estado == "cancelada":
            raise ErrorReserva("No se puede confirmar una reserva cancelada")
        self.estado = "confirmada"

    def cancelar(self):
        """
        Cancela una reserva.
        """
        if self.estado == "confirmada":
            raise ErrorReserva("No se puede cancelar una reserva confirmada")
        self.estado = "cancelada"

    def mostrar_reserva(self):
        """
        Muestra la información de la reserva.
        """
        return (
            f"Reserva: [{self.id}] | "
            f"Cliente: [{self.cliente.get_nombre()}] | "
            f"Servicio: [{self.servicio.get_nombre()}] | "
            f"Horas: [{self.horas}] | "
            f"Costo: ${self.costo} | "
            f"Estado: [{self.estado}]"
        )
