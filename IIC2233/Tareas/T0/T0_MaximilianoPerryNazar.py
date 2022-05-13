print(" ")
print("            ---¡Bienvenid@s a DCCommerce!---")
c0 = 0
from datetime import datetime
###### MENUS ######
from Menus import Menu
a = Menu()
def men_pub():
    pub = open('publicaciones.csv', 'r')
    data_pub = pub.readlines()
    data_pub1 = []
    data_pub2 = []
    data_pub3 = []
    archivo = open("publicaciones.csv", "r")
    for linea in archivo.readlines():
        data_pub1 += [linea]
    archivo.close()
    for i in range(len(data_pub2)):
        data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3], data_pub1[i][4]]
        for j in range(len(data_pub1[i])):
            if j > 4:
                data_pub3[i] += data_pub1[i][j] + ","
        data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
    for i in range(len(data_pub2)):
        data_pub2[i] += [data_pub3[i]]
    from datetime import date, time, datetime, timedelta
    print(" ")
    print("****** Menú de Publicaciones ******")
    print(" ")
    tiempo = []
    copia = data_pub2
    from datetime import date, time, datetime, timedelta
    for i in range(1, len(copia)):
        d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
        c = str(datetime.now() - d2)
        c = c.split(',')
        tiempo += [c]
    for i in range(len(tiempo)):
        tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
    for i in range(len(tiempo)):
        if len(tiempo[i][0]) > 7:
            tiempo[i] = [str(0), str(tiempo[i][0])]
            tiempo[i][1] = tiempo[i][1].split(":")
            tiempo[i] = [
                (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                    float(str(tiempo[i][1][0]))) * 60 * 60 + (
                    float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]

    for i in range(len(tiempo)):
        tiempo[i][1] = tiempo[i][1].split(":")
        tiempo[i] = [(float(str(tiempo[i][0]))) * 24 * 60 * 60 + (float(str(tiempo[i][1][0]))) * 60 * 60 + (
            float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
    for i in range(len(copia) - 1):
        tiempo[i] += [copia[i + 1]]
    tiempo.sort()
    for i in range(len(tiempo)):
        print(f"[{i + 1}] {tiempo[i][1][1]}")
    return " "
def men_pub_rea(nombre):
    print(" ")
    print("          ****** Mis publicaciones ******")
    print(" ")
    pub = open('publicaciones.csv', 'r')
    data_pub = pub.readlines()
    data_pub1 = []
    data_pub2 = []
    data_pub3 = []
    for i in range(len(data_pub)):
        data_pub1 += [data_pub[i].split(',')]
        data_pub2 += [[]]
        data_pub3 += [""]
    for i in range(len(data_pub1)):
        for j in range(len(data_pub1[i])):
            if "\n" in data_pub1[i][j]:
                data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
    for i in range(len(data_pub2)):
        data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3],
                         data_pub1[i][4]]
        for j in range(len(data_pub1[i])):
            if j > 4:
                data_pub3[i] += data_pub1[i][j] + ","
        data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
    for i in range(len(data_pub2)):
        data_pub2[i] += [data_pub3[i]]
    from datetime import date, time, datetime, timedelta
    if resp == "1":
        print(" ")
        print("****** Menú de Publicaciones ******")
        print(" ")
        tiempo = []
        copia = data_pub2
        from datetime import date, time, datetime, timedelta
        for i in range(1, len(copia)):
            d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
            c = str(datetime.now() - d2)
            c = c.split(',')
            tiempo += [c]
        for i in range(len(tiempo)):
            tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
        for i in range(len(tiempo)):
            if len(tiempo[i][0]) > 7:
                tiempo[i] = [str(0), str(tiempo[i][0])]
                tiempo[i][1] = tiempo[i][1].split(":")
                tiempo[i] = [
                    (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                        float(str(tiempo[i][1][0]))) * 60 * 60 + (
                        float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
            else:
                tiempo[i][1] = tiempo[i][1].split(":")
                tiempo[i] = [
                    (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (float(str(tiempo[i][1][0]))) * 60 * 60 + (
                        float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
        for i in range(len(copia) - 1):
            tiempo[i] += [copia[i + 1]]
        tiempo.sort()
        mis = []
        for i in range(len(tiempo)):
            if nombre == tiempo[i][1][2]:
                mis += [tiempo[i][1][1]]
        for i in range(len(mis)):
            print(f"- {mis[i]}")
        print(" ")
        print("          [1] Crear nueva publicación")
        print("          [2] Eliminar publicación")
        print("          [x] Volver")
        print(" ")
def fecha_actual():
    fecha = str(datetime.now())
    fecha2 = " "
    for x in range(len(fecha)):
        if fecha[x] != "-":
            fecha2 += fecha[x]
        elif fecha[x] == "-":
            fecha2 += "/"
    fecha2 = fecha2[1: len(fecha2) - 7]
    return fecha2
###### FIN MENUS ######

while c0 == 0:
    file = open('usuarios.csv')
    archivo = file.readlines()
    data_us = []
    for linea in archivo:
        if "\n" in linea:
            linea = linea[:len(linea) - 1]
            if linea != "usuario":
                data_us.append(linea)
    c0 = 1
    a.impresion()
    d0 = input("Por favor, seleccione una de las opciones (1, 2, 3, x): ")
    # PRIMERA OPCIÓN (1/5) #
    c1 = 0
    nombre = ","
    while c1 == 0:
        c1 = 1
        if d0 == "1":
            if nombre == ",":
                nombre = input("Ingrese su nombre de usuario: ")
            c4 = 0
            while c4 == 0:
                c4 = 1
                if nombre in data_us:
                    print("Abriendo Menú Principal...")
                    a.impr_men_pri()
                    resp = input("Por favor, seleccione una de las opciones (1, 2, x): ")
                    ###### CODIGO REUTILIZADO DENTRO DEL MISMO CODIGO ######
                    c5 = 0
                    while c5 == 0:
                        c5 = 1
                        pub = open('publicaciones.csv', 'r')
                        data_pub = pub.readlines()
                        data_pub1 = []
                        data_pub2 = []
                        data_pub3 = []
                        for i in range(len(data_pub)):
                            data_pub1 += [data_pub[i].split(',')]
                            data_pub2 += [[]]
                            data_pub3 += [""]
                        for i in range(len(data_pub1)):
                            for j in range(len(data_pub1[i])):
                                if "\n" in data_pub1[i][j]:
                                    data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
                        for i in range(len(data_pub2)):
                            data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3],
                                             data_pub1[i][4]]
                            for j in range(len(data_pub1[i])):
                                if j > 4:
                                    data_pub3[i] += data_pub1[i][j] + ","
                            data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                        for i in range(len(data_pub2)):
                            data_pub2[i] += [data_pub3[i]]
                        from datetime import date, time, datetime, timedelta
                        if resp == "1":
                            pub = open('publicaciones.csv', 'r')
                            data_pub = pub.readlines()
                            data_pub1 = []
                            data_pub2 = []
                            data_pub3 = []
                            for i in range(len(data_pub)):
                                data_pub1 += [data_pub[i].split(',')]
                                data_pub2 += [[]]
                                data_pub3 += [""]
                            for i in range(len(data_pub1)):
                                for j in range(len(data_pub1[i])):
                                    if "\n" in data_pub1[i][j]:
                                        data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
                            for i in range(len(data_pub2)):
                                data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3],
                                                 data_pub1[i][4]]
                                for j in range(len(data_pub1[i])):
                                    if j > 4:
                                        data_pub3[i] += data_pub1[i][j] + ","
                                data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                            for i in range(len(data_pub2)):
                                data_pub2[i] += [data_pub3[i]]
                            from datetime import date, time, datetime, timedelta
                            print(" ")
                            print("****** Menú de Publicaciones ******")
                            print(" ")
                            tiempo = []
                            copia = data_pub2
                            from datetime import date, time, datetime, timedelta
                            for i in range(1, len(copia)):
                                d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
                                c = str(datetime.now() - d2)
                                c = c.split(',')
                                tiempo += [c]
                            for i in range(len(tiempo)):
                                tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
                            for i in range(len(tiempo)):
                                if len(tiempo[i][0]) > 7:
                                    tiempo[i] = [str(0), str(tiempo[i][0])]
                                    tiempo[i][1] = tiempo[i][1].split(":")
                                    tiempo[i] = [
                                        (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                            float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                            float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                                else:
                                    tiempo[i][1] = tiempo[i][1].split(":")
                                    tiempo[i] = [
                                        (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                            float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                            float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                            for i in range(len(copia) - 1):
                                tiempo[i] += [copia[i + 1]]
                            tiempo.sort()
                            printeado = []
                            for i in range(len(tiempo)):
                                print(f"[{i + 1}] {tiempo[i][1][1]}")
                                printeado += [f"[{i + 1}] {tiempo[i][1][1]}"]
                                if i + 1 == len(tiempo):
                                    print("[x] Volver")
                            resp33 = input("Seleccione una opción: ")
                            if resp33 == "x":
                                c1 = 0
                            elif resp33 != "x":
                                respuestas = []
                                for i in range(len(tiempo)):
                                    respuestas += {i + 1}
                                verif3 = 0
                                for i in range(len(respuestas)):
                                    if resp33 == str(respuestas[i]):
                                        verif3 = 1
                                if verif3 == 0:
                                    print("Respuesta inválida.")
                                    c5 = 0
                                elif verif3 == 1:
                                    c7 = 0
                                    while c7 == 0:
                                        c7 = 1
                                        for i in range(len(printeado)):
                                            printeado[i] = printeado[i].split()
                                            printeado[i][0] = printeado[i][0][1 : len(printeado[i][0]) - 1]
                                            if resp33 == printeado[i][0]:
                                                print(f"""\n*** {tiempo[i][1][1]} ***
Creado: {tiempo[i][1][3]}
Vendedor: {tiempo[i][1][2]}
Precio: {tiempo[i][1][4]}
Descripción: {tiempo[i][1][5]}
Comentarios de la publicación: """)
                                                comen = open('comentarios.csv', 'r')
                                                comentarios = comen.readlines()
                                                comen.close()
                                                copia_com = comentarios
                                                com_def = []
                                                for j in range(len(copia_com)):
                                                    copia_com[j] = copia_com[j].split(',')
                                                    if copia_com[j][0] == tiempo[i][1][0]:
                                                        com_def += [copia_com[j]]
                                                for k in range(len(com_def)):
                                                    com_fin = " "
                                                    for j in range(len(com_def[k])):
                                                        if j >= 3:
                                                            com_fin += str(com_def[k][j]) + ","
                                                    com_fin = com_fin[1: len(com_fin) - 1]
                                                    pub = open('publicaciones.csv', 'r')
                                                    data_pub = pub.readlines()
                                                    data_pub1 = []
                                                    data_pub2 = []
                                                    data_pub3 = []
                                                    for i in range(len(data_pub)):
                                                        data_pub1 += [data_pub[i].split(',')]
                                                        data_pub2 += [[]]
                                                        data_pub3 += [""]
                                                    for i in range(len(data_pub1)):
                                                        for j in range(len(data_pub1[i])):
                                                            if "\n" in data_pub1[i][j]:
                                                                data_pub1[i][j] = (data_pub1[i][j])[
                                                                                  :len(data_pub1[i][j]) - 1]
                                                    for i in range(len(data_pub2)):
                                                        data_pub2[i] += [data_pub1[i][0], data_pub1[i][1],
                                                                         data_pub1[i][2], data_pub1[i][3],
                                                                         data_pub1[i][4]]
                                                        for j in range(len(data_pub1[i])):
                                                            if j > 4:
                                                                data_pub3[i] += data_pub1[i][j] + ","
                                                        data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                                                    for i in range(len(data_pub2)):
                                                        data_pub2[i] += [data_pub3[i]]
                                                    from datetime import date, time, datetime, timedelta
                                                    if resp == "1":
                                                        tiempo = []
                                                        copia = data_pub2
                                                        from datetime import date, time, datetime, timedelta
                                                        for i in range(1, len(copia)):
                                                            d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
                                                            c = str(datetime.now() - d2)
                                                            c = c.split(',')
                                                            tiempo += [c]
                                                        for i in range(len(tiempo)):
                                                            tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
                                                        for i in range(len(tiempo)):
                                                            if len(tiempo[i][0]) > 7:
                                                                tiempo[i] = [str(0), str(tiempo[i][0])]
                                                                tiempo[i][1] = tiempo[i][1].split(":")
                                                                tiempo[i] = [
                                                                    (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                                        float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                                        float(str(tiempo[i][1][1]))) * 60 + (
                                                                        float(str(tiempo[i][1][2])))]
                                                            else:
                                                                tiempo[i][1] = tiempo[i][1].split(":")
                                                                tiempo[i] = [
                                                                    (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                                        float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                                        float(str(tiempo[i][1][1]))) * 60 + (
                                                                        float(str(tiempo[i][1][2])))]
                                                        for i in range(len(copia) - 1):
                                                            tiempo[i] += [copia[i + 1]]
                                                        tiempo.sort()
                                                        printeado = []
                                                        for i in range(len(tiempo)):
                                                            printeado += [f"[{i + 1}] {tiempo[i][1][1]}"]
                                                            if i + 1 == len(tiempo) and k + 1 != len(com_def):
                                                                print(f"{com_def[k][2]} -- {com_def[k][1]}: {com_fin[: len(com_fin) - 1]}")
                                                            elif i + 1 == len(tiempo) and k + 1 == len(com_def):
                                                                print(
                                                                    f"{com_def[k][2]} -- {com_def[k][1]}: {com_fin[: len(com_fin)]}")
                                                resp333 = input("\n[1] Agregar comentario \n[x] Volver\nSeleccione una opción: ")
                                                print(" ")
                                                if resp333 == "x":
                                                    c5 = 0
                                                elif resp333 == "1":
                                                    comentario = input("Escriba a continuación su comentario: ")
                                                    fecha = fecha_actual()
                                                    transcripcion = str(f"\n{tiempo[i][1][0]},{nombre},{fecha},{comentario}")
                                                    coments = open('comentarios.csv', 'a')
                                                    coments.write(transcripcion)
                                                    coments.close()
                                                    print("Comentario ingresado.\nRedireccionando a Menú de Publicaciones.")
                                                    c5 = 0
                                                else:
                                                    print("Respuesta inválida. Redireccionando a Menú de Publicaciones.")
                                                    c5 = 0
                                                ###### FIN CÓDIGO REUTILIZADO ######
                        elif resp == "2":
                            c10 = 0
                            while c10 == 0:
                                c10 = 1
                                ###### CODIGO REUTILIZADO DENTRO DEL MISMO CODIGO ######
                                print(" ")
                                print("          ****** Mis publicaciones ******")
                                print(" ")
                                pub = open('publicaciones.csv', 'r')
                                data_pub = pub.readlines()
                                data_pub1 = []
                                data_pub2 = []
                                data_pub3 = []
                                for i in range(len(data_pub)):
                                    data_pub1 += [data_pub[i].split(',')]
                                    data_pub2 += [[]]
                                    data_pub3 += [""]
                                for i in range(len(data_pub1)):
                                    for j in range(len(data_pub1[i])):
                                        if "\n" in data_pub1[i][j]:
                                            data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
                                for i in range(len(data_pub2)):
                                    data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3],
                                                     data_pub1[i][4]]
                                    for j in range(len(data_pub1[i])):
                                        if j > 4:
                                            data_pub3[i] += data_pub1[i][j] + ","
                                    data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                                for i in range(len(data_pub2)):
                                    data_pub2[i] += [data_pub3[i]]
                                from datetime import date, time, datetime, timedelta
                                tiempo = []
                                copia = data_pub2
                                from datetime import date, time, datetime, timedelta

                                for i in range(1, len(copia)):
                                    d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
                                    c = str(datetime.now() - d2)
                                    c = c.split(',')
                                    tiempo += [c]
                                for i in range(len(tiempo)):
                                    tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
                                for i in range(len(tiempo)):
                                    if len(tiempo[i][0]) > 7:
                                        tiempo[i] = [str(0), str(tiempo[i][0])]
                                        tiempo[i][1] = tiempo[i][1].split(":")
                                        tiempo[i] = [
                                            (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                                    else:
                                        tiempo[i][1] = tiempo[i][1].split(":")
                                        tiempo[i] = [
                                            (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                                for i in range(len(copia) - 1):
                                    tiempo[i] += [copia[i + 1]]
                                tiempo.sort()
                                mis = []
                                for i in range(len(tiempo)):
                                    # print(f"nombre: {nombre} y tiempo: {tiempo[i][1][2]}")
                                    if nombre == tiempo[i][1][2]:
                                        mis += [tiempo[i][1][1]]

                                for i in range(len(mis)):
                                    print(f"- {mis[i]}")
                                print(" ")
                                print("          [1] Crear nueva publicación")
                                print("          [2] Eliminar publicación")
                                print("          [x] Volver")
                                print(" ")
                                ###### FIN CODIGO REUTILIZADO ######
                                resp2 = input("Por favor, seleccione una de las opciones (1, 2, x): ")
                                c9 = 0
                                while c9 == 0:
                                    c9 = 1
                                    if resp2 == "x":
                                        c1 = 0
                                    elif resp2 == "2":
                                        realizado = []
                                        num = []
                                        for i in range(len(data_pub2)):
                                            if nombre == data_pub2[i][2]:
                                                realizado += [data_pub2[i]]
                                        for i in range(len(realizado)):
                                            print(f"[{i + 1}] {realizado[i][1]} -- Creado el {realizado[i][3]}")
                                            num += str(i+1)
                                        print("[x] Volver")
                                        elim = input("¿Qué publicación desea eliminar? ")
                                        if str(elim) not in num and elim != "x":
                                            print("Respuesta inválida.")
                                            c9 = 0
                                        elif elim == "x":
                                            c10 = 0
                                        elif str(elim) in num:
                                            publica = open('publicaciones.csv', 'w')
                                            for i in range(len(data_pub)):
                                                datap = data_pub[i].split(",")
                                                if str(realizado[(int(elim)) - 1][3]) == str(datap[3]):
                                                    print(f"""Se eliminó exitosamente: {datap[1]}
Redireccionando a Menú Principal...""")
                                                    c4 = 0
                                                else:
                                                    publica.write(data_pub[i])
                                            publica.close()
                                    elif resp2 == "1":
                                        pub_nueva = " "
                                        producto = input("Escriba el producto que desea publicar: ")
                                        presio = input("Ingrese el precio del producto: ")
                                        descripcion = input("Añada una descripción acerca del producto: ")
                                        fecha = fecha_actual()
                                        pub_nueva = str(f"{int(tiempo[0][1][0]) + 1},{producto},{nombre},{fecha},{presio},{descripcion}")
                                        pubs = open('publicaciones.csv', 'a')
                                        pubs.write(pub_nueva)
                                        pubs.write("\n")
                                        pubs.close()
                                        print("¡Muchas gracias por ingresar un nuevo producto! \nA continuación lo redireccionaremos al Menú Principal.\nRedireccionando..." )
                                        c4 = 0
                                    elif resp2 != "1" and resp2 != "2" and resp2 != "x":
                                        print("Respuesta inválida.")
                                        c10 = 0

                        elif resp == "x":
                            c0 = 0
                        else:
                            print("Respuesta inváldia. Redireccionando a Menu Inicio.")
                            c0 = 0

                elif nombre not in data_us:
                    print(" ")
                    print("############################################# ")
                    print("Nombre de usuario inválido.")
                    print("Recuerde respetar las mayúsculas y minúsculas.")
                    c0 = 0

    # SEGUNDA OPCIÓN (2/5) #
    c2 = 0
    while c2 == 0:
        c2 = 1
        if d0 == "2":
            nombre = input("Ingrese el nombre con el que desee registrarse: ")
            if ',' in nombre or len(nombre) < 1 or len(nombre) > 15:
                print("Nombre de usuario inválido. Redireccionando a Menú Inicio...")
                c0 = 0
            else:
                verif = True
                for nom in data_us:
                    if nombre == nom:
                        print("Nombre de usuario inválido. Redireccionando a Menú Inicio...")
                        verif = False
                        c0 = 0
                if verif == True:
                    data_us += [nombre]
                    verif2 = True
                    for linea in archivo:
                        if nombre == linea[:len(linea) - 1] or nombre == archivo[len(archivo) - 1]:
                            verif2 = False
                    if verif2 == True:
                        usuarios = open('usuarios.csv', 'a')
                        usuarios.write(f"\n{nombre}")
                        usuarios.close()
                        c19 = 0
                        while c19 == 0:
                            c19 = 1
                            print("Abriendo Menú Principal...")
                            a.impr_men_pri()
                            resp = input("Por favor, seleccione una de las opciones (1, 2, x): ")
                            ###### CODIGO REUTILIZADO DENTRO DEL MISMO CODIGO ######
                            c5 = 0
                            while c5 == 0:
                                c5 = 1
                                pub = open('publicaciones.csv', 'r')
                                data_pub = pub.readlines()
                                data_pub1 = []
                                data_pub2 = []
                                data_pub3 = []
                                for i in range(len(data_pub)):
                                    data_pub1 += [data_pub[i].split(',')]
                                    data_pub2 += [[]]
                                    data_pub3 += [""]
                                for i in range(len(data_pub1)):
                                    for j in range(len(data_pub1[i])):
                                        if "\n" in data_pub1[i][j]:
                                            data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
                                for i in range(len(data_pub2)):
                                    data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3],
                                                     data_pub1[i][4]]
                                    for j in range(len(data_pub1[i])):
                                        if j > 4:
                                            data_pub3[i] += data_pub1[i][j] + ","
                                    data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                                for i in range(len(data_pub2)):
                                    data_pub2[i] += [data_pub3[i]]
                                from datetime import date, time, datetime, timedelta
                                if resp == "1":
                                    pub = open('publicaciones.csv', 'r')
                                    data_pub = pub.readlines()
                                    data_pub1 = []
                                    data_pub2 = []
                                    data_pub3 = []
                                    for i in range(len(data_pub)):
                                        data_pub1 += [data_pub[i].split(',')]
                                        data_pub2 += [[]]
                                        data_pub3 += [""]
                                    for i in range(len(data_pub1)):
                                        for j in range(len(data_pub1[i])):
                                            if "\n" in data_pub1[i][j]:
                                                data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
                                    for i in range(len(data_pub2)):
                                        data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3],
                                                         data_pub1[i][4]]
                                        for j in range(len(data_pub1[i])):
                                            if j > 4:
                                                data_pub3[i] += data_pub1[i][j] + ","
                                        data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                                    for i in range(len(data_pub2)):
                                        data_pub2[i] += [data_pub3[i]]
                                    from datetime import date, time, datetime, timedelta
                                    print(" ")
                                    print("****** Menú de Publicaciones ******")
                                    print(" ")
                                    tiempo = []
                                    copia = data_pub2
                                    from datetime import date, time, datetime, timedelta
                                    for i in range(1, len(copia)):
                                        d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
                                        c = str(datetime.now() - d2)
                                        c = c.split(',')
                                        tiempo += [c]
                                    for i in range(len(tiempo)):
                                        tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
                                    for i in range(len(tiempo)):
                                        if len(tiempo[i][0]) > 7:
                                            tiempo[i] = [str(0), str(tiempo[i][0])]
                                            tiempo[i][1] = tiempo[i][1].split(":")
                                            tiempo[i] = [
                                                (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                    float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                    float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                                        else:
                                            tiempo[i][1] = tiempo[i][1].split(":")
                                            tiempo[i] = [
                                                (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                    float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                    float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                                    for i in range(len(copia) - 1):
                                        tiempo[i] += [copia[i + 1]]
                                    tiempo.sort()
                                    printeado = []
                                    for i in range(len(tiempo)):
                                        print(f"[{i + 1}] {tiempo[i][1][1]}")
                                        printeado += [f"[{i + 1}] {tiempo[i][1][1]}"]
                                        if i + 1 == len(tiempo):
                                            print("[x] Volver")
                                    resp33 = input("Seleccione una opción: ")
                                    if resp33 == "x":
                                        c19 = 0
                                    elif resp33 != "x":
                                        respuestas = []
                                        for i in range(len(tiempo)):
                                            respuestas += {i + 1}
                                        verif3 = 0
                                        for i in range(len(respuestas)):
                                            if resp33 == str(respuestas[i]):
                                                verif3 = 1
                                        if verif3 == 0:
                                            print("Respuesta inválida.")
                                            c5 = 0
                                        elif verif3 == 1:
                                            c7 = 0
                                            while c7 == 0:
                                                c7 = 1
                                                for i in range(len(printeado)):
                                                    printeado[i] = printeado[i].split()
                                                    printeado[i][0] = printeado[i][0][1: len(printeado[i][0]) - 1]
                                                    if resp33 == printeado[i][0]:
                                                        print(f"""\n*** {tiempo[i][1][1]} ***
    Creado: {tiempo[i][1][3]}
    Vendedor: {tiempo[i][1][2]}
    Precio: {tiempo[i][1][4]}
    Descripción: {tiempo[i][1][5]}
    Comentarios de la publicación: """)
                                                        comen = open('comentarios.csv', 'r')
                                                        comentarios = comen.readlines()
                                                        comen.close()
                                                        copia_com = comentarios
                                                        com_def = []
                                                        for j in range(len(copia_com)):
                                                            copia_com[j] = copia_com[j].split(',')
                                                            if copia_com[j][0] == tiempo[i][1][0]:
                                                                com_def += [copia_com[j]]
                                                        for k in range(len(com_def)):
                                                            com_fin = " "
                                                            for j in range(len(com_def[k])):
                                                                if j >= 3:
                                                                    com_fin += str(com_def[k][j]) + ","
                                                            com_fin = com_fin[1: len(com_fin) - 1]
                                                            pub = open('publicaciones.csv', 'r')
                                                            data_pub = pub.readlines()
                                                            data_pub1 = []
                                                            data_pub2 = []
                                                            data_pub3 = []
                                                            for i in range(len(data_pub)):
                                                                data_pub1 += [data_pub[i].split(',')]
                                                                data_pub2 += [[]]
                                                                data_pub3 += [""]
                                                            for i in range(len(data_pub1)):
                                                                for j in range(len(data_pub1[i])):
                                                                    if "\n" in data_pub1[i][j]:
                                                                        data_pub1[i][j] = (data_pub1[i][j])[
                                                                                          :len(data_pub1[i][j]) - 1]
                                                            for i in range(len(data_pub2)):
                                                                data_pub2[i] += [data_pub1[i][0], data_pub1[i][1],
                                                                                 data_pub1[i][2], data_pub1[i][3],
                                                                                 data_pub1[i][4]]
                                                                for j in range(len(data_pub1[i])):
                                                                    if j > 4:
                                                                        data_pub3[i] += data_pub1[i][j] + ","
                                                                data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                                                            for i in range(len(data_pub2)):
                                                                data_pub2[i] += [data_pub3[i]]
                                                            from datetime import date, time, datetime, timedelta
                                                            if resp == "1":
                                                                print(" ")
                                                                print("****** Menú de Publicaciones ******")
                                                                print(" ")
                                                                tiempo = []
                                                                copia = data_pub2
                                                                from datetime import date, time, datetime, timedelta
                                                                for i in range(1, len(copia)):
                                                                    d2 = datetime.strptime(data_pub2[i][3],
                                                                                           '%Y/%m/%d %H:%M:%S')
                                                                    c = str(datetime.now() - d2)
                                                                    c = c.split(',')
                                                                    tiempo += [c]
                                                                for i in range(len(tiempo)):
                                                                    tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
                                                                for i in range(len(tiempo)):
                                                                    if len(tiempo[i][0]) > 7:
                                                                        tiempo[i] = [str(0), str(tiempo[i][0])]
                                                                        tiempo[i][1] = tiempo[i][1].split(":")
                                                                        tiempo[i] = [
                                                                            (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                                                float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                                                float(str(tiempo[i][1][1]))) * 60 + (
                                                                                float(str(tiempo[i][1][2])))]
                                                                    else:
                                                                        tiempo[i][1] = tiempo[i][1].split(":")
                                                                        tiempo[i] = [
                                                                            (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                                                float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                                                float(str(tiempo[i][1][1]))) * 60 + (
                                                                                float(str(tiempo[i][1][2])))]
                                                                for i in range(len(copia) - 1):
                                                                    tiempo[i] += [copia[i + 1]]
                                                                tiempo.sort()
                                                                ###### FIN CODIGO REUTILIZADO ######
                                                                printeado = []
                                                                for i in range(len(tiempo)):
                                                                    print(f"[{i + 1}] {tiempo[i][1][1]}")
                                                                    printeado += [f"[{i + 1}] {tiempo[i][1][1]}"]
                                                                    if i + 1 == len(tiempo) and k + 1 != len(com_def):
                                                                        print(f"{com_def[k][2]} -- {com_def[k][1]}: {com_fin[: len(com_fin) - 1]}")
                                                                    elif i + 1 == len(tiempo) and k + 1 == len(com_def):
                                                                        print(f"{com_def[k][2]} -- {com_def[k][1]}: {com_fin[: len(com_fin)]}")
                                                        resp333 = input("\n[1] Agregar comentario \n[x] Volver\nSeleccione una opción: ")
                                                        print(" ")
                                                        if resp333 == "x":
                                                            c5 = 0
                                                        elif resp333 == "1":
                                                            comentario = input("Escriba a continuación su comentario: ")
                                                            fecha = fecha_actual()
                                                            print(fecha)
                                                            transcripcion = str(
                                                                f"\n{tiempo[i][1][0]},{nombre},{fecha},{comentario}")
                                                            coments = open('comentarios.csv', 'a')
                                                            coments.write(transcripcion)
                                                            coments.close()
                                                            print("Comentario ingresado.\nRedireccionando a Menú de Publicaciones.")
                                                            c5 = 0
                                                        else:
                                                            print(
                                                                "Respuesta inválida. Redireccionando a Menú de Publicaciones.")
                                                            c5 = 0
                                elif resp == "2":
                                    c10 = 0
                                    while c10 == 0:
                                        c10 = 1
                                        ###### CODIGO REUTILIZADO DENTRO DEL MISMO ######
                                        print(" ")
                                        print("             ****** Mis publicaciones ******")
                                        print(" ")
                                        pub = open('publicaciones.csv', 'r')
                                        data_pub = pub.readlines()
                                        data_pub1 = []
                                        data_pub2 = []
                                        data_pub3 = []
                                        for i in range(len(data_pub)):
                                            data_pub1 += [data_pub[i].split(',')]
                                            data_pub2 += [[]]
                                            data_pub3 += [""]
                                        for i in range(len(data_pub1)):
                                            for j in range(len(data_pub1[i])):
                                                if "\n" in data_pub1[i][j]:
                                                    data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
                                        for i in range(len(data_pub2)):
                                            data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2],
                                                             data_pub1[i][3],
                                                             data_pub1[i][4]]
                                            for j in range(len(data_pub1[i])):
                                                if j > 4:
                                                    data_pub3[i] += data_pub1[i][j] + ","
                                            data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                                        for i in range(len(data_pub2)):
                                            data_pub2[i] += [data_pub3[i]]
                                        from datetime import date, time, datetime, timedelta
                                        tiempo = []
                                        copia = data_pub2
                                        from datetime import date, time, datetime, timedelta
                                        for i in range(1, len(copia)):
                                            d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
                                            c = str(datetime.now() - d2)
                                            c = c.split(',')
                                            tiempo += [c]
                                        for i in range(len(tiempo)):
                                            tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
                                        for i in range(len(tiempo)):
                                            if len(tiempo[i][0]) > 7:
                                                tiempo[i] = [str(0), str(tiempo[i][0])]
                                                tiempo[i][1] = tiempo[i][1].split(":")
                                                tiempo[i] = [
                                                    (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                        float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                        float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                                            else:
                                                tiempo[i][1] = tiempo[i][1].split(":")
                                                tiempo[i] = [
                                                    (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                                        float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                                        float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                                        for i in range(len(copia) - 1):
                                            tiempo[i] += [copia[i + 1]]
                                        tiempo.sort()
                                        mis = []
                                        for i in range(len(tiempo)):
                                            if nombre == tiempo[i][1][2]:
                                                mis += [tiempo[i][1][1]]
                                        for i in range(len(mis)):
                                            print(f"- {mis[i]}")
                                        print(" ")
                                        print("             [1] Crear nueva publicación")
                                        print("             [2] Eliminar publicación")
                                        print("             [x] Volver")
                                        print(" ")
                                        resp2 = input("Por favor, seleccione una de las opciones (1, 2, x): ")
                                        c9 = 0
                                        while c9 == 0:
                                            c9 = 1
                                            if resp2 == "x":
                                                c19 = 0
                                            elif resp2 == "2":
                                                realizado = []
                                                num = []
                                                for i in range(len(data_pub2)):
                                                    if nombre == data_pub2[i][2]:
                                                        realizado += [data_pub2[i]]
                                                for i in range(len(realizado)):
                                                    print(f"[{i + 1}] {realizado[i][1]} -- Creado el {realizado[i][3]}")
                                                    num += str(i + 1)
                                                print("[x] Volver")
                                                elim = input("¿Qué publicación desea eliminar? ")
                                                if str(elim) not in num and elim != "x":
                                                    print("Respuesta inválida.")
                                                    c5 = 0
                                                elif elim == "x":
                                                    c5 = 0
                                                elif str(elim) in num:
                                                    publica = open('publicaciones.csv', 'w')
                                                    for i in range(len(data_pub)):
                                                        datap = data_pub[i].split(",")
                                                        if str(realizado[(int(elim)) - 1][3]) == str(datap[3]):
                                                            print(f"""Se eliminó exitosamente: {datap[1]}
Redireccionando a Menú Principal...""")
                                                            c4 = 0
                                                        else:
                                                            publica.write(data_pub[i])
                                                    publica.close()
                                                c5 = 0
                                            elif resp2 == "1":
                                                pub_nueva = " "
                                                producto = input("Escriba el producto que desea publicar: ")
                                                presio = input("Ingrese el precio del producto: ")
                                                descripcion = input("Añada una descripción acerca del producto: ")
                                                fecha = fecha_actual()
                                                pub_nueva = str(
                                                    f"{int(tiempo[0][1][0]) + 1},{producto},{nombre},{fecha},{presio},{descripcion}")
                                                pubs = open('publicaciones.csv', 'a')
                                                pubs.write(pub_nueva)
                                                pubs.write("\n")
                                                pubs.close()
                                                print("¡Muchas gracias por ingresar un nuevo producto! \nA continuación lo redireccionaremos al Menú Principal.\nRedireccionando...")
                                                c5 = 0
                                            elif resp2 != "1" and resp2 != "2" and resp2 != "x":
                                                print("Respuesta inválida.")
                                                c10 = 0
                                elif resp == "x":
                                    print("Redireccionando a Menu Inicio.")
                                    c0 = 0
                                elif resp != "1" and resp != "2" and resp != "x":
                                    print("Respuesta inválida. Redireccionando a Menu Inicio.")
                                    c19 = 0
                    elif verif2 == False:
                        print("Nombre de usuario inválido. Redireccionando a Menú Inicio...")
                        verif = False
                        c0 = 0
                    file = open('usuarios.csv')
                    archivo = file.readlines()

    # TERCERA OPCIÓN (3/5) #
    c3 = 0
    while c3 == 0:
        c3 = 1
        if d0 == "3":
            print("Abriendo el Menú Principal...")
            a.impr_men_pri()
            resp = input("Por favor, seleccione una de las opciones (1, 2, x): ")
            if resp == "x":
                c0 = 0
            elif resp == "2":
                print("Lo lamento, debe registrarse o iniciar sesión para poder ingresar a esta sección")
                c3 = 0
            elif resp != "x" and resp != "1" and resp != "2":
                print("Respuesta inválida.")
                c3 = 0
            elif resp == "1":
                c6 = 0
                while c6 == 0:
                    c6 = 1
                    pub = open('publicaciones.csv', 'r')
                    data_pub = pub.readlines()
                    data_pub1 = []
                    data_pub2 = []
                    data_pub3 = []
                    for i in range(len(data_pub)):
                        data_pub1 += [data_pub[i].split(',')]
                        data_pub2 += [[]]
                        data_pub3 += [""]
                    for i in range(len(data_pub1)):
                        for j in range(len(data_pub1[i])):
                            if "\n" in data_pub1[i][j]:
                                data_pub1[i][j] = (data_pub1[i][j])[:len(data_pub1[i][j]) - 1]
                    for i in range(len(data_pub2)):
                        data_pub2[i] += [data_pub1[i][0], data_pub1[i][1], data_pub1[i][2], data_pub1[i][3],
                                         data_pub1[i][4]]
                        for j in range(len(data_pub1[i])):
                            if j > 4:
                                data_pub3[i] += data_pub1[i][j] + ","
                        data_pub3[i] = data_pub3[i][:len(data_pub3[i]) - 1]
                    for i in range(len(data_pub2)):
                        data_pub2[i] += [data_pub3[i]]
                    from datetime import date, time, datetime, timedelta
                    print(" ")
                    print("****** Menú de Publicaciones ******")
                    print(" ")
                    tiempo = []
                    copia = data_pub2
                    from datetime import date, time, datetime, timedelta
                    for i in range(1, len(copia)):
                        d2 = datetime.strptime(data_pub2[i][3], '%Y/%m/%d %H:%M:%S')
                        c = str(datetime.now() - d2)
                        c = c.split(',')
                        tiempo += [c]
                    for i in range(len(tiempo)):
                        tiempo[i][0] = tiempo[i][0][:len(tiempo[i][0]) - 4]
                    for i in range(len(tiempo)):
                        if len(tiempo[i][0]) > 7:
                            tiempo[i] = [str(0), str(tiempo[i][0])]
                            tiempo[i][1] = tiempo[i][1].split(":")
                            tiempo[i] = [
                                (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (
                                    float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                    float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                        else:
                            tiempo[i][1] = tiempo[i][1].split(":")
                            tiempo[i] = [
                                (float(str(tiempo[i][0]))) * 24 * 60 * 60 + (float(str(tiempo[i][1][0]))) * 60 * 60 + (
                                    float(str(tiempo[i][1][1]))) * 60 + (float(str(tiempo[i][1][2])))]
                    for i in range(len(copia) - 1):
                        tiempo[i] += [copia[i + 1]]
                    tiempo.sort()
                    printeado =[]
                    for i in range(len(tiempo)):
                        print(f"[{i + 1}] {tiempo[i][1][1]}")
                        printeado += [f"[{i + 1}] {tiempo[i][1][1]}"]
                        if i + 1 == len(tiempo):
                            print("[x] Volver")
                    resp33 = input("Seleccione una opción: ")
                    if resp33 == "x":
                        c3 = 0
                    elif resp33 != "x":
                        respuestas = []
                        for i in range(len(tiempo)):
                            respuestas += {i + 1}
                        verif3 = 0
                        for i in range(len(respuestas)):
                            if resp33 == str(respuestas[i]):
                                verif3 = 1
                        if verif3 == 0:
                            print("Respuesta inválida.")
                            c6 = 0
                        elif verif3 == 1:
                            c7 = 0
                            while c7 == 0:
                                c7 = 1
                                for i in range(len(printeado)):
                                    if resp33 == printeado[i][1:len(resp33)+1]:
                                        print(f"""\n*** {tiempo[i][1][1]} ***
Creado: {tiempo[i][1][3]}
Vendedor: {tiempo[i][1][2]}
Precio: {tiempo[i][1][4]}
Descripción: {tiempo[i][1][5]}
Comentarios de la publicación: """)
                                        comen = open('comentarios.csv', 'r')
                                        comentarios = comen.readlines()
                                        comen.close()
                                        copia_com = comentarios
                                        com_def = []
                                        for j in range(len(copia_com)):
                                            copia_com[j] = copia_com[j].split(',')
                                            if copia_com[j][0] == tiempo[i][1][0]:
                                                com_def += [copia_com[j]]
                                        for k in range(len(com_def)):
                                            com_fin = " "
                                            for j in range(len(com_def[k])):
                                                if j >= 3:
                                                    com_fin += str(com_def[k][j]) + ","
                                            com_fin = com_fin[1: len(com_fin) - 1]
                                            if i + 1 == len(tiempo) and k + 1 != len(com_def):
                                                print(
                                                    f"{com_def[k][2]} -- {com_def[k][1]}: {com_fin[: len(com_fin) - 1]}")
                                            elif i + 1 == len(tiempo) and k + 1 == len(com_def):
                                                print(
                                                    f"{com_def[k][2]} -- {com_def[k][1]}: {com_fin[: len(com_fin)]}")
                                        resp333 = input("\n[1] Agregar comentario \n[x] Volver\nSeleccione una opción: ")
                                        print(" ")
                                        if resp333 == "x":
                                            c6 = 0
                                        elif resp333 == "1":
                                            print(
                                                "Debe registrarse para agregar un comentario. Redireccionando a Menú de Publicaciones.")
                                            c6 = 0
                                        else:
                                            print("Respuesta inválida. Redireccionando a Menú de Publicaciones.")
                                            c6 = 0
# CUARTA Y QUINTA OPCIÓN (4/5) y (5/5) #
    if d0 == "x":
        print("¡Ha salido exitosamente del programa!")
    if d0 != "1" and d0 != "2" and d0 != "3" and d0 != "x":
        print(" ")
        print("Por favor ingrese una respuesta válida")
        c0 = 0