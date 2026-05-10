from excepciones import ErrorCliente

class Cliente:
    """
    Clase que representa un cliente del sistema.
    """

    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

        # Validar datos al crear el cliente
        self.validar()

    def validar(self):
        """
        Valida el correo y teléfono del cliente.
        """

        # Validar correo electrónico
        if "@" not in self.email or "." not in self.email:
            raise ErrorCliente("Email inválido")

        # Validar teléfono
        if not self.telefono.isdigit():
            raise ErrorCliente("El teléfono debe contener solo números")

        if len(self.telefono) < 7:
            raise ErrorCliente("El teléfono es demasiado corto")

    def get_nombre(self):
        """
        Retorna el nombre del cliente.
        """
        return self.nombre

    def mostrar_datos(self):
        """
        Retorna la información completa del cliente.
        """
        return f"[{self.id}] - [{self.nombre}] - [{self.email}] - [{self.telefono}]"