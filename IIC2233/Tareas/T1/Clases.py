import parametros as p
import cargar_datos as c
import funciones as f
from random import randint
from abc import ABC, abstractmethod


class Tributo:

    def __init__(self, tributo):  # Recibe una lista como input
        self.nombre = tributo[0]
        self.distrito = tributo[1]
        self.edad = int(tributo[2])
        self.vida = int(tributo[3])
        self.energia = int(tributo[4])
        self.energia_inicial = int(tributo[4])
        self.agilidad = int(tributo[5])
        self.fuerza = int(tributo[6])
        self.ingenio = int(tributo[7])
        self.popularidad = int(tributo[8])
        self.popularidad_inicial = int(tributo[8])
        self.dano = 0

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, value):
        self.__energia = min(max(value, 0), 100)

    @property
    def popularidad(self):
        return self.__popularidad

    @popularidad.setter
    def popularidad(self, value):
        self.__popularidad = min(max(value, 0), 100)

    def accion_heroica(self):  # Inicio opción Acción Heroica
        if self.energia < p.ENERGIA_ACCION_HEROICA:
            return False
        else:
            self.energia -= p.ENERGIA_ACCION_HEROICA
            self.popularidad += p.POPULARIDAD_ACCION_HEROICA
            self.notificar()
            respaldo_datos = c.cargar_tributos(p.RUTA_TRIBUTOS)
            with open(p.RUTA_TRIBUTOS, 'w') as archivo:
                for linea in respaldo_datos:
                    if self.nombre == linea[0]:
                        string = f"{self.nombre},{self.distrito},{self.edad},{self.vida},{self.energia},{self.agilidad},{self.fuerza},{self.ingenio},{self.popularidad}\n"
                        archivo.write(string)
                    else:
                        string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                        archivo.write(string)

    def notificar(self):
        print(f"""{self.nombre} ha realizado una acción súmamente heroica ¡WOW!.

Energía Inicial: {self.energia_inicial}
Energía Actual: {self.energia}

Popularidad Inicial: {self.popularidad_inicial}
Popularidad Actual: {self.popularidad}
""")  # Fin opción Accion Heroica

    def atacar_tributo(self):  # Inicio opción Atacar Tributo
        self.actualizar_dano()  # Se actualiza, ya que parte valiendo 0
        respaldo_datos = c.cargar_tributos(p.RUTA_TRIBUTOS)
        print("""
Nombre: Vida""")
        turno = 1
        for dato in respaldo_datos[2:]:
            print(f"[{turno}] {dato[0]}: {dato[3]}")
            turno += 1
        tributo_atacado = input("Escoja un tributo a atacar: ")
        if tributo_atacado.isdigit() is True:
            if int(tributo_atacado) in range(1, len(respaldo_datos)):
                self.actualizar_dano()
                if self.energia >= p.ENERGIA_ATACAR:
                    self.energia -= p.ENERGIA_ATACAR
                    nombre_atacado = respaldo_datos[int(tributo_atacado) + 1][0]
                    with open(p.RUTA_TRIBUTOS, 'w') as archivo:
                        for linea in respaldo_datos:
                            if nombre_atacado == linea[0]:
                                print(f"Objetivo a atacar: {nombre_atacado}")
                                vida_atacada = max(0, int(linea[3]) - self.dano)
                                print(f"Le ha causado {self.dano} de daño a {nombre_atacado}, dejando su vida en {vida_atacada}.")
                                string = f"{linea[0]},{linea[1]},{linea[2]},{vida_atacada},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                                archivo.write(string)
                                if vida_atacada == 0:  # Muerte de tributo
                                    self.popularidad += p.POPULARIDAD_ATACAR
                            else:
                                string = f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]}\n"
                                archivo.write(string)
                    f.actualizar_self(self)
                    f.actualizar_vivos()
                    print(" ")
                else:
                    print("No tiene suficiente energía para realizar esta acción.")
                    return False

            else:
                print("Respuesta inválida")
                self.atacar_tributo()
        else:
            print("Respuesta inválida")
            self.atacar_tributo()  # Fin opción Atacar Tributo

    def pedir_objeto_a_patrocinadores(self):  # Inicio opción pedir objetos
        datos_objetos = c.cargar_objetos(p.RUTA_OBJETOS)
        indice_objeto_nuevo = randint(1, len(datos_objetos) - 1)
        if self.popularidad >= p.POPULARIDAD_PEDIR:
            f.actualizar_mochila(self.nombre, [datos_objetos[indice_objeto_nuevo][0],datos_objetos[indice_objeto_nuevo][1],datos_objetos[indice_objeto_nuevo][2]])
            f.retorna_peso(self.nombre)
            self.popularidad -= p.POPULARIDAD_PEDIR
            print(f"""Ha obtenido {datos_objetos[indice_objeto_nuevo][0]} a cambio de {p.POPULARIDAD_PEDIR} puntos de popularidad.
Popularidad actual: {self.popularidad}""")
            f.actualizar_self(self)
            self.actualizar_dano()
            print(f"""Debido a este nuevo objeto, su daño ha pasado disminuido.
Daño actual: {self.dano}""")
        else:
            print("No dispone de suficiente popularidad para pedir un objeto.")  # Fin opción pedir objetos

    def hacerse_bolita(self):  # Inicio opción hacerse bolita
        print(f"""Arriesgada jugada...
*procede a hacerse bolita*
Su energía ha pasado de {self.energia} a {self.energia + p.ENERGIA_BOLITA}""")
        self.energia += p.ENERGIA_BOLITA
        f.actualizar_self(self)  # Fin opción hacerse bolita

    def ver_estado_actual(self):
        print(f"""                      Estado Tributo
-----------------------------------------------------------------
Nombre: {self.nombre}
Distrito: {self.distrito}
Edad: {self.edad}
Vida: {self.vida}
Energía: {self.energia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
Ingenio: {self.ingenio}
Popularidad: {self.popularidad}
Objetos: {f.retorna_mochila(self.nombre)}
Peso: {f.retorna_peso(self.nombre)}
""")

    def actualizar_dano(self):
        self.dano = max(0, round(((60 * self.fuerza) + (40 * self.agilidad) + (40 * self.ingenio) - (30 * int(f.retorna_peso(self.nombre))))/self.edad))  # El daño se redondea para poder mantener la vida de los tributos en un int


class Ambiente:

    def __init__(self):
        self.nombre_ambiente = c.cargar_ambientes(p.RUTA_AMBIENTES)[1][0]
        self.evento = c.cargar_ambientes(p.RUTA_AMBIENTES)[1][1:]

    def rotar_ambientes(self):  # metodo a usar despues de simulacion_hora
        data = c.cargar_ambientes(p.RUTA_AMBIENTES)
        datos = [data[0]] + data[2:len(data)] + [data[1]]
        with open(p.RUTA_AMBIENTES, "w") as archivo:
            archivo.write(f"{data[0][0]},{data[0][1][0]};{data[0][1][1]},{data[0][2][0]};{data[0][2][1]},{data[0][3][0]};{data[0][3][1]}\n")
            for dato in datos[1:]:
                archivo.write(f"{dato[0]},{dato[1][0]};{dato[1][1]},{dato[2][0]};{dato[2][1]},{dato[3][0]};{dato[3][1]}\n")

    def calcular_daño(self):
        if self.nombre_ambiente == "bosque":
            return max(5, round(((0.4 * 0) + (0.2 * p.VELOCIDAD_VIENTOS_BOSQUE) + (0.1 * p.PRECIPITACIONES_BOSQUE) + (0.3 * 0) + int(self.evento[randint(0, 2)][1])) / 5))
        if self.nombre_ambiente == "playa":
            return max(5, round(((0.4 * p.HUMEDAD_PLAYA) + (0.2 * p.VELOCIDAD_VIENTOS_PLAYA) + (0.1 * 0) + (0.3 * 0) + int(self.evento[randint(0, 2)][1])) / 5))
        else:
            return max(5, round(((0.4 * 0) + (0.2 * 0) + (0.1 * p.PRECIPITACIONES_MONTAÑA) + (0.3 * p.NUBOSIDAD_MONTAÑA) + int(self.evento[randint(0, 2)][1])) / 5))


class Arena(Tributo):

    def __init__(self, tributo):
        Tributo.__init__(self, tributo)
        Ambiente.__init__(self)
        self.arena = c.cargar_arenas(p.RUTA_ARENAS)[1][0]
        self.jugador = tributo[0]  # tributo = lista
        self.riesgo = 0
        self.dificultad = ""
        self.tributos = c.cargar_tributos(p.RUTA_TRIBUTOS)[1:]  # a partir del segundo tributo se encontrarán todo el resto
        self.ambientes = c.cargar_ambientes(p.RUTA_AMBIENTES)

    def setear_datos(self):
        data_arenas = c.cargar_arenas(p.RUTA_ARENAS)
        for dato in data_arenas:
            if dato[0] == self.arena:
                self.dificultad = str(dato[1])
                self.riesgo = float(dato[2])

    def ejecutar_evento(self):
        FIN = False
        self.setear_datos()
        jugador = c.cargar_tributos(p.RUTA_TRIBUTOS)[1][0]
        numero_aleatorio = randint(1, 100)
        if numero_aleatorio >= int(round(p.PROBABILIDAD_EVENTO * 100)):
            print(f"¡Se ejecutó un evento aleatorio dentro de: {c.cargar_ambientes(p.RUTA_AMBIENTES)[1][0]}")
            daño = Ambiente().calcular_daño()
            print(f"Todos los tributos han sufrido {daño} de daño.")
            print(" ")
            f.ocurre_evento(daño)
        f.actualizar_vivos()
        if c.cargar_tributos(p.RUTA_TRIBUTOS)[1][0] != jugador:
            FIN = True
        if FIN is True:
            print(f"¡OH NO! Su tributo, {self.jugador} ha muerto.")
            print("Redireccionando a Menú de Incio...")
            return False

    def encuentros(self):
        FIN = False
        self.setear_datos()
        num_encuentros = int(self.riesgo * (len(self.tributos)) // 2)
        print("ENCUENTROS:")
        if len(self.tributos) == 2:
            atacante = c.cargar_tributos(p.RUTA_TRIBUTOS)[2]
            atacado = c.cargar_tributos(p.RUTA_TRIBUTOS)[1]
            daño = round(min(90, max(5, ((60 * int(atacante[6]) + (40 * int(atacante[5])) + (40 * int(atacante[7]))))/int(atacante[2]))))
            print(f"    {atacante[0]} atacó a {atacado[0]}.")
            print(f"""    {atacante[0]} le ha propiciado {daño} puntos de daño a {atacado[0]}, dejando a {atacado[0]} con {max(0, int(atacado[3]) - daño)} de vida.
""")
            atacado[3] = max(0, int(atacado[3]) - daño)
            f.actualizar_encuentros(atacado)
            f.actualizar_vivos()
            if str(c.cargar_tributos(p.RUTA_TRIBUTOS)[1][0]) != atacado[0]:
                FIN = True
                with open(p.RUTA_TRIBUTOS, "a") as archivo:
                    archivo.write("0,0,0,99,0,0,0,0,0")  # se hace esto para evitar que se ejecute la funcion de victoria
        else:
            for i in range(num_encuentros):
                tributos_atacados = []
                atacante = self.tributos[randint(1, len(self.tributos) - 1)]
                for cada_tributo in self.tributos:
                    if cada_tributo[0] != atacante[0]:
                        tributos_atacados += [cada_tributo]
                    atacado = tributos_atacados[randint(0, len(tributos_atacados) - 1)]
                    daño = round(min(90, max(5, ((60 * int(atacante[6]) + (40 * int(atacante[5])) + (40 * int(atacante[7]))))/int(atacante[2]))))
                print(f"    {atacante[0]} atacó a {atacado[0]}.")
                print(f"""    {atacante[0]} le ha propiciado {daño} puntos de daño a {atacado[0]}, dejando a {atacado[0]} con {max(0, int(atacado[3]) - daño)} de vida.
""")
                atacado[3] = max(0, int(atacado[3]) - daño)
                jugador_antes = c.cargar_tributos(p.RUTA_TRIBUTOS)[1][0]
                f.actualizar_encuentros(atacado)
                f.actualizar_vivos()
                if c.cargar_tributos(p.RUTA_TRIBUTOS)[1][0] != jugador_antes:
                    FIN = True
        if FIN is True:
            print(f"¡OH NO! Su tributo, {self.jugador} ha muerto.")
            print("Redireccionando a Menú de Incio...")
            return False
        if FIN is False:
            f.mostrar_vivos_muertos()


class Objeto:

    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso

    def entregar_beneficio(self, tributo):  # tributo es instancia
        f.restar_objeto_mochila(tributo[0], self.nombre)
        if self.tipo == "consumible":
            tributo[4] = int(tributo[4]) + p.AUMENTAR_ENERGIA
            print(f"Su nueva energía es {tributo[4]}.")
        if self.tipo == "arma":
            Arena(tributo).setear_datos()
            tributo[6] = round(float(tributo[6]) * (float(p.PONDERADOR_AUMENTAR_FUERZA) * float(c.cargar_arenas(p.RUTA_ARENAS)[1][2]) + 1.0))
            print(f"Ahora su fuerza es {tributo[6]}.")
        if self.tipo == "especial":
            Arena(tributo).setear_datos()
            tributo[4] = int(tributo[4]) + p.AUMENTAR_ENERGIA
            tributo[6] = round(float(tributo[6]) * (float(p.PONDERADOR_AUMENTAR_FUERZA) * float(c.cargar_arenas(p.RUTA_ARENAS)[1][2])+ 1.0))
            tributo[5] = int(tributo[5]) + p.AUMENTAR_AGILIDAD
            tributo[7] = int(tributo[7]) + p.AUMENTAR_INGENIO
            print(f"¡Felicidades! Este objeto ha aumentado su energia ({tributo[4]}), su fuerza ({tributo[6]}), su agilidad ({tributo[5]}) y su ingenio ({tributo[7]}).")
        f.actualizar_self_lista([tributo[0], tributo[1], tributo[2], tributo[3], tributo[4], tributo[5], tributo[6], tributo[7], tributo[8]])


class ResumenSimulacion:

    def __init__(self, accion):
        self.accion = accion

    def __str__(self):
        print(f"""                       Resumen última hora
--------------------------------------------------------------
Última acción realizada: {self.accion}
""")


class ResumenGeneral(ABC):

    @abstractmethod
    def armar_resumen(self):
        f.actualizar_vivos()
        print(f"""                                Estado DCCapitolio
--------------------------------------------------------------------------------
Dificultad: {c.cargar_arenas(p.RUTA_ARENAS)[1][1]}
Ambiente actual: {c.cargar_ambientes(p.RUTA_AMBIENTES)[1][0]}
Tributos vivios:""")
        tributos = c.cargar_tributos(p.RUTA_TRIBUTOS)
        for tributo in tributos[1:]:
            print(f"     {tributo[0]}: {tributo[3]}")
        print(f"Próximo ambiente: {c.cargar_ambientes(p.RUTA_AMBIENTES)[2][0]}")

    def mostrar_resumen(self):
        print("")
        self.armar_resumen()
        return (" ")


class VerEstadoActual(Tributo):

    def notificar(self):
        super().notificar()
