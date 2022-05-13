from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton)
from PyQt5.QtWidgets import *
import os
import sys
import parametros as p


class VentanaRanking(QWidget):

    senal_abrir_ranking = pyqtSignal()
    senal_cerrar_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setGeometry(550, 300, 800, 600)

        self.setWindowTitle('Ventana de Ranking')

        self.setStyleSheet("background-color: #33FF99")

        # Lectura de archivo .txt
        tabla = []
        if os.path.isfile("puntajes.txt") == True:
            with open("puntajes.txt", "r") as archivo:
                file = archivo.readlines()
                for dato in file:
                    dato = dato[:len(dato) - 1]
                    dato = str(dato).split(",")
                    tabla += [dato]
            if len(tabla) >= 5:
                tabla = sorted(tabla, key=lambda x: int(x[1]), reverse=True)
                tabla = tabla[:5]
        else:
            archivo = open("puntajes.txt", "w")
            archivo.close()

        # Fin lectura de archivo .txt
        self.titulo = QLabel("RANKING DE PUNTAJES", self)
        self.titulo.move(120, 120)
        self.titulo.setStyleSheet("border-radius: 5px;"
                                        "color: black")
        self.titulo.setFont(QFont('ALGERIAN', 30.5))

        if len(tabla) == 5:

            self.primero = QLabel(f"1.  {str(tabla[0][0])}", self)
            self.primero.move(120, 230)
            self.primero_ranking = QLabel(f"{str(tabla[0][1])} puntos", self)
            self.primero_ranking.move(540, 230)

            self.primero.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.primero.setFont(QFont('Consolas', 12))
            self.primero_ranking.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.primero_ranking.setFont(QFont('Consolas', 12))

            self.segundo = QLabel(f"2.  {str(tabla[1][0])}", self)
            self.segundo.move(120, 270)
            self.segundo_ranking = QLabel(f"{str(tabla[1][1])} puntos", self)
            self.segundo_ranking.move(540, 270)
            self.segundo.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.segundo.setFont(QFont('Consolas', 12))
            self.segundo_ranking.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.segundo_ranking.setFont(QFont('Consolas', 12))

            self.tercero = QLabel(f"3.  {str(tabla[2][0])}", self)
            self.tercero.move(120, 310)
            self.tercero_ranking = QLabel(f"{str(tabla[2][1])} puntos", self)
            self.tercero_ranking.move(540, 310)
            self.tercero.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.tercero.setFont(QFont('Consolas', 12))
            self.tercero_ranking.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.tercero_ranking.setFont(QFont('Consolas', 12))

            self.cuarto = QLabel(f"4.  {str(tabla[3][0])}", self)
            self.cuarto.move(120, 350)
            self.cuarto_ranking = QLabel(f"{str(tabla[3][1])} puntos", self)
            self.cuarto_ranking.move(540, 350)
            self.cuarto.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.cuarto.setFont(QFont('Consolas', 12))
            self.cuarto_ranking.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.cuarto_ranking.setFont(QFont('Consolas', 12))

            self.quinto = QLabel(f"5.  {str(tabla[4][0])}", self)
            self.quinto.move(120, 390)
            self.quinto_ranking = QLabel(f"{str(tabla[4][1])} puntos", self)
            self.quinto_ranking.move(540, 390)
            self.quinto.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.quinto.setFont(QFont('Consolas', 12))
            self.quinto_ranking.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.quinto_ranking.setFont(QFont('Consolas', 12))

        else:
            self.error = QLabel("""No han participado suficientes usuarios para tener un ranking
              (mínimo 5 usuarios distintos)
""", self)
            self.error.move(70, 250)
            self.error.setStyleSheet("border-radius: 5px;"
                                            "color: black")
            self.error.setFont(QFont('Consolas', 12))

        self.volver_button = QPushButton('Volver', self)
        self.volver_button.setGeometry(360, 450, 80, 23)
        self.volver_button.setStyleSheet("background-color: #FFFFFF;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.volver_button.setFont(QFont('Calibri', 12))
        self.volver_button.clicked.connect(self.volver)
        self.senal_cerrar_ranking.connect(self.show)

    def mostrar_ranking(self):
        self.show()
        self.senal_abrir_ranking.emit()

    def volver(self):
        self.senal_cerrar_ranking.emit()
        self.ocultar()

    def ocultar(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaRanking()
    ventana.show()
    sys.exit(app.exec_())
