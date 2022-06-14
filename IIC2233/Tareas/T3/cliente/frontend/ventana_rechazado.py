import json
from PyQt5.QtWidgets import QWidget, QLabel, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect

# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

RUTA_ICONO = jsonObject["ruta_icono"]


class VentanaRechazo(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui(QRect(740, 410, 300, 200))

    def init_gui(self, tamano_ventana):

        self.setWindowTitle('DCCALAMAR')
        self.setGeometry(tamano_ventana)

        self.setWindowIcon(QIcon(RUTA_ICONO))
        self.setStyleSheet("background-color: black")

        self.mensaje = QLabel('Tu invitación fue rechazada :(', self)
        self.mensaje.setGeometry(15, 60, 600, 30)
        self.mensaje.setStyleSheet("border-radius: 5px;"
                                   "color: white")
        self.mensaje.setFont(QFont('Daytona', 12))

        self.boton = QPushButton('cerrar', self)
        self.boton.setGeometry(120, 120, 60, 30)
        self.boton.setStyleSheet("background-color: red;"
                                 "border-radius: 4px;"
                                 "color: white")
        self.boton.setFont(QFont('Arial', 12))
        self.boton.clicked.connect(self.close)
