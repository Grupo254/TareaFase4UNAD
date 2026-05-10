from abc import ABC, abstractmethod
from excepciones import ErrorServicio

class Servicio(ABC):
    """
    Clase abstracta para los servicios.
    """

    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, horas):
        """
        Método abstracto para calcular costos.
        """
        pass

    def get_nombre(self):
        return self.nombre


# ==================================================
# SERVICIO DE SALA
# ==================================================

class Sala(Servicio):

    def __init__(self):
        super().__init__("S1", "Reserva de Sala", 50000)

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a cero")

        return self.precio * horas


# ==================================================
# SERVICIO DE EQUIPOS
# ==================================================

class Equipos(Servicio):

    def __init__(self):
        super().__init__("S2", "Alquiler de Equipos", 30000)

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a cero")

        descuento = 0.10 if horas > 4 else 0

        return self.precio * horas * (1 - descuento)


# ==================================================
# SERVICIO DE ASESORÍA
# ==================================================

class Asesoria(Servicio):

    def __init__(self):
        super().__init__("S3", "Asesoría Especializada", 80000)

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a cero")

        impuesto = 0.19

        return self.precio * horas * (1 + impuesto)