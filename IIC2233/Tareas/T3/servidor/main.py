from json.decoder import JSONDecodeError
import sys
import json
from servidor import Servidor

# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

HOST = jsonObject["host"]
PORT = jsonObject["port"]
RUTA_DATOS = jsonObject["ruta_datos"]

if __name__ == "__main__":
    servidor = Servidor(HOST, PORT)

    with open(RUTA_DATOS, "w") as archivo:  # se crea archivo que guarda datos
        print("Se ha creado el  archivo de datos")

    try:
        while True:
            input("""[Presione Ctrl+C para cerrar el servidor]

""")
    except KeyboardInterrupt:
        print("Cerrando servidor...")
        servidor.socket_servidor.close()
        sys.exit()
