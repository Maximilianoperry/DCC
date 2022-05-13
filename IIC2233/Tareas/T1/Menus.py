import cargar_datos as c
import parametros as p
import funciones as f
import Clases as cl


class MenuDeInicio:
    def __init__(self):
        self.iniciar_partida = "[1] Iniciar partida"
        self.salir = "[2] Salir"
        self.tributo = " "

    def __str__(self):
        print(f"""*** Menú de Inicio ***
----------------------
{self.iniciar_partida}
{self.salir}
""")
        f.reiniciar_datos()
        respuesta_menu_inicio = input("Ingrese una opción: ")
        if respuesta_menu_inicio == "1":
            print(" ")
            opciones = f.mostrar_opciones()
            while opciones is False:
                opciones = f.mostrar_opciones()
            self.tributo = c.cargar_tributos(p.RUTA_TRIBUTOS)[1]
            print(f"Escogió a {self.tributo[0]} como tributo.")
            f.seleccionar_arena()
            print("¡QUE COMIENCE EL DCCAPITOLIO!")
            f.crear_archivo_participantes()
            return MenuPrincipal().opciones_menu_principal()

        elif respuesta_menu_inicio == 2 or respuesta_menu_inicio == "2":
            return "Ha salido con éxito."

        else:
            print("Respuesta inválida.")
            return MenuDeInicio().__str__()


class MenuPrincipal(MenuDeInicio, cl.ResumenGeneral):
    def __init__(self):
        MenuDeInicio().__init__()
        self.simulacion_hora = "[1] Simulación hora"
        self.mostrar_estado = "[2] Mostrar estado del tributo"
        self.utilizar_objeto = "[3] Utilizar objeto"
        self.resumen = "[4] Resumen DCCapitolio"
        self.volver = "[5] Volver"
        self.salir = "[6] Salir"
        self.tributo = c.cargar_tributos(p.RUTA_TRIBUTOS)[1]
        self.nombre = self.tributo[0]
        self.instancia = cl.Tributo(self.tributo)

    def opciones_menu_principal(self):
        print(f"""
*** Menú Principal ***
----------------------
{self.simulacion_hora}
{self.mostrar_estado}
{self.utilizar_objeto}
{self.resumen}
{self.volver}
{self.salir}
""")
        respuesta_menu_principal = input("Ingrese una opción: ")
        if respuesta_menu_principal == "1":
            return MenuSimularUnaHora().opciones_simular_hora()
        if respuesta_menu_principal == "2":
            return LlamadoVerEstadoActual().ver_estado()
        if respuesta_menu_principal == "3":
            lista_mochila = f.retorna_mochila(self.nombre).split(",")
            if f.retorna_peso(self.nombre) == 0:
                print("No posee objetos en la mochila.")
                return self.opciones_menu_principal()
            else:
                objeto = f.utilizar_objeto(lista_mochila)
                datos = c.cargar_objetos(p.RUTA_OBJETOS)
                for dato in datos:
                    if dato[0] == objeto:
                        tipo = dato[1]
                        peso = dato[2]
                instancia_objeto = cl.Objeto(objeto, tipo, peso)
                instancia_objeto.entregar_beneficio(self.tributo)
                return self.opciones_menu_principal()
        if respuesta_menu_principal == "4":
            print(MenuPrincipal().mostrar_resumen())
            return self.opciones_menu_principal()
        if respuesta_menu_principal == "5":
            return MenuDeInicio().__str__()
        if respuesta_menu_principal == "6":
            return "Ha saido con éxito."
        else:
            print("Respuesta inválida.")
            return self.opciones_menu_principal()

    def armar_resumen(self):
        print(" ")
        super().armar_resumen()
        return " "


class MenuSimularUnaHora(MenuPrincipal):
    def __init__(self):
        super().__init__()
        self.accion_heroica = "[1] Acción heroica"
        self.atacar_atributo = "[2] Atacar a un atributo"
        self.pedir_objeto_patrocinadores = "[3] Pedir objeto a patrocinadores"
        self.bolita = "[4] Hacerse bolita"

    def opciones_simular_hora(self):
        print(f"""*** Simulación de hora ***
--------------------------
{self.accion_heroica}
{self.atacar_atributo}
{self.pedir_objeto_patrocinadores}
{self.bolita}
{self.volver}
{self.salir}
""")
        respuesta = input("Seleccione una opción: ")
        if respuesta == "1":
            if self.instancia.energia < p.ENERGIA_ACCION_HEROICA:
                print("No dispone de suficiente energía para realizar una acción heroica.")
                return self.opciones_simular_hora()
            else:
                self.instancia.accion_heroica()
                cl.ResumenSimulacion("accion heroica").__str__()
        if respuesta == "2":
            if self.instancia.energia < p.ENERGIA_ATACAR:
                print("Energía insufciente.")
                return self.opciones_menu_principal()
            else:
                self.instancia.atacar_tributo()
                cl.ResumenSimulacion("atacar tributo").__str__()
        if respuesta == "3":
            self.instancia.pedir_objeto_a_patrocinadores()
            cl.ResumenSimulacion("pedir objeto a patrocinadores").__str__()
        if respuesta == "4":
            self.instancia.hacerse_bolita()
            cl.ResumenSimulacion("hacerse bolita (¡wow!)").__str__()
        if respuesta == "5":
            return MenuPrincipal().opciones_menu_principal()
        if respuesta == "6":
            return "Ha salido con éxito."
        if respuesta.isdigit() is False:
            print("Respuesta inválida")
            return MenuSimularUnaHora().opciones_simular_hora()
        if respuesta.isdigit() is True:
            if int(respuesta) not in range(1, 7):
                print("Respuesta inválida")
                return MenuSimularUnaHora().opciones_simular_hora()
        if cl.Arena(self.tributo).ejecutar_evento() is False or cl.Arena(self.tributo).encuentros() is False:
            return MenuDeInicio().__str__()
        if len(c.cargar_tributos(p.RUTA_TRIBUTOS)) == 2:
            print("""

!!!!!FELICIDADES¡¡¡¡¡
HAS GANADO EL DCCAPITOLIO


 """)
            return MenuDeInicio().__str__()
        else:
            cl.Ambiente().rotar_ambientes()
            MenuPrincipal().opciones_menu_principal()


class LlamadoVerEstadoActual(MenuPrincipal):
    def __init__(self):
        super().__init__()
        self.instancia = cl.VerEstadoActual(self.tributo)

    def ver_estado(self):
        self.instancia.ver_estado_actual()
        return MenuPrincipal().opciones_menu_principal()
