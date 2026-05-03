from datetime import datetime

class Logger:
    ARCHIVO = "eventos_sistema.log"

    @staticmethod
    def registrar(tipo, mensaje):
        # Obtiene la fecha y hora actual
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Crea la línea de texto que se guardará
        texto = f"[{fecha}] [{tipo}] {mensaje}\n"
        
        # Abre el archivo y agrega la línea (el "a" significa 'append' o añadir)
        with open(Logger.ARCHIVO, "a", encoding="utf-8") as f:
            f.write(texto)
        
        # También lo muestra en la pantalla de VS Code para que lo veas
        print(texto.strip())
        