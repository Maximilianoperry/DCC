import parametros as p
import cargar_datos as c


def actualizar_vivos():
    respaldo_datos = c.cargar_tributos(p.RUTA_TRIBUTOS)
    with open(p.RUTA_TRIBUTOS, 'w') as archivo:
        for linea in respaldo_datos:
            if linea[3].isdigit() is True:
                if int(linea[3]) > 0:
                    string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                    archivo.write(string)
            else:
                if linea[3][0] != "-":
                    string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                    archivo.write(string)


def mostrar_vivos_muertos():
    actualizar_vivos()
    vivos = c.cargar_tributos(p.RUTA_TRIBUTOS)
    nombre_vivos = []
    data_muertos_no_filtrada = c.cargar_tributos("respaldo_datos/tributos.csv")
    nombres_muertos = []
    muertos = []
    for dato in data_muertos_no_filtrada[1:]:
        nombres_muertos += [dato[0]]
    for vivo in vivos[1:]:
        nombre_vivos += [vivo[0]]
    for nombre in nombres_muertos:
        agregar = True
        for vivo in nombre_vivos:
            if nombre == vivo:
                agregar = False
        if agregar is True:
            muertos += [nombre]

    print("VIVOS:")
    for vivo in nombre_vivos:
        print(f"   - {vivo}")
    print(" ")
    print("MUERTOS:")
    for muerto in muertos:
        print(f"   - {muerto}")


def mostrar_opciones():
    datos = c.cargar_tributos(p.RUTA_TRIBUTOS)
    numero = 1
    for dato in datos:
        if dato[0] != "nombre":
            print(f"""[{numero}]
Nombre: {dato[0]}
Distrito:{dato[1]}
Edad: {dato[2]}
Vida: {dato[3]}
Energía: {dato[4]}
Agilidad: {dato[5]}
Fuerza: {dato[6]}
Ingenio: {dato[7]}
Popularidad: {dato[8]}
""")
            numero += 1
    opcion = input("Seleccione un tributo: ")
    if opcion.isdigit() is True:
        if int(opcion) in range(1, len(datos)):
            tributo_seleccionado = datos[int(opcion)][0]
            respaldo_datos = c.cargar_tributos(p.RUTA_TRIBUTOS)
            with open(p.RUTA_TRIBUTOS, 'w') as archivo:  # Se reordena el archivo para que el tributo seleccionado se separe del resto
                for linea in respaldo_datos:
                    if linea[0] == tributo_seleccionado:
                        string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                        archivo.write("nombre,distrito,edad,vida,energía,agilidad,fuerza,ingenio,popularidad\n")
                        archivo.write(string)
            with open(p.RUTA_TRIBUTOS, 'a') as archivo:
                for linea in respaldo_datos:
                    if linea[0] != tributo_seleccionado and linea[0] != "nombre":
                        string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                        archivo.write(string)
        else:
            return False
    else:
        return False


def crear_archivo_participantes():
    respaldo = c.cargar_tributos(p.RUTA_TRIBUTOS)
    with open("datos/mochila_peso.csv", "w") as archivo:
        for linea in respaldo[1:]:
            archivo.write(f"{linea[0]};;0\n")


def actualizar_self(instancia):
    respaldo_datos = c.cargar_tributos(p.RUTA_TRIBUTOS)
    with open(p.RUTA_TRIBUTOS, 'w') as archivo:
        for linea in respaldo_datos:
            if instancia.nombre == linea[0]:
                string = f"{instancia.nombre},{instancia.distrito},{instancia.edad},{instancia.vida},{instancia.energia},{instancia.agilidad},{instancia.fuerza},{instancia.ingenio},{instancia.popularidad}\n"
                archivo.write(string)
            else:
                string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                archivo.write(string)


def actualizar_self_lista(lista):
    respaldo_datos = c.cargar_tributos(p.RUTA_TRIBUTOS)
    with open(p.RUTA_TRIBUTOS, 'w') as archivo:
        for linea in respaldo_datos:
            if lista[0] == linea[0]:
                string = f"{lista[0]},{lista[1]},{lista[2]},{lista[3]},{lista[4]},{lista[5]},{lista[6]},{lista[7]},{lista[8]}\n"
                archivo.write(string)
            else:
                string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                archivo.write(string)


def actualizar_mochila(tributo, objeto):
    respaldo = []
    with open("datos/mochila_peso.csv", "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(";")
            respaldo += [linea]
    with open("datos/mochila_peso.csv", "w") as archivo:
        for dato in respaldo:
            if tributo == dato[0]:
                suma_peso = int(objeto[2])
                mochila_actual = dato[1]
                mochila_actual = mochila_actual.strip().split(",")
                for elemento in mochila_actual:
                    if elemento.isdigit() is True:
                        suma_peso += int(elemento)
                mochila_nueva = f"{dato[1]},{objeto[0]},{objeto[1]},{objeto[2]}"
                if mochila_nueva[0] == ",":
                    mochila_nueva = mochila_nueva[1:]
                archivo.write(f"{dato[0]};{mochila_nueva};{suma_peso}\n")
    with open("datos/mochila_peso.csv", "a") as archivo:
        for dato in respaldo:
            if dato[0] != tributo:
                archivo.write(f"{dato[0]};{dato[1]};{dato[2]}\n")
    respal2 = []
    with open("datos/mochila_peso.csv", "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(";")
            respal2 += [linea]
    for lista in respal2:
        if lista[0] == tributo:
            return lista[1]


def retorna_peso(tributo):  # se llama si o si despues de llamar a mochila_peso
    with open("datos/mochila_peso.csv", "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(";")
            if linea[0] == tributo:
                return int(linea[2])


def retorna_mochila(tributo):
    with open("datos/mochila_peso.csv", "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(";")
            if linea[0] == tributo:
                objetos = ""
                lista_objetos = linea[1].split(",")
                for i in range(len(lista_objetos) // 3):
                    objetos += f",{lista_objetos[3 * i]}"
                objetos = objetos[1:]
                return objetos


def utilizar_objeto(lista):  # imprime el Menú de objetos y retorna el escogido
    print("""Objeto disponibles
------------------------------------""")
    for i in range(len(lista)):
        print(f"[{i + 1}] {lista[i]}")
    escogido = input("Seleccione un objeto: ")
    if escogido.isdigit() is True:
        if 0 < int(escogido) < len(lista) + 1:
            return lista[int(escogido) - 1]
        else:
            print("Respuesta inválida.")
            return utilizar_objeto(lista)
    else:
        print("Respuesta inválida.")
        return utilizar_objeto(lista)


def restar_objeto_mochila(nombre, objeto):
    respaldo = []
    lista_sin_objeto = []
    string_sin_objeto = ""
    peso = 0
    stop = False
    with open("datos/mochila_peso.csv", "r") as archivo:
        for linea in archivo.readlines():
            linea = linea.strip().split(";")
            respaldo += [linea]
    for dato in respaldo:
        if dato[0] == nombre:
            mochila = dato[1].split(",")
            for i in range(len(mochila)):
                if mochila[i] == objeto and stop is False:
                    peso += int(mochila[i + 2])
                    lista_sin_objeto = mochila[:i] + mochila[i+3:]
                    stop = True
                    for objeto_lista in lista_sin_objeto:
                        string_sin_objeto += str(objeto_lista) + ","
                    string_sin_objeto = string_sin_objeto[:len(string_sin_objeto) - 1]
            dato[1] = string_sin_objeto
    with open("datos/mochila_peso.csv", "w") as archivo:
        for dato in respaldo:
            archivo.write(f"{dato[0]};{dato[1]};{int(dato[2]) - peso}\n")


def ocurre_evento(daño):
    respaldo = c.cargar_tributos(p.RUTA_TRIBUTOS)
    for dato in respaldo[1:]:
        dato[3] = int(dato[3]) - daño
    with open(p.RUTA_TRIBUTOS, "w") as archivo:
        for dato in respaldo:
            archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]}\n")


def actualizar_encuentros(tributo):
    string = f"{tributo[0]},{tributo[1]},{tributo[2]},{tributo[3]},{tributo[4]},{tributo[5]},{tributo[6]},{tributo[7]},{tributo[8]}\n"
    respaldo = c.cargar_tributos(p.RUTA_TRIBUTOS)
    with open(p.RUTA_TRIBUTOS, "w") as archivo:
        for dato in respaldo:
            if dato[0] == tributo[0]:
                archivo.write(string)
            else:
                archivo.write(f"{dato[0]},{dato[1]},{dato[2]},{dato[3]},{dato[4]},{dato[5]},{dato[6]},{dato[7]},{dato[8]}\n")


def seleccionar_arena():
    arenas = c.cargar_arenas(p.RUTA_ARENAS)
    arenas = sorted(arenas, key=lambda x: x[2], reverse=False)
    print("""
            Arenas
---------------------------------""")
    for i in range(len(arenas) - 1):
        print(f"""[{i + 1}]
Arena: {arenas[i][0]}
Dificultad: {arenas[i][1]}
Riesgo: {arenas[i][2]}
""")
    seleccion = input("Seleccione una arena: ")
    if seleccion != "1" and seleccion != "2" and seleccion != "3":
        print("Respuesta inválida")
        print(" ")
        return seleccionar_arena()
    else:
        print(f"Ha escogido como arena a {arenas[int(seleccion) - 1][0]}")
    with open(p.RUTA_ARENAS, "w") as archivo:
        archivo.write("nombre,dificultad,riesgo\n")
        archivo.write(f"{arenas[int(seleccion) - 1][0]},{arenas[int(seleccion) - 1][1]},{arenas[int(seleccion) - 1][2]}\n")
        for arena in arenas:
            if arena[0] != arenas[int(seleccion) - 1][0] and arena[0] != "nombre":
                archivo.write(f"{arena[0]},{arena[1]},{arena[2]}\n")
        return arenas[int(seleccion) - 1][0]


def reiniciar_datos():
    ambientes = c.cargar_ambientes("respaldo_datos/ambientes.csv")
    tributos = c.cargar_tributos("respaldo_datos/tributos.csv")
    arenas = c.cargar_arenas("respaldo_datos/arenas.csv")
    objetos = c.cargar_objetos("respaldo_datos/objetos.csv")
    with open(p.RUTA_TRIBUTOS, "w") as archivo:
        for linea in tributos:
            archivo.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n")
    with open(p.RUTA_ARENAS, "w") as archivo:
        for linea in arenas:
            archivo.write(f"{linea[0]},{linea[1]},{linea[2]}\n")
    with open(p.RUTA_OBJETOS, "w") as archivo:
        for linea in objetos:
            archivo.write(f"{linea[0]},{linea[1]},{linea[2]}\n")
    with open(p.RUTA_AMBIENTES, "w") as archivo:
        for linea in ambientes:
            archivo.write(f"{linea[0]},{linea[1][0]};{linea[1][1]},{linea[2][0]};{linea[2][1]},{linea[3][0]};{linea[3][1]}\n")
