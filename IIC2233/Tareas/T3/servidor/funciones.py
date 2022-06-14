import json


# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

RUTA_DATOS = jsonObject["ruta_datos"]


def leer_tipo_mensaje(mensaje):
    retorno = ""
    leer = False
    for letra in mensaje:
        if letra == "[":
            leer = True
        if letra == "]":
            leer = False
        if leer:
            retorno += letra
    return retorno[1:]


def leer_participantes():
    lista_retorno = []
    with open(RUTA_DATOS, "r") as archivo:
        for linea in archivo:
            lista_retorno += [linea]
    return lista_retorno


def registrar_info(lista):
    with open("datos.csv", "w") as archivo:
        for dato in lista:
            archivo.write(f"{dato}\n")


def agregar_participante(participante):
    with open(RUTA_DATOS, "a") as archivo:
        archivo.write(f"{participante}\n")


def revisar_repetidos(nombre):
    repetido = False
    existentes = leer_participantes()
    for participante in existentes:
        if nombre == participante[:len(participante) - 1]:
            repetido = True
    return repetido


def revisar_fecha(fecha):
    if "/" not in fecha:
        return False
    else:
        fecha = fecha.split("/")
        if len(fecha) == 3:
            if (len(fecha[0]) == 2 and str(fecha[0]).isdigit()) and (len(fecha[1]) == 2 and str(fecha[1]).isdigit()) and (len(fecha[2]) == 4 and str(fecha[2]).isdigit()):
                if 1 <= int(fecha[1]) <= 12:
                    if 1 <= int(fecha[0]) <= 31:  # Se supone que todos los meses tienen 31 días
                        if int(fecha[2]) <= 2021:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
