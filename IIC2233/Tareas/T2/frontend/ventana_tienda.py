from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton)
from PyQt5.QtWidgets import *
import parametros as p
import backend.funciones as f


class VentanaTienda(QWidget):

    senal_abrir_post_nivel = pyqtSignal()
    senal_sumar_vida = pyqtSignal()
    senal_skin = pyqtSignal()
    senal_insuficiente = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setGeometry(500, 100, 800, 800)

        self.setWindowTitle('Ventana Post Nivel')

        self.setStyleSheet("background-color: #33FF99")

        self.cerrada = False

        self.titulo = QLabel("TIENDA CROSSY FROG", self)
        self.titulo.move(100, 50)
        self.titulo.setStyleSheet("border-radius: 5px;"
                                        "color: black")
        self.titulo.setFont(QFont('Arial Rounded MT Bold', 30.5))

        self.skin1 = QLabel(self)
        pixeles_rojo = QPixmap(p.RUTA_RANA_ROJA)
        self.skin1.setPixmap(pixeles_rojo)
        self.skin1.setScaledContents(True)
        self.skin1.resize(100, 100)
        self.skin1.move(50, 650)

        self.skin2 = QLabel(self)
        pixeles_naranjo = QPixmap(p.RUTA_RANA_NARANJA)
        self.skin2.setPixmap(pixeles_naranjo)
        self.skin2.setScaledContents(True)
        self.skin2.resize(100, 100)
        self.skin2.move(50, 500)

        self.skin3 = QLabel(self)
        pixeles_verde = QPixmap(p.RUTA_RANA)
        self.skin3.setPixmap(pixeles_verde)
        self.skin3.setScaledContents(True)
        self.skin3.resize(100, 100)
        self.skin3.move(50, 350)

        self.corazon = QLabel(self)
        pixeles_corazon = QPixmap(p.RUTA_CORAZON)
        self.corazon.setPixmap(pixeles_corazon)
        self.corazon.setScaledContents(True)
        self.corazon.resize(100, 100)
        self.corazon.move(50, 200)

        self.precio1 = QLabel(f"$300", self)
        self.precio1.move(220, 690)
        self.precio1.setStyleSheet("border-radius: 5px;""color: black")
        self.precio1.setFont(QFont('Consolas', 14))
        self.precio2 = QLabel(f"$150", self)
        self.precio2.move(220, 540)
        self.precio2.setStyleSheet("border-radius: 5px;""color: black")
        self.precio2.setFont(QFont('Consolas', 14))
        self.precio3 = QLabel(f"$0", self)
        self.precio3.move(220, 390)
        self.precio3.setStyleSheet("border-radius: 5px;""color: black")
        self.precio3.setFont(QFont('Consolas', 14))
        self.precio4 = QLabel(f"$50", self)
        self.precio4.move(220, 240)
        self.precio4.setStyleSheet("border-radius: 5px;""color: black")
        self.precio4.setFont(QFont('Consolas', 14))

        self.comprar = QPushButton("Comprar", self)
        self.comprar.move(350, 235)
        self.comprar.setStyleSheet("background-color: white;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.comprar.setFont(QFont('Consolas', 14))
        self.comprar.resize(100, 30)
        self.comprar.clicked.connect(self.sumar_vida)

        self.comprar2 = QPushButton("Comprar", self)
        self.comprar2.move(350, 385)
        self.comprar2.setStyleSheet("background-color: white;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.comprar2.setFont(QFont('Consolas', 14))
        self.comprar2.resize(100, 30)
        self.comprar2.clicked.connect(self.comprar_verde)

        self.comprar3 = QPushButton("Comprar", self)
        self.comprar3.move(350, 535)
        self.comprar3.setStyleSheet("background-color: white;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.comprar3.setFont(QFont('Consolas', 14))
        self.comprar3.resize(100, 30)
        self.comprar3.clicked.connect(self.comprar_naranjo)

        self.comprar4 = QPushButton("Comprar", self)
        self.comprar4.move(350, 685)
        self.comprar4.setStyleSheet("background-color: white;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.comprar4.setFont(QFont('Consolas', 14))
        self.comprar4.resize(100, 30)
        self.comprar4.clicked.connect(self.comprar_rojo)

        self.volver = QPushButton("Volver", self)
        self.volver.move(650, 685)
        self.volver.setStyleSheet("background-color: white;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.volver.setFont(QFont('Consolas', 14))
        self.volver.resize(100, 30)
        self.volver.clicked.connect(self.cerrar)

    def mostrar(self):
        self.show()

    def cerrar(self):
        self.cerrada = True
        self.hide()
        self.senal_abrir_post_nivel.emit()

    def sumar_vida(self):
        if int(f.retorna_monedas()) >= 50:
            f.sumar_vida()
            self.senal_sumar_vida.emit()
        else:
            self.senal_insuficiente.emit()

    def comprar_naranjo(self):
        if int(f.retorna_monedas()) >= 150:
            self.senal_skin.emit()
            f.restar_cantidad_monedas(150)
            print("skin naranja comprada")
        else:
            self.senal_insuficiente.emit()

    def comprar_verde(self):
        if int(f.retorna_monedas()) >= 0:
            self.senal_skin.emit()
            f.restar_cantidad_monedas(150)
            print("skin verde comprada")
        else:
            self.senal_insuficiente.emit()

    def comprar_rojo(self):
        if int(f.retorna_monedas()) >= 300:
            self.senal_skin.emit()
            f.restar_cantidad_monedas(300)
            print("skin roja comprada")
        else:
            self.senal_insuficiente.emit()
