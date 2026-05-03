# 1. Importamos todas las herramientas necesarias
from excepciones import ErrorCliente, ErrorPrecioNegativo, ErrorFechaInvalida
from logger import Logger

def sistema_principal():
    print("--- SISTEMA INTEGRADO UNAD (FASE 4) ---")
    
    try:
        # VALIDACIÓN 1: Nombre
        nombre = input("Ingrese el nombre del cliente/servicio: ")
        if len(nombre) < 3:
            raise ErrorCliente("El nombre es muy corto o está vacío.")
        
        # VALIDACIÓN 2: Precio
        precio_input = input("Ingrese el precio: ")
        precio = float(precio_input) # Convertimos a número
        if precio < 0:
            raise ErrorPrecioNegativo(f"Precio negativo detectado: ${precio}")

        # VALIDACIÓN 3: Fecha
        fecha = input("Ingrese fecha (DD/MM/AAAA): ")
        if "/" not in fecha or len(fecha) != 10:
            raise ErrorFechaInvalida(f"Formato de fecha incorrecto: {fecha}")

        # SI TODO SALE BIEN: Registro de éxito
        mensaje = f"ÉXITO: {nombre} | Precio: ${precio} | Fecha: {fecha}"
        Logger.registrar("INFO", mensaje)
        print("\n¡Todo se registró correctamente en el sistema!")

    # Aquí atrapamos cada error por separado para que el Logger sepa qué pasó
    except ErrorCliente as e:
        Logger.registrar("ERROR", f"Nombre inválido: {e}")
        print(f"Error de validación: {e}")

    except ErrorPrecioNegativo as e:
        Logger.registrar("ERROR", f"Precio inválido: {e}")
        print(f"Error de finanzas: {e}")

    except ErrorFechaInvalida as e:
        Logger.registrar("ERROR", f"Fecha inválida: {e}")
        print(f"Error de calendario: {e}")

    except ValueError:
        # Este salta si el usuario escribe letras donde van números
        Logger.registrar("CRITICAL", "El usuario ingresó letras en el campo de precio.")
        print("Error: En el precio solo se permiten números.")

# 2. Ejecución del programa
if __name__ == "__main__":
    sistema_principal()
    
    
    