# funciones
def cargar_ambientes(ruta):
    ambientes = []
    with open(ruta, "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(",")
            linea = [linea[0], linea[1].split(";"), linea[2].split(";"), linea[3].split(";")]
            ambientes += [linea]
    return ambientes


def cargar_arenas(ruta):
    arenas = []
    with open(ruta, "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(",")
            arenas += [linea]
    return arenas


def cargar_objetos(ruta):
    objetos = []
    with open(ruta, "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(",")
            objetos += [linea]
    return objetos


def cargar_tributos(ruta):
    tributos = []
    with open(ruta, "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(",")
            tributos += [linea]
    return tributos
