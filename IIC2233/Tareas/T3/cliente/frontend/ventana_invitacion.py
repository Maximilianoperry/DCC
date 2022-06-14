import json
from PyQt5.QtWidgets import QWidget, QLabel, QWidget, QLabel, QPushButton, QApplication
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSignal, QRect

# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

RUTA_TARJETA = jsonObject["ruta_tarjeta"]
RUTA_LOGO_BLANCO = jsonObject["ruta_logo_blanco"]
RUTA_ICONO = jsonObject["ruta_icono"]


class VentanaInvitacion(QWidget):

    respuesta_reto_signal = pyqtSignal(str)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):

        self.setWindowTitle('Invitación')
        self.setGeometry(tamano_ventana)

        self.setWindowIcon(QIcon(RUTA_TARJETA))
        self.setStyleSheet("background-color: black")

        self.retador = ""

        self.subtitulo = QLabel('retador te ha invitado a jugar', self)
        self.subtitulo.setGeometry(225, 30, 600, 30)
        self.subtitulo.setStyleSheet("border-radius: 5px;"
                                     "color: white")
        self.subtitulo.setFont(QFont('Daytona', 16))

        self.logo = QLabel(self)
        pixeles = QPixmap(RUTA_LOGO_BLANCO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMaximumSize(710, 180)
        self.logo.move(50, 100)

        self.pregunta = QLabel('¿Aceptas el reto?', self)
        self.pregunta.setGeometry(300, 280, 400, 50)
        self.pregunta.setStyleSheet("border-radius: 5px;"
                                    "color: white")
        self.pregunta.setFont(QFont('Daytona', 16))

        self.aceptar = QPushButton('Aceptar', self)
        self.aceptar.setGeometry(275, 340, 120, 30)
        self.aceptar.setStyleSheet("background-color: white;"
                                   "border-radius: 2px;"
                                   "color: black")
        self.aceptar.setFont(QFont('Arial', 12))
        self.aceptar.clicked.connect(self.opcion_aceptar)

        self.rechazar = QPushButton('Rechazar', self)
        self.rechazar.setGeometry(415, 340, 120, 30)
        self.rechazar.setStyleSheet("background-color: white;"
                                    "border-radius: 2px;"
                                    "color: black")
        self.rechazar.setFont(QFont('Arial', 12))
        self.rechazar.clicked.connect(self.opcion_rechazar)

        self.tarjeta = QLabel(self)
        pixeles_tarjeta = QPixmap(RUTA_ICONO)
        self.tarjeta.setPixmap(pixeles_tarjeta)
        self.tarjeta.setScaledContents(True)
        self.tarjeta.setMaximumSize(200, 80)
        self.tarjeta.move(310, 400)

    def opcion_rechazar(self):
        self.close()
        msg_rechazo = "[RRETO]RECHAZADO-" + str(self.retador[1:])
        self.respuesta_reto_signal.emit(msg_rechazo)

    def opcion_aceptar(self):
        self.close()
        msg_aceptar = "[RACEP]ACEPTADO-" + str(self.retador[1:])
        self.respuesta_reto_signal.emit(msg_aceptar)
