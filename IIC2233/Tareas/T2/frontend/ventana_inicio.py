from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)
from PyQt5.QtCore import QRect
from PyQt5 import QtCore, QtMultimedia  # Bonus Música
import backend.funciones as f
import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_abrir_ranking = pyqtSignal()
    senal_cerrar_ranking = pyqtSignal()
    senal_abrir_juego = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.musica = Musica(p.RUTA_CANCION)  # Bonus musica
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):

        self.logo = QLabel(self)
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMaximumSize(300, 300)
        self.logo.move(250, 50)
        self.setWindowTitle('Ventana Inicio')
        self.setGeometry(tamano_ventana)
        self.label_usuario = QLabel('Escribe tu nombre de usuario: ', self)
        self.label_usuario.move(300, 350)
        self.usuario_form = QLineEdit('', self)
        self.usuario_form.setGeometry(250, 370, 280, 23)

        self.iniciar_button = QPushButton('Iniciar partida', self)
        self.iniciar_button.setGeometry(345, 420, 100, 23)
        self.iniciar_button.clicked.connect(self.enviar_login)

        self.ver_ranking = QPushButton('Ver ranking', self)
        self.ver_ranking.setGeometry(345, 450, 100, 23)
        self.ver_ranking.clicked.connect(self.abrir_ranking)

        self.agregar_estilo()

    def enviar_login(self):
        self.senal_enviar_login.emit(self.usuario_form.text())
        f.guardar_jugador(self.usuario_form.text())

    def abrir_ranking(self):
        self.senal_abrir_ranking.emit()
        self.ocultar()

    def agregar_estilo(self):
        self.setStyleSheet("background-color: #33FF99")
        self.usuario_form.setStyleSheet("background-color: #000000;"
                                        "border-radius: 5px;"
                                        "color: white")
        self.iniciar_button.setStyleSheet("background-color: #000000;"
                                      "border-radius: 5px;"
                                      "color: white")
        self.ver_ranking.setStyleSheet("background-color: #000000;"
                                      "border-radius: 5px;"
                                      "color: white")

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.senal_abrir_juego.emit()
            self.ocultar()

        else:
            self.usuario_form.setText("")
            self.usuario_form.setPlaceholderText(f"Ingrese un usuario de {p.MIN_CARACTERES + 1} a {p.MAX_CARACTERES} caracteres! (sin "","")")

    def start(self):  # Bonus musica
        self.musica.comenzar()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()


class Musica(QObject):  # Bonus musica

    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion

    def comenzar(self):
        try:
            self.cancion = QtMultimedia.QSound(self.ruta_cancion)
            self.cancion.Loop()
            self.cancion.play()
        except Exception as error:
            print('No se pudo iniciar la cancion', error)

    def pausar(self):
        self.cancion.stop()
