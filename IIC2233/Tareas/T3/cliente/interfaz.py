from PyQt5.QtCore import pyqtSignal, QObject, QRect
from frontend.ventana_inicio import VentanaInicio
from frontend.sala_principal import SalaPrincipal
from frontend.ventana_invitacion import VentanaInvitacion
from frontend.ventana_rechazado import VentanaRechazo
from frontend.sala_juego import SalaJuego


class Controlador(QObject):

    mostrar_ventana_principal_signal = pyqtSignal()
    mostrar_ventana_reto_signal = pyqtSignal(str)
    mostrar_rechazo_signal = pyqtSignal()
    mostrar_sala_juego_signal = pyqtSignal(str)
    enviar_usuario_signal = pyqtSignal(str)
    crear_retos_signal = pyqtSignal(str)
    ofrecer_reto_signal = pyqtSignal(str)
    enviar_info_juego_cliente_signal = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()

        tamano_ventana = QRect(600, 150, 800, 800)
        self.ventana_inicio = VentanaInicio(tamano_ventana)
        self.sala_principal = SalaPrincipal(tamano_ventana)
        self.ventana_invitacion = VentanaInvitacion(QRect(200, 250, 800, 550))
        self.ventana_rechazo = VentanaRechazo()
        self.sala_juego = SalaJuego(QRect(250, 250, 900, 600))

        # Conectar señales
        self.ventana_inicio.senal_nombre_usuario.connect(parent.recibir_mensaje)
        self.mostrar_ventana_principal_signal.connect(self.abrir_sala_principal)
        self.crear_retos_signal.connect(self.agregar_retar_sala_principal)
        self.sala_principal.reto_signal.connect(self.enviar_info_reto_cliente)
        self.mostrar_ventana_reto_signal.connect(self.abrir_ventana_reto)
        self.ventana_invitacion.respuesta_reto_signal.connect(self.enviar_info_reto_cliente)
        self.ventana_invitacion.respuesta_reto_signal.connect(self.sala_principal.show)
        self.mostrar_rechazo_signal.connect(self.ventana_rechazo.show)
        self.mostrar_sala_juego_signal.connect(self.abrir_sala_juego)
        self.sala_juego.mensaje_juego_signal.connect(self.enviar_info_juego)

    def mostrar_login(self):
        self.ventana_inicio.show()

    def label_usuario(self):
        self.ventana_inicio.edit_usuario.setText("")
        self.ventana_inicio.edit_usuario.setPlaceholderText("Nombre de usuario ya registrado")

    def abrir_sala_principal(self):
        self.sala_principal.show()
        self.ventana_inicio.close()

    def agregar_retar_sala_principal(self, nombre):
        self.sala_principal.agregar_labels_retar(nombre)

    def enviar_info_reto_cliente(self, info):
        info = info + "-" + str(self.sala_principal.nombre)
        self.ofrecer_reto_signal.emit(info + "")

    def abrir_ventana_reto(self, retador):
        self.sala_principal.hide()
        self.ventana_invitacion.subtitulo.setText(f"{retador[1:]} te ha invitado a jugar")
        self.ventana_invitacion.retador = str(retador)
        self.ventana_invitacion.show()

    def mostrar_rechazo_invitacion(self):
        self.sala_principal.show()
        self.mostrar_rechazo_signal.emit()
        self.ventana_invitacion.close()
        self.sala_principal.mostrar_botones_retar()

    def aceptar_invtiacion(self, info):
        self.mostrar_sala_juego_signal.emit(info)

    def abrir_sala_juego(self, info):
        self.sala_juego.show()
        self.sala_principal.hide()
        jug1 = info.split("-")[0]
        jug2 = info.split("-")[1]
        print(f"{jug1} jugará contra {jug2}")
        self.sala_juego.nombre_jug_1.setText(f"Jugador 1: {jug1}")
        self.sala_juego.nombre_jug_2.setText(f"Jugador 2: {jug2}")
        if jug1 == self.sala_principal.nombre:
            self.sala_juego.spinbox2.hide()
            self.sala_juego.label_impar_jug_2.hide()
            self.sala_juego.label_par_jug_2.hide()
            self.sala_juego.par_jug_2.hide()
            self.sala_juego.impar_jug_2.hide()
            self.sala_juego.boton_listo_jug_2.hide()
            self.sala_juego.label_espera_3.show()
            self.sala_juego.label_espera_4.show()
            self.sala_juego.reloj_jug_2.show()
            self.sala_juego.esperando_reloj_jug_2.show()
            self.sala_juego.pregunta_jug_2_1.setText("¿Cual ha de ser su apuesta?")
            self.sala_juego.pregunta_jug_2_2.setText("El valor de tu apuesta es")

        if jug2 == self.sala_principal.nombre:
            self.sala_juego.spinbox1.hide()
            self.sala_juego.label_impar_jug_1.hide()
            self.sala_juego.label_par_jug_1.hide()
            self.sala_juego.par_jug_1.hide()
            self.sala_juego.impar_jug_1.hide()
            self.sala_juego.boton_listo_jug_1.hide()
            self.sala_juego.label_espera_1.show()
            self.sala_juego.label_espera_2.show()
            self.sala_juego.reloj_jug_1.show()
            self.sala_juego.esperando_reloj_jug_1.show()
            self.sala_juego.pregunta_jug_1_1.setText("¿Cual ha de ser su apuesta?")
            self.sala_juego.pregunta_jug_1_2.setText("El valor de tu apuesta es")

    def enviar_info_juego(self, info):
        self.enviar_info_juego_cliente_signal.emit(info)
