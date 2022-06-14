import json
from random import randint
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QSpinBox, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import pyqtSignal, QRect

# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

RUTA_TARJETA = jsonObject["ruta_tarjeta"]
RUTA_LOGO_BLANCO = jsonObject["ruta_logo_blanco"]
RUTA_ICONO = jsonObject["ruta_icono"]
RUTA_AVATAR_1 = jsonObject["ruta_avatar_1"]
RUTA_AVATAR_2 = jsonObject["ruta_avatar_2"]
RUTA_CANICA_1 = jsonObject["ruta_canica_1"]
RUTA_CANICA_2 = jsonObject["ruta_canica_2"]
RUTA_RELOJ = jsonObject["ruta_reloj"]


class SalaJuego(QWidget):

    respuesta_reto_signal = pyqtSignal(str)
    mensaje_juego_signal = pyqtSignal(str)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):

        self.setWindowTitle('Sala juego')
        self.setGeometry(tamano_ventana)

        self.setWindowIcon(QIcon(RUTA_TARJETA))
        self.setStyleSheet("background-color: red")

        self.fondo = QLabel('', self)
        self.fondo.setGeometry(15, 15, 870, 570)
        self.fondo.setStyleSheet("border-radius: 5px;"
                                 "color: white")
        self.fondo.setStyleSheet("background-color: black")

        self.separacion = QLabel(self)
        self.separacion.setGeometry(0, 297, 900, 15)
        self.separacion.setStyleSheet("background-color: red")

        # jugador 1
        self.imagen_jug_1 = QLabel(self)
        pixeles_jug_1 = QPixmap(RUTA_AVATAR_1)
        self.imagen_jug_1.setPixmap(pixeles_jug_1)
        self.imagen_jug_1.setScaledContents(True)
        self.imagen_jug_1.setGeometry(30, 30, 140, 160)

        self.nombre_jug_1 = QLabel("Jugador 1: NOMBRE", self.fondo)
        self.nombre_jug_1.setGeometry(170, 10, 500, 30)
        self.nombre_jug_1.setStyleSheet("border-radius: 5px;"
                                        "color: white")
        self.nombre_jug_1.setFont(QFont('Daytona', 14))

        self.pregunta_jug_1_1 = QLabel('¿Cuántas canicas apuestas?', self.fondo)
        self.pregunta_jug_1_1.setGeometry(170, 60, 2000, 30)
        self.pregunta_jug_1_1.setStyleSheet("color: white")
        self.pregunta_jug_1_1.setFont(QFont('Consolas', 10))

        self.spinbox1 = QSpinBox(self.fondo)
        self.spinbox1.setGeometry(250, 100, 60, 30)
        self.spinbox1.setStyleSheet("border-radius: 5px;"
                                    "color: white;"
                                    "border: 2px solid white")
        self.spinbox1.setFont(QFont('Consolas', 10))
        self.spinbox1.setRange(0, 10)

        self.pregunta_jug_1_2 = QLabel('La apuesta de tu oponente es', self.fondo)
        self.pregunta_jug_1_2.move(430, 65)
        self.pregunta_jug_1_2.setStyleSheet("color: white")
        self.pregunta_jug_1_2.setFont(QFont('Consolas', 10))

        self.par_jug_1 = QCheckBox(self.fondo)
        self.par_jug_1.move(470, 100)
        self.par_jug_1.setStyleSheet("color: white;")

        self.label_par_jug_1 = QLabel('Par', self.fondo)
        self.label_par_jug_1.move(490, 97)
        self.label_par_jug_1.setStyleSheet("color: white;")
        self.label_par_jug_1.setFont(QFont('Consolas', 10))

        self.impar_jug_1 = QCheckBox(self.fondo)
        self.impar_jug_1.move(610, 100)
        self.impar_jug_1.setStyleSheet("color: white;")

        self.label_impar_jug_1 = QLabel('Impar', self.fondo)
        self.label_impar_jug_1.move(630, 97)
        self.label_impar_jug_1.setStyleSheet("color: white;")
        self.label_impar_jug_1.setFont(QFont('Consolas', 10))

        self.boton_listo_jug_1 = QPushButton('Listo!', self)
        self.boton_listo_jug_1.setGeometry(750, 105, 80, 30)
        self.boton_listo_jug_1.setStyleSheet("background-color: white;"
                                             "border-radius: 2px;"
                                             "color: black")
        self.boton_listo_jug_1.setFont(QFont('Arial', 12))
        self.boton_listo_jug_1.clicked.connect(self.listo_1)

        # creacion de canicas
        pixeles_canica_1 = QPixmap(RUTA_CANICA_1)
        self.canica_jug_1 = QLabel(self.fondo)
        self.canica_jug_1.setPixmap(pixeles_canica_1)
        self.canica_jug_1.setScaledContents(True)
        self.canica_jug_1.setGeometry(105, 190, 70, 70)

        self.num_canicas1 = QLabel("10X", self)
        self.num_canicas1.setGeometry(35, 198, 90, 85)
        self.num_canicas1.setStyleSheet("background-color: black;"
                                        "border-radius: 2px;"
                                        "color: white")
        self.num_canicas1.setFont(QFont('Arial', 32))

        # creacion mensajes de espera
        self.label_espera_1 = QLabel("Esperando...", self.fondo)
        self.label_espera_1.move(240, 90)
        self.label_espera_1.setStyleSheet("color: grey")
        self.label_espera_1.setFont(QFont('Consolas', 12))
        self.label_espera_1.hide()

        self.label_espera_2 = QLabel("Esperando...", self.fondo)
        self.label_espera_2.move(510, 90)
        self.label_espera_2.setStyleSheet("color: grey")
        self.label_espera_2.setFont(QFont('Consolas', 12))
        self.label_espera_2.hide()

        self.label_espera_3 = QLabel("Esperando...", self.fondo)
        self.label_espera_3.move(240, 420)
        self.label_espera_3.setStyleSheet("color: grey")
        self.label_espera_3.setFont(QFont('Consolas', 12))
        self.label_espera_3.hide()

        self.label_espera_4 = QLabel("Esperando...", self.fondo)
        self.label_espera_4.move(510, 420)
        self.label_espera_4.setStyleSheet("color: grey")
        self.label_espera_4.setFont(QFont('Consolas', 12))
        self.label_espera_4.hide()

        self.reloj_jug_1 = QLabel(self.fondo)
        pixeles_reloj = QPixmap(RUTA_RELOJ)
        self.reloj_jug_1.setPixmap(pixeles_reloj)
        self.reloj_jug_1.setScaledContents(True)
        self.reloj_jug_1.setGeometry(710, 100, 110, 90)
        self.reloj_jug_1.hide()

        self.esperando_reloj_jug_1 = QLabel("Esperando...", self.fondo)
        self.esperando_reloj_jug_1.move(705, 185)
        self.esperando_reloj_jug_1.setStyleSheet("color: grey")
        self.esperando_reloj_jug_1.setFont(QFont('Consolas', 12))
        self.esperando_reloj_jug_1.hide()

        self.reloj_jug_2 = QLabel(self.fondo)
        self.reloj_jug_2.setPixmap(pixeles_reloj)
        self.reloj_jug_2.setScaledContents(True)
        self.reloj_jug_2.setGeometry(710, 420, 110, 90)
        self.reloj_jug_2.hide()

        self.esperando_reloj_jug_2 = QLabel("Esperando...", self.fondo)
        self.esperando_reloj_jug_2.setGeometry(705, 505, 120, 25)
        self.esperando_reloj_jug_2.setStyleSheet("color: grey")
        self.esperando_reloj_jug_2.setFont(QFont('Consolas', 12))
        self.esperando_reloj_jug_2.hide()

        # jugador 2
        self.imagen_jug_2 = QLabel(self)
        pixeles_jug_2 = QPixmap(RUTA_AVATAR_2)
        self.imagen_jug_2.setPixmap(pixeles_jug_2)
        self.imagen_jug_2.setScaledContents(True)
        self.imagen_jug_2.setGeometry(30, 330, 140, 160)

        self.nombre_jug_2 = QLabel("Jugador 2: NOMBRE", self.fondo)
        self.nombre_jug_2.setGeometry(170, 330, 500, 30)
        self.nombre_jug_2.setStyleSheet("border-radius: 5px;"
                                        "color: white")
        self.nombre_jug_2.setFont(QFont('Daytona', 14))

        self.pregunta_jug_2_1 = QLabel('¿Cuántas canicas apuestas?', self.fondo)
        self.pregunta_jug_2_1.setGeometry(170, 390, 2000, 30)
        self.pregunta_jug_2_1.setStyleSheet("color: white")
        self.pregunta_jug_2_1.setFont(QFont('Consolas', 10))

        self.spinbox2 = QSpinBox(self.fondo)
        self.spinbox2.setGeometry(250, 430, 60, 30)
        self.spinbox2.setStyleSheet("border-radius: 5px;"
                                    "color: white;"
                                    "border: 2px solid white")
        self.spinbox2.setFont(QFont('Consolas', 10))
        self.spinbox2.setRange(0, 10)

        self.pregunta_jug_2_2 = QLabel('La apuesta de tu oponente es', self.fondo)
        self.pregunta_jug_2_2.move(430, 395)
        self.pregunta_jug_2_2.setStyleSheet("color: white")
        self.pregunta_jug_2_2.setFont(QFont('Consolas', 10))

        self.par_jug_2 = QCheckBox(self.fondo)
        self.par_jug_2.move(470, 430)
        self.par_jug_2.setStyleSheet("color: white;")

        self.label_par_jug_2 = QLabel('Par', self.fondo)
        self.label_par_jug_2.move(490, 427)
        self.label_par_jug_2.setStyleSheet("color: white;")
        self.label_par_jug_2.setFont(QFont('Consolas', 10))

        self.impar_jug_2 = QCheckBox(self.fondo)
        self.impar_jug_2.move(610, 430)
        self.impar_jug_2.setStyleSheet("color: white;")

        self.label_impar_jug_2 = QLabel('Impar', self.fondo)
        self.label_impar_jug_2.move(630, 427)
        self.label_impar_jug_2.setStyleSheet("color: white;")
        self.label_impar_jug_2.setFont(QFont('Consolas', 10))

        self.boton_listo_jug_2 = QPushButton('Listo!', self)
        self.boton_listo_jug_2.setGeometry(750, 435, 80, 30)
        self.boton_listo_jug_2.setStyleSheet("background-color: white;"
                                             "border-radius: 2px;"
                                             "color: black")
        self.boton_listo_jug_2.setFont(QFont('Arial', 12))
        self.boton_listo_jug_2.clicked.connect(self.listo_2)

        # creacion de canicas
        pixeles_canica_2 = QPixmap(RUTA_CANICA_2)
        self.canica_jug_2 = QLabel(self.fondo)
        self.canica_jug_2.setPixmap(pixeles_canica_2)
        self.canica_jug_2.setScaledContents(True)
        self.canica_jug_2.setGeometry(105, 490, 70, 70)

        self.num_canicas2 = QLabel("10X", self)
        self.num_canicas2.setGeometry(35, 498, 90, 85)
        self.num_canicas2.setStyleSheet("background-color: black;"
                                        "border-radius: 2px;"
                                        "color: white")
        self.num_canicas2.setFont(QFont('Arial', 32))

    def listo_1(self):
        if self.spinbox1.text() != "0":  # se verifica el número apostado
            if self.par_jug_1.isChecked() and not self.impar_jug_1.isChecked():
                # se envía la info
                self.enviar_info_jug_1(int(self.spinbox1.text()), "par")
                print(f"Jugador 1 apuesta {self.spinbox1.text()} al par")
                self.esperando_reloj_jug_1.setText("Esperando...")
                self.esperando_reloj_jug_1.show()
                self.boton_listo_jug_1.hide()
                self.reloj_jug_1.show()
            elif self.impar_jug_1.isChecked() and not self.par_jug_1.isChecked():
                # se envía la info
                self.enviar_info_jug_1(int(self.spinbox1.text()), "impar")
                print(f"Jugador 1 apuesta {self.spinbox1.text()} al impar")
                self.esperando_reloj_jug_1.setText("Esperando...")
                self.esperando_reloj_jug_1.show()
                self.boton_listo_jug_1.hide()
                self.reloj_jug_1.show()
            else:
                self.esperando_reloj_jug_1.setText("Inválido...")
                self.esperando_reloj_jug_1.show()
        else:
            self.esperando_reloj_jug_1.setText("Inválido...")
            self.esperando_reloj_jug_1.show()

    def listo_2(self):
        if self.spinbox2.text() != "0":  # se verifica el número apostado
            if self.par_jug_2.isChecked() and not self.impar_jug_2.isChecked():
                self.enviar_info_jug_2(int(self.spinbox2.text()), "par")  # se envía la info
                print(f"Jugador 2 apuesta {self.spinbox2.text()} al par")
                self.esperando_reloj_jug_2.setText("Esperando...")
                self.esperando_reloj_jug_2.show()
                self.boton_listo_jug_2.hide()
                self.reloj_jug_2.show()
            elif self.impar_jug_2.isChecked() and not self.par_jug_2.isChecked():
                self.enviar_info_jug_2(int(self.spinbox2.text()), "impar")  # se envía la info
                print(f"Jugador 2 apuesta {self.spinbox2.text()} al impar")
                self.esperando_reloj_jug_2.setText("Esperando...")
                self.esperando_reloj_jug_2.show()
                self.boton_listo_jug_2.hide()
                self.reloj_jug_2.show()
            else:
                self.esperando_reloj_jug_2.setText("Inválido...")
                self.esperando_reloj_jug_2.show()
        else:
            self.esperando_reloj_jug_2.setText("Inválido...")
            self.esperando_reloj_jug_2.show()

    def enviar_info_jug_1(self, numero, par_o_impar):
        mensaje_enviar = "[PARTIDA]"
        nombre = self.nombre_jug_1.text().split(" ")[2]
        rival = self.nombre_jug_2.text().split(" ")[2]
        canicas_actuales = int(self.num_canicas1.text()[:2])
        mensaje_enviar += f"{str(par_o_impar)}-{numero}-{nombre}-{rival}-{canicas_actuales}"
        self.mensaje_juego_signal.emit(mensaje_enviar)

    def enviar_info_jug_2(self, numero, par_o_impar):
        mensaje_enviar = "[PARTIDA]"
        rival = self.nombre_jug_1.text().split(" ")[2]
        nombre = self.nombre_jug_2.text().split(" ")[2]
        canicas_actuales = int(self.num_canicas2.text()[:2])
        mensaje_enviar += f"{str(par_o_impar)}-{numero}-{nombre}-{rival}-{canicas_actuales}"
        self.mensaje_juego_signal.emit(mensaje_enviar)


import sys
if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    a = SalaJuego(QRect(500, 250, 900, 600))
    a.show()
    app.exec()
