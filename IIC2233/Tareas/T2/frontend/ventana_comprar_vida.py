from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton)
from PyQt5.QtWidgets import *
import parametros as p
import backend.funciones as f


class VentanaComprarVida(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(650, 500, 300, 100)

        self.setWindowTitle('Pop-up')

        self.setStyleSheet("background-color: #33FF99")

        self.titulo = QLabel("Haz comprado una vida", self)

        self.titulo.setFont(QFont('Aldhabi', 12))

        self.titulo.move(30, 45)


class VentanaSkin(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(650, 500, 300, 100)

        self.setWindowTitle('Pop-up')

        self.setStyleSheet("background-color: #33FF99")

        self.titulo = QLabel("Haz un comprado un skin", self)

        self.titulo.setFont(QFont('Aldhabi', 12))

        self.titulo.move(30, 45)


class VentanaNoMonedas(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(650, 500, 300, 100)

        self.setWindowTitle('Pop-up')

        self.setStyleSheet("background-color: #33FF99")

        self.titulo = QLabel("Monedas insufcientes", self)

        self.titulo.setFont(QFont('Aldhabi', 12))

        self.titulo.move(30, 45)
