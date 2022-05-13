from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton)
from PyQt5.QtWidgets import *
import sys
import parametros as p
import backend.funciones as f


class VentanaPostNivel(QWidget):

    senal_abrir_post_nivel = pyqtSignal()
    senal_abrir_juego = pyqtSignal()
    senal_cerrar_juego = pyqtSignal()
    senal_abrir_tienda = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setGeometry(350, 100, 1200, 900)

        self.setWindowTitle('Ventana Post Nivel')

        self.setStyleSheet("background-color: #C0C0C0")

        self.titulo = QLabel("RESUMEN DE NIVEL", self)
        self.titulo.move(330, 120)
        self.titulo.setStyleSheet("border-radius: 5px;"
                                        "color: black")
        self.titulo.setFont(QFont('Arial Rounded MT Bold', 30.5))

    def abrir_ventana_post_nivel(self):
        self.senal_abrir_post_nivel.emit()
        self.label_nivel = QLabel(f"nivel:  ", self)
        self.label_nivel.setGeometry(270, 200, 500, 100)
        self.label_nivel.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_nivel.setFont(QFont('Aldhabi', 15))
        self.label_nivel_num = QLabel(str(int(f.retorna_nivel()) - 1), self)
        self.label_nivel_num.setGeometry(870, 200, 500, 100)
        self.label_nivel_num.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_nivel_num.setFont(QFont('Aldhabi', 15))

        self.label_vidas = QLabel(f"vidas:   ", self)
        self.label_vidas.setGeometry(270, 300, 500, 100)
        self.label_vidas.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_vidas.setFont(QFont('Aldhabi', 15))
        self.label_vidas_num = QLabel(f"{f.retorna_vidas()}", self)
        self.label_vidas_num.setGeometry(870, 300, 500, 100)
        self.label_vidas_num.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_vidas_num.setFont(QFont('Aldhabi', 15))

        self.label_monedas = QLabel(f"monedas:   ", self)
        self.label_monedas.setGeometry(270, 400, 500, 100)
        self.label_monedas.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_monedas.setFont(QFont('Aldhabi', 15))
        self.label_monedas_num = QLabel(f"{f.retorna_monedas()}", self)
        self.label_monedas_num.setGeometry(870, 400, 500, 100)
        self.label_monedas_num.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_monedas_num.setFont(QFont('Aldhabi', 15))

        self.label_puntaje = QLabel(f"puntaje esta ronda:   ", self)
        self.label_puntaje.setGeometry(270, 500, 500, 100)
        self.label_puntaje.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_puntaje.setFont(QFont('Aldhabi', 15))
        self.label_puntaje_num = QLabel(f"{int(f.retorna_puntaje_ronda())}", self)
        self.label_puntaje_num.setGeometry(870, 500, 500, 100)
        self.label_puntaje_num.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_puntaje_num.setFont(QFont('Aldhabi', 15))

        self.label_puntaje_total = QLabel(f"puntaje total:   ", self)
        self.label_puntaje_total.setGeometry(270, 600, 500, 100)
        self.label_puntaje_total.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_puntaje_total.setFont(QFont('Aldhabi', 15))
        self.label_puntaje_total_num = QLabel(f"{f.retorna_puntaje_total()}", self)
        self.label_puntaje_total_num.setGeometry(870, 600, 500, 100)
        self.label_puntaje_total_num.setStyleSheet("border-radius: 5px;"
                                            "color: black")
        self.label_puntaje_total_num.setFont(QFont('Aldhabi', 15))

        self.tiempo_actual = f.retorna_tiempo()

        self.label_jugar = QPushButton("Puedes seguir con el siguiente nivel!", self)
        self.label_jugar.setGeometry(312, 700, 550, 100)
        self.label_jugar.setStyleSheet("background-color: #009900;"
                                            "border-radius: 5px;"
                                            "color: black")
        self.label_jugar.setFont(QFont('Aldhabi', 20))

        if int(f.retorna_vidas()) == 0 or int(self.tiempo_actual) <= 0:
            self.label_jugar.setText("No puedes seguir jugando, lamentable...")
            self.label_jugar.setGeometry(287, 700, 600, 100)
            self.label_jugar.setStyleSheet("background-color: #cc6600;"
                                            "border-radius: 5px;"
                                            "color: black")

            puntaje_nivel = f.retorna_puntaje_ronda_perder()
            f.registrar_puntaje_ronda(puntaje_nivel)
            f.registrar_puntaje_total(puntaje_nivel)
            f.registrar_puntaje_jugador(str(f.retorna_usuario()), str(f.retorna_puntaje_total()))

            self.label_nivel_num.setText(str(f.retorna_nivel()))
            self.label_puntaje_num.setText(f"{int(f.retorna_puntaje_ronda_perder())}")
            self.label_puntaje_total_num.setText(f"{f.retorna_puntaje_total()}")

            self.boton_sig_nivel = QLabel("    Siguiente nivel!", self)
            self.boton_sig_nivel.setGeometry(495, 830, 180, 30)
            self.boton_sig_nivel.setStyleSheet("background-color: #A0A0A0;"
                                            "border-radius: 5px;"
                                            "color: #C0C0C0")
            self.boton_sig_nivel.setFont(QFont('Aldhabi', 12))

            self.boton_tienda = QLabel("     Ir a la Tienda", self)
            self.boton_tienda.setGeometry(270, 830, 180, 30)
            self.boton_tienda.setStyleSheet("background-color: #A0A0A0;"
                                            "border-radius: 5px;"
                                            "color: #C0C0C0")
            self.boton_tienda.setFont(QFont('Aldhabi', 12))

        else:
            self.boton_sig_nivel = QPushButton("  Siguiente nivel!", self)
            self.boton_sig_nivel.setGeometry(495, 830, 180, 30)
            self.boton_sig_nivel.setStyleSheet("background-color: #FFFFFF;"
                                            "border-radius: 5px;"
                                            "color: black")
            self.boton_sig_nivel.setFont(QFont('Aldhabi', 12))
            self.boton_sig_nivel.clicked.connect(self.empezar_juego_nuevo)

            self.boton_tienda = QPushButton("  Ir a la Tienda", self)
            self.boton_tienda.setGeometry(270, 830, 180, 30)
            self.boton_tienda.setStyleSheet("background-color: #FFFFFF;"
                                            "border-radius: 5px;"
                                            "color: black")
            self.boton_tienda.setFont(QFont('Aldhabi', 12))
            self.boton_tienda.clicked.connect(self.ir_a_tienda)

        self.salir = QPushButton(" Salir", self)
        self.salir.setGeometry(720, 830, 180, 30)
        self.salir.setStyleSheet("background-color: #FFFFFF;"
                                            "border-radius: 5px;"
                                            "color: black")
        self.salir.setFont(QFont('Aldhabi', 12))
        self.salir.clicked.connect(self.cerrar_juego)

        self.show()

    def empezar_juego_nuevo(self):
        self.senal_abrir_juego.emit()
        f.actualiza_duracion_ronda()
        self.hide()

    def cerrar_juego(self):
        f.registrar_puntaje_jugador(str(f.retorna_usuario()), str(f.retorna_puntaje_total()))
        self.senal_cerrar_juego.emit()
        self.close()

    def ir_a_tienda(self):
        self.hide()
        self.senal_abrir_tienda.emit()
