import json
import funciones as f
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import *


# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

RUTA_LOGO_BLANCO = jsonObject["ruta_logo_blanco"]
RUTA_ICONO = jsonObject["ruta_icono"]


class VentanaInicio(QWidget):

    senal_nombre_usuario = pyqtSignal(str)
    senal_fecha = pyqtSignal(str)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):

        self.setWindowTitle('Ventana Inicio')
        self.setGeometry(tamano_ventana)

        self.setWindowIcon(QIcon(RUTA_ICONO))
        self.setStyleSheet("background-color: black")

        self.pregunta = QLabel("", self)
        self.pregunta.move(30, 80)
        self.pregunta.setStyleSheet("border-radius: 5px;"
                                    "color: white")
        self.pregunta.setFont(QFont('Blackadder ITC', 24))

        self.logo = QLabel(self)
        pixeles = QPixmap(RUTA_LOGO_BLANCO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMaximumSize(450, 150)
        self.logo.move(180, 200)

        self.label_usuario = QLabel('Escribe tu nombre de usuario (alfanumérico):', self)
        self.label_usuario.setGeometry(200, 360, 400, 15)
        self.label_usuario.setStyleSheet("border-radius: 5px;"
                                         "color: white")
        self.label_usuario.setFont(QFont('Arial', 12))

        self.edit_usuario = QLineEdit('', self)
        self.edit_usuario.setGeometry(200, 385, 390, 30)
        self.edit_usuario.setStyleSheet("background-color: white;"
                                        "border-radius: 2px;"
                                        "color: black")
        self.edit_usuario.setFont(QFont('Arial', 12))

        self.label_nacimiento = QLabel('Fecha de nacimiento (dd/mm/yyyy):', self)
        self.label_nacimiento.setGeometry(200, 450, 400, 25)
        self.label_nacimiento.setStyleSheet("border-radius: 5px;"
                                            "color: white")
        self.label_nacimiento.setFont(QFont('Arial', 12))

        self.edit_nacimiento = QLineEdit('', self)
        self.edit_nacimiento.setGeometry(200, 475, 390, 30)
        self.edit_nacimiento.setStyleSheet("background-color: white;"
                                           "border-radius: 2px;"
                                           "color: black")
        self.edit_nacimiento.setFont(QFont('Arial', 12))

        self.firmar = QPushButton('Firmar', self)
        self.firmar.setGeometry(350, 570, 100, 40)
        self.firmar.setStyleSheet("background-color: white;"
                                  "border-radius: 2px;"
                                  "color: black")
        self.firmar.setFont(QFont('Arial', 12))
        self.firmar.clicked.connect(self.firma_realizada)

        self.logo2 = QLabel(self)
        pixeles2 = QPixmap(RUTA_ICONO)
        self.logo2.setPixmap(pixeles2)
        self.logo2.setScaledContents(True)
        self.logo2.setMaximumSize(250, 150)
        self.logo2.move(280, 660)

    def firma_realizada(self):
        if len(str(self.edit_usuario.text())) < 1:
            self.edit_usuario.setText("")
            self.edit_usuario.setPlaceholderText("Ingrese un nombre de usuario")
        elif str(self.edit_usuario.text()).isalnum() is False:
            self.edit_usuario.setText("")
            self.edit_usuario.setPlaceholderText("Ingrese un nombre de usuario alfanumérico")
        elif str(self.edit_nacimiento.text()) == "":
            self.edit_nacimiento.setText("")
            self.edit_nacimiento.setPlaceholderText("Fecha inválida")
        elif str(self.edit_nacimiento.text())[0] == "[":
            self.edit_nacimiento.setText("")
            self.edit_nacimiento.setPlaceholderText("Fecha inválida")
        elif f.revisar_fecha(str(self.edit_nacimiento.text())) is False:
            self.edit_nacimiento.setText("")
            self.edit_nacimiento.setPlaceholderText("Fecha inválida")
        else:
            print("Firma realizada")
            self.senal_nombre_usuario.emit("[USUARIO]" + self.edit_usuario.text())
            self.senal_fecha.emit("[FECHA]" + self.edit_nacimiento.text())

    def cerrar(self):
        self.close()