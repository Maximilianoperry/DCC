from random import randint
import parametros as p


def llenar_archivos():
    with open("datos_jugador.csv", "w") as archivo:
        archivo.write(f"0,{p.VIDAS_INICIO},0,1,0, {p.DURACION_RONDA_INICIAL + 1},0,0,0,{p.DURACION_RONDA_INICIAL}")
        # usuario, vidas, monedas, nivel, puntos, tiempo_ronda, tiempos_sobreante, puntos_esta_ronda, puntos_totales, duracion_ronda


def guardar_jugador(nombre):
    with open("datos_jugador.csv", "w") as archivo:
        archivo.write(f"{nombre},{p.VIDAS_INICIO},0,1,0, {p.DURACION_RONDA_INICIAL + 1},0,0,0,{p.DURACION_RONDA_INICIAL}")


def leer_nombre():
    with open("datos_jugador.csv", "r") as archivo:
        nombre = archivo.readlines()
        return nombre


def retorna_vidas():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        vidas = dato[1]
    return vidas


def retorna_monedas():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        monedas = dato[2]
    return monedas


def retorna_nivel():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        nivel = dato[3]
    return nivel


def retorna_puntaje():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        puntaje = dato[4]
    return puntaje


def retorna_tiempo():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        tiempo = dato[5]
    return tiempo


def retorna_tiempo_restante():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        tiempo_res = dato[6]
    return tiempo_res


def retorna_puntaje_ronda_perder():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        vidas = int(retorna_vidas())
        tiempo = int(retorna_tiempo())
        nivel = int(retorna_nivel())
        puntaje = int(((vidas * 100) + (tiempo * 50)) * nivel)
        return puntaje


def sumar_moneda():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        moneda = int(dato[2]) + int(p.CANTIDAD_MONEDAS)
        archivo.write(f"{dato[0]},{dato[1]},{moneda},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")


def sumar_vida():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        vida = int(dato[1]) + 1
        archivo.write(f"{dato[0]},{vida},{dato[2]},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")


def restar_vida():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        vida = int(dato[1]) - 1
        if vida >= 0:
            archivo.write(f"{dato[0]},{vida},{dato[2]},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")
        else:
            archivo.write(f"{dato[0]},0,{dato[2]},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")


def actualizar_tiempo():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        tiempo = int(dato[5]) - 1
        if tiempo >= 0:
            archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{tiempo},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")
        else:
            tiempo = 0
            archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},0,{dato[6]},{dato[7]},{dato[8]},{dato[9]}")
    return tiempo


def mantener_tiempo():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        tiempo = 1000  # el jugador tiene 1000 segundos para elegir si quiere seguir jugando
        archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{tiempo},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")


def sumar_tiempo():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        tiempo_adicional = int(10 * (int(dato[5])/p.DURACION_RONDA_INICIAL))  # Se trabaja en int para que gráficamente se vea mejor
        tiempo = tiempo_adicional + int(dato[5])
        archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{tiempo},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")


def actualizar_nivel():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        nivel = int(dato[3]) + 1
        archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{nivel},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")


def registrar_tiempo_sobra(tiempo):
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{dato[5]},{tiempo},{dato[7]},{dato[8]},{dato[9]}")


def retorna_puntaje_ronda():
    vidas = int(retorna_vidas())
    tiempo_restante = int(retorna_tiempo_restante())
    nivel = int(int(retorna_nivel()) - 1)  # se actualiza el nivel antes de entregar el puntaje, por eso se le resta 1
    puntaje_nivel = ((vidas * 100) + (tiempo_restante * 50)) * nivel
    return puntaje_nivel


def registrar_puntaje_ronda(puntaje):
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{puntaje},{dato[8]},{dato[9]}")


def retorna_duracion_ronda():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        duracion = dato[9]
    return duracion


def actualiza_duracion_ronda():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        dur_ronda = int(float(dato[9]) * p.PONDERACION_DIFICULTAD)
        archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{dur_ronda},{dato[6]},{dato[7]},{dato[8]},{dur_ronda}")


def retorna_usuario():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        usuario = dato[0]
    return usuario


def registrar_puntaje_total(puntaje):
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        puntaje_acumulado = int(dato[8]) + int(puntaje)
        archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{puntaje_acumulado},{dato[9]}")


def retorna_puntaje_total():
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
        puntaje_total = dato[8]
    return puntaje_total


def registrar_puntaje_jugador(nombre, puntaje):
    with open("puntajes.txt", "a") as archivo:
        archivo.write(f"{nombre},{puntaje}\n")


def restar_cantidad_monedas(cantidad):
    with open("datos_jugador.csv", "r") as archivo:
        dato = str(archivo.readlines())
        dato = dato[2:len(dato)-2]
        dato = dato.split(",")
    with open("datos_jugador.csv", "w") as archivo:
        moneda = int(dato[2]) - int(cantidad)
        archivo.write(f"{dato[0]},{dato[1]},{moneda},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]},{dato[9]}")
