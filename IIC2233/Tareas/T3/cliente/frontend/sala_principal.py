import json
from PyQt5.QtWidgets import QWidget, QLabel, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSignal

# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

RUTA_TARJETA = jsonObject["ruta_tarjeta"]


class SalaPrincipal(QWidget):

    reto_signal = pyqtSignal(str)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):

        self.setWindowTitle('Sala Principal')
        self.setGeometry(tamano_ventana)

        self.setWindowIcon(QIcon(RUTA_TARJETA))
        self.setStyleSheet("background-color: black")

        self.label_0 = QLabel("Jugadores que han aceptado el reto...", self)
        self.label_0.move(165, 80)
        self.label_0.setStyleSheet("border-radius: 5px;"
                                   "color: white")
        self.label_0.setFont(QFont('Blackadder ITC', 24))

        self.label_pregunta = QLabel('¿Quién ganará el premio mayor?:', self)
        self.label_pregunta.setGeometry(200, 500, 400, 30)
        self.label_pregunta.setStyleSheet("border-radius: 5px;"
                                          "color: white")
        self.label_pregunta.setFont(QFont('Arial', 16))

        self.premio = QLabel('₩ 45.600.000.000', self)
        self.premio.setGeometry(50, 530, 700, 150)
        self.premio.setStyleSheet("border-radius: 5px;"
                                  "color: white")
        self.premio.setFont(QFont('Arial', 50))

        self.logo2 = QLabel(self)
        pixeles2 = QPixmap(RUTA_TARJETA)
        self.logo2.setPixmap(pixeles2)
        self.logo2.setScaledContents(True)
        self.logo2.setMaximumSize(250, 150)
        self.logo2.move(280, 660)

        # Label jugadores
        self.jug_1 = QLabel("Esperando jugadores...", self)
        self.jug_1.setGeometry(200, 200, 390, 40)
        self.jug_1.setStyleSheet("border-radius: 2px;"
                                 "color: red")
        self.jug_1.setFont(QFont('Arial', 20))

        self.jug_2 = QLabel("Esperando jugadores...", self)
        self.jug_2.setGeometry(200, 250, 390, 40)
        self.jug_2.setStyleSheet("border-radius: 2px;"
                                 "color: red")
        self.jug_2.setFont(QFont('Arial', 20))

        self.jug_3 = QLabel("Esperando jugadores...", self)
        self.jug_3.setGeometry(200, 300, 390, 40)
        self.jug_3.setStyleSheet("border-radius: 2px;"
                                 "color: red")
        self.jug_3.setFont(QFont('Arial', 20))

        self.jug_4 = QLabel("Esperando jugadores...", self)
        self.jug_4.setGeometry(200, 350, 390, 40)
        self.jug_4.setStyleSheet("border-radius: 2px;"
                                 "color: red")
        self.jug_4.setFont(QFont('Arial', 20))

        # botones para retar permanecen ocultos al principio
        self.retar_1 = QPushButton('Retar', self)
        self.retar_1.setGeometry(550, 200, 60, 40)
        self.retar_1.setStyleSheet("background-color: black;"
                                   "border-radius: 2px;"
                                   "color: black")
        self.retar_1.clicked.connect(self.retar_jug1)

        self.retar_2 = QPushButton('Retar', self)
        self.retar_2.setGeometry(550, 250, 60, 40)
        self.retar_2.setStyleSheet("background-color: black;"
                                   "border-radius: 2px;"
                                   "color: black")
        self.retar_2.clicked.connect(self.retar_jug2)

        self.retar_3 = QPushButton('Retar', self)
        self.retar_3.setGeometry(550, 300, 60, 40)
        self.retar_3.setStyleSheet("background-color: black;"
                                   "border-radius: 2px;"
                                   "color: black")
        self.retar_3.clicked.connect(self.retar_jug3)           

        self.retar_4 = QPushButton('Retar', self)
        self.retar_4.setGeometry(550, 350, 60, 40)
        self.retar_4.setStyleSheet("background-color: black;"
                                   "border-radius: 2px;"
                                   "color: black")
        self.retar_4.clicked.connect(self.retar_jug4)

    def agregar_labels_retar(self, nombre):
        self.nombre = nombre  # se agrega para tener esta info
        if nombre == self.jug_1.text()[3:]:
            self.retar_1.move(1000, 1000)
            self.retar_2.setStyleSheet("background-color: white;")
            self.retar_2.setFont(QFont('Arial', 12))
            self.retar_3.setStyleSheet("background-color: white;")
            self.retar_3.setFont(QFont('Arial', 12))
            self.retar_4.setStyleSheet("background-color: white;")
            self.retar_4.setFont(QFont('Arial', 12))

        if nombre == self.jug_2.text()[3:]:
            self.retar_1.setStyleSheet("background-color: white;")
            self.retar_1.setFont(QFont('Arial', 12))
            self.retar_2.move(1000, 1000)
            self.retar_3.setStyleSheet("background-color: white;")
            self.retar_3.setFont(QFont('Arial', 12))
            self.retar_4.setStyleSheet("background-color: white;")
            self.retar_4.setFont(QFont('Arial', 12))

        if nombre == self.jug_3.text()[3:]:
            self.retar_1.setStyleSheet("background-color: white;")
            self.retar_1.setFont(QFont('Arial', 12))
            self.retar_2.setStyleSheet("background-color: white;")
            self.retar_2.setFont(QFont('Arial', 12))
            self.retar_3.move(1000, 1000)
            self.retar_4.setStyleSheet("background-color: white;")
            self.retar_4.setFont(QFont('Arial', 12))

        if nombre == self.jug_4.text()[3:]:
            self.retar_1.setStyleSheet("background-color: white;")
            self.retar_1.setFont(QFont('Arial', 12))
            self.retar_2.setStyleSheet("background-color: white;")
            self.retar_2.setFont(QFont('Arial', 12))
            self.retar_3.setStyleSheet("background-color: white;")
            self.retar_3.setFont(QFont('Arial', 12))
            self.retar_4.move(1000, 1000)

    def retar_jug1(self):
        print(f"{self.nombre} ha retado a {self.jug_1.text()[3:]}")
        self.reto_signal.emit(f"[RETO]{self.nombre}-{self.jug_1.text()[3:]}")
        self.esconder_botones_retar()

    def retar_jug2(self):
        print(f"{self.nombre} ha retado a {self.jug_2.text()[3:]}")
        self.reto_signal.emit(f"[RETO]{self.nombre}-{self.jug_2.text()[3:]}")
        self.esconder_botones_retar()

    def retar_jug3(self):
        print(f"{self.nombre} ha retado a {self.jug_3.text()[3:]}")
        self.reto_signal.emit(f"[RETO]{self.nombre}-{self.jug_3.text()[3:]}")
        self.esconder_botones_retar()

    def retar_jug4(self):
        print(f"{self.nombre} ha retado a {self.jug_4.text()[3:]}")
        self.reto_signal.emit(f"[RETO]{self.nombre}-{self.jug_4.text()[3:]}")
        self.esconder_botones_retar()

    def esconder_botones_retar(self):
        self.retar_1.hide()
        self.retar_2.hide()
        self.retar_3.hide()
        self.retar_4.hide()

    def mostrar_botones_retar(self):
        print("Has sido rechazado")
        self.retar_1.show()
        self.retar_2.show()
        self.retar_3.show()
        self.retar_4.show()
