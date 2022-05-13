from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import parametros as p
from random import randint
from backend.logica_juego import MiThread, Timer, Item, Tiempo
from frontend.ventana_inicio import Musica
import backend.funciones as f
from time import sleep


class VentanaJuego(QWidget):

    senal_abrir_juego = pyqtSignal()
    senal_tecla = pyqtSignal(str)
    senal_thread_up = pyqtSignal(str)
    senal_thread_right = pyqtSignal(str)
    senal_thread_left = pyqtSignal(str)
    senal_thread_down = pyqtSignal(str)
    senal_thread_salto = pyqtSignal(str)
    senal_thread_timer = pyqtSignal(int)
    senal_thread_item = pyqtSignal(str)
    senal_thread_tiempo = pyqtSignal(int)
    senal_abrir_post_nivel = pyqtSignal()

    def init_gui(self):
        self.pixeles_pasto = QPixmap(p.RUTA_PASTO)

    def __init__(self):
        super().__init__()

        self.setGeometry(350, 100, 1200, 900)
        self.setWindowTitle('Ventana de Juego')

        self.musica = Musica(p.RUTA_CANCION)

        self.thread_up = None
        self.senal_thread_up.connect(self.actualizar_labels_up)
        self.thread_right = None
        self.senal_thread_right.connect(self.actualizar_labels_right)
        self.thread_left = None
        self.senal_thread_left.connect(self.actualizar_labels_left)
        self.thread_down = None
        self.senal_thread_down.connect(self.actualizar_labels_down)
        self.thread_salto = None
        self.senal_thread_salto.connect(self.actualizar_labels_salto)
        self.thread_timer = None
        self.senal_thread_timer.connect(self.actualizar_timer)
        self.thread_item = None
        self.senal_thread_item.connect(self.actualizar_item)
        self.senal_thread_tiempo.connect(self.actualiza_tiempo)
        self.thread_tiempo = None
        self.senal_abrir_post_nivel.connect(self.esconder)

        # Elementos del mapa
        self.pasto = QLabel(self)
        pixeles_pasto = QPixmap(p.RUTA_PASTO)
        self.pasto.setPixmap(pixeles_pasto)
        self.pasto.setGeometry(0, 850, 2400, 550)

        self.rio = QLabel(self)
        pixeles_rio = QPixmap(p.RUTA_RIO)
        self.rio.setPixmap(pixeles_rio)
        self.rio.setGeometry(0, 700, 2400, 150)

        self.pasto_2 = QLabel(self)
        self.pasto_2.setPixmap(pixeles_pasto)
        self.pasto_2.setGeometry(0, 650, 2400, 50)

        self.calle = QLabel(self)
        self.calle.setGeometry(0, 500, 2400, 150)
        pixeles_calle = QPixmap(p.RUTA_CARRETERA)
        self.calle.setPixmap(pixeles_calle)
        self.calle.setScaledContents(True)

        self.pasto_3 = QLabel(self)
        self.pasto_3.setPixmap(pixeles_pasto)
        self.pasto_3.setGeometry(0, 450, 2400, 50)

        self.calle_2 = QLabel(self)
        self.calle_2.setGeometry(0, 300, 2400, 150)
        self.calle_2.setPixmap(pixeles_calle)
        self.calle_2.setScaledContents(True)

        self.pasto_4 = QLabel(self)
        self.pasto_4.setPixmap(pixeles_pasto)
        self.pasto_4.setGeometry(0, 200, 2400, 100)

        self.cuadro_0 = QLabel(self)
        self.cuadro_0.setStyleSheet("background-color: #663300;")
        self.cuadro_0.setGeometry(0, 0, 2400, 200)

        self.logo = QLabel(self)
        self.logo.setGeometry(500, 0, 200, 200)
        pixeles_logo = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles_logo)
        self.logo.setScaledContents(True)

        self.cuadro_1 = QLabel(self)
        self.cuadro_1.setStyleSheet("background-color: #C0C0C0;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.cuadro_1.setGeometry(10, 10, 350, 180)

        self.cuadro_2 = QLabel(self)
        self.cuadro_2.setStyleSheet("background-color: #C0C0C0;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.cuadro_2.setGeometry(840, 10, 350, 180)

        self.indicador_timer = QLabel("TIEMPO:                 sgds.", self)
        self.indicador_timer.move(60, 90)
        self.indicador_timer.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_timer = QLabel(f"{f.actualizar_tiempo()}     ", self)
        self.label_timer.move(189, 90)
        self.label_timer.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_vidas = QLabel(f"VIDAS:       ", self)
        self.label_vidas.move(60, 50)
        self.label_vidas.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_vidas_num = QLabel(f"  {f.retorna_vidas()}    ", self)
        self.label_vidas_num.move(176, 50)
        self.label_vidas_num.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_monedas = QLabel(f"MONEDAS:  ", self)
        self.label_monedas.move(60, 130)
        self.label_monedas.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_monedas_num = QLabel(f"  {f.retorna_monedas()}    ", self)
        self.label_monedas_num.move(178, 130)
        self.label_monedas_num.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_nivel = QLabel(f"NIVEL:        {f.retorna_nivel()}", self)
        self.label_nivel.move(855, 70)
        self.label_nivel.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_puntaje = QLabel("PUNTAJE:     ", self)
        self.label_puntaje.move(855, 120)
        self.label_puntaje.setFont(QFont('Arial Rounded MT Bold', 14))
        self.label_puntaje_num = QLabel(f"{f.retorna_puntaje()}           ", self)
        self.label_puntaje_num.move(983, 120)
        self.label_puntaje_num.setFont(QFont('Arial Rounded MT Bold', 14))

        self.pausar = QLabel('Pausar', self)
        self.pausar.setGeometry(1060, 70, 75, 30)
        self.pausar.setFont(QFont('Arial', 14))
        self.pausar.setStyleSheet("background-color: #FFFFFF;"
                                        "border-radius: 5px;"
                                        "color: black")
        self.salir = QLabel('Salir', self)
        self.salir.setGeometry(1075, 120, 48, 30)
        self.salir.setFont(QFont('Arial', 14))
        self.salir.setStyleSheet("background-color: #FFFFFF;"
                                        "border-radius: 5px;"
                                        "color: black")

        self.pos1_actual = randint(300, 1150)  # Evita toparse con troncos
        self.pos2_actual = 850

        self.rana = QLabel(self)
        self.pixeles_rana = QPixmap(p.RUTA_RANA)
        self.rana.setPixmap(self.pixeles_rana)
        self.rana.setScaledContents(True)
        self.rana.resize(50, 50)
        self.rana.move(self.pos1_actual, self.pos2_actual)
        self.ultima_tecla = "w"
        self.duracion_ronda = p.DURACION_RONDA_INICIAL

        self.tronco = self.crear_tronco()
        self.pos_tronco = 0
        self.tronco.move(self.pos_tronco, 700)
        self.tronco2 = self.crear_tronco()
        self.pos_tronco2 = 1100
        self.tronco2.move(self.pos_tronco2, 750)
        self.tronco3 = self.crear_tronco()
        self.pos_tronco3 = - 50
        self.tronco3.move(self.pos_tronco3, 800)
        self.tronco4 = self.crear_tronco()
        self.pos_tronco4 = p.lista_troncos[randint(0, 7)]
        self.tronco4.move(self.pos_tronco4, 700)
        self.tronco5 = self.crear_tronco()
        self.pos_tronco5 = p.lista_troncos2[randint(0, 7)]
        self.tronco5.move(self.pos_tronco5, 750)
        self.tronco6 = self.crear_tronco()
        self.pos_tronco6 = p.lista_troncos[randint(0, 7)]
        self.tronco6.move(self.pos_tronco6, 800)
        self.velocidad_tronco = p.VELOCIDAD_TRONCOS
        self.velocidad_autos = p.VELOCIDAD_AUTOS

        self.auto = self.crear_auto(1)
        self.pos_auto = - 150
        self.auto.move(self.pos_auto, 600)
        self.auto2 = self.crear_auto(1)
        self.pos_auto2 = - 450
        self.auto2.move(self.pos_auto2, 550)
        self.auto3 = self.crear_auto(0)
        self.pos_auto3 = 1300
        self.auto3.move(self.pos_auto3, 500)
        self.auto4 = self.crear_auto(0)
        self.pos_auto4 = 1550
        self.auto4.move(self.pos_auto4, 600)
        self.auto5 = self.crear_auto(1)
        self.pos_auto5 = - 150
        self.auto5.move(self.pos_auto5, 550)
        self.auto6 = self.crear_auto(1)
        self.pos_auto6 = - 450
        self.auto6.move(self.pos_auto6, 500)
        self.auto7 = self.crear_auto(0)
        self.pos_auto7 = - 150
        self.auto7.move(self.pos_auto7, 600)
        self.auto8 = self.crear_auto(0)
        self.pos_auto8 = - 450
        self.auto8.move(self.pos_auto8, 550)
        self.auto9 = self.crear_auto(1)
        self.pos_auto9 = 1300
        self.auto9.move(self.pos_auto9, 500)
        self.auto10 = self.crear_auto(1)
        self.pos_auto10 = 1700
        self.auto10.move(self.pos_auto10, 600)
        self.auto11 = self.crear_auto(0)
        self.pos_auto11 = - 150
        self.auto11.move(self.pos_auto11, 550)
        self.auto12 = self.crear_auto(0)
        self.pos_auto12 = - 600
        self.auto12.move(self.pos_auto12, 500)

        func_item = self.crear_item()
        self.item = func_item[0]
        self.icono_item = func_item[1] + 1
        self.item.move(p.lista_aleatorios_1[randint(0, 10)], p.lista_aleatorios_2[randint(0, 10)])
        func_item2 = self.crear_item()
        self.item2 = func_item2[0]
        self.icono_item2 = func_item2[1] + 1
        self.item2.move(p.lista_aleatorios_1[randint(0, 10)], p.lista_aleatorios_2[randint(0, 10)])
        func_item3 = self.crear_item()
        self.item3 = func_item3[0]
        self.icono_item3 = func_item3[1] + 1
        self.item3.move(p.lista_aleatorios_1[randint(0, 10)], p.lista_aleatorios_2[randint(0, 10)])
        func_item4 = self.crear_item()
        self.item4 = func_item4[0]
        self.icono_item4 = func_item4[1] + 1
        self.item4.move(p.lista_aleatorios_1[randint(0, 10)], p.lista_aleatorios_2[randint(0, 10)])

    def crear_tronco(self):
        tronco = QLabel(self)
        pixeles_tronco = QPixmap(p.RUTA_TRONCO)
        tronco.setPixmap(pixeles_tronco)
        tronco.setScaledContents(True)
        tronco.resize(150, 50)
        return tronco

    def crear_auto(self, num):  # num=0 es de izq-der, num=1 es de der-izq
        auto = QLabel(self)
        lista_right = [QPixmap(p.RUTA_ROJO_RIGHT), QPixmap(p.RUTA_AMARILLO_RIGHT), QPixmap(p.RUTA_AZUL_RIGHT), QPixmap(p.RUTA_PLATA_RIGHT), QPixmap(p.RUTA_MORADO_RIGHT), QPixmap(p.RUTA_NEGRO_RIGHT), QPixmap(p.RUTA_BLANCO_RIGHT)]
        lista_left = [QPixmap(p.RUTA_ROJO_LEFT), QPixmap(p.RUTA_AMARILLO_LEFT), QPixmap(p.RUTA_AZUL_LEFT), QPixmap(p.RUTA_PLATA_LEFT), QPixmap(p.RUTA_MORADO_LEFT), QPixmap(p.RUTA_NEGRO_LEFT), QPixmap(p.RUTA_BLANCO_LEFT)]
        if num == 0:
            pixeles_auto = lista_right[randint(0, 6)]
        else:
            pixeles_auto = lista_left[randint(0, 6)]
        auto.setPixmap(pixeles_auto)
        auto.setScaledContents(True)
        auto.resize(120, 40)
        return auto

    def crear_item(self):
        item = QLabel(self)
        lista = [QPixmap(p.RUTA_CALAVERA), QPixmap(p.RUTA_CORAZON), QPixmap(p.RUTA_RELOJ), QPixmap(p.RUTA_MONEDA)]
        num = randint(0, 3)
        pixeles_item = lista[num]
        item.setPixmap(pixeles_item)
        item.setScaledContents(True)
        item.resize(30, 30)
        return (item, num)

    def ejecutar_threads_up(self):
        if self.thread_up is None or not self.thread_up.is_alive():
            self.thread_up = MiThread(self.senal_thread_up)
            self.thread_up.start()

    def ejecutar_threads_right(self):
        if self.thread_right is None or not self.thread_right.is_alive():
            self.thread_right = MiThread(self.senal_thread_right)
            self.thread_right.start()

    def ejecutar_threads_left(self):
        if self.thread_left is None or not self.thread_left.is_alive():
            self.thread_left = MiThread(self.senal_thread_left)
            self.thread_left.start()

    def ejecutar_threads_down(self):
        if self.thread_down is None or not self.thread_down.is_alive():
            self.thread_down = MiThread(self.senal_thread_down)
            self.thread_down.start()

    def ejecutar_threads_salto(self):
        if self.thread_salto is None or not self.thread_salto.is_alive():
            self.thread_salto = MiThread(self.senal_thread_salto)
            self.thread_salto.start()

    def ejecutar_threads_timer(self):
        if self.thread_timer is None or not self.thread_timer.is_alive():
            self.thread_timer = Timer(self.senal_thread_timer, p.DURACION_RONDA_INICIAL * 100)  # para que se ejecute constantemente
            self.thread_timer.start()

    def ejecutar_threads_tiempo(self):
        if self.thread_tiempo is None or not self.thread_tiempo.is_alive():
            self.thread_tiempo = Tiempo(self.senal_thread_tiempo, p.DURACION_RONDA_INICIAL * 100)  # para que se ejecute por suficiente tiempo
            self.thread_tiempo.start()

    def ejecutar_threads_item(self):
        if self.thread_item is None or not self.thread_item.is_alive():
            self.thread_item = Item(self.senal_thread_item)
            self.thread_item.start()

    def actualizar_labels_up(self, evento):
        ranas = [QPixmap(p.RUTA_UP1), QPixmap(p.RUTA_UP2), QPixmap(p.RUTA_UP3)]
        self.rana.setPixmap(QPixmap(ranas[int(evento)]))
        self.rana.setScaledContents(True)
        self.rana.resize(50, 50)

    def actualizar_labels_right(self, evento):
        ranas = [QPixmap(p.RUTA_RIGHT1), QPixmap(p.RUTA_RIGHT2), QPixmap(p.RUTA_RIGHT3)]
        self.rana.setPixmap(QPixmap(ranas[int(evento)]))
        self.rana.setScaledContents(True)
        self.rana.resize(50, 50)

    def actualizar_labels_left(self, evento):
        ranas = [QPixmap(p.RUTA_LEFT1), QPixmap(p.RUTA_LEFT2), QPixmap(p.RUTA_LEFT3)]
        self.rana.setPixmap(QPixmap(ranas[int(evento)]))
        self.rana.setScaledContents(True)
        self.rana.resize(50, 50)

    def actualizar_labels_down(self, evento):
        ranas = [QPixmap(p.RUTA_DOWN1), QPixmap(p.RUTA_DOWN2), QPixmap(p.RUTA_DOWN3)]
        self.rana.setPixmap(QPixmap(ranas[int(evento)]))
        self.rana.setScaledContents(True)
        self.rana.resize(50, 50)

    def actualizar_labels_salto(self, evento):
        ranas = [QPixmap(p.RUTA_JUMP1), QPixmap(p.RUTA_JUMP2), QPixmap(p.RUTA_JUMP3)]
        self.rana.setPixmap(QPixmap(ranas[int(evento)]))
        self.rana.setScaledContents(True)
        self.rana.resize(50, 50)

    def actualizar_item(self, evento):
        lista = [QPixmap(p.RUTA_CALAVERA), QPixmap(p.RUTA_CORAZON), QPixmap(p.RUTA_RELOJ), QPixmap(p.RUTA_MONEDA)]
        n_item = randint(0, 3)
        n_item2 = randint(0, 3)
        n_item3 = randint(0, 3)
        n_item4 = randint(0, 3)
        if n_item == 0:
            self.icono_item = 1  # calavera
        if n_item == 1:
            self.icono_item = 2  # corazon
        if n_item == 2:
            self.icono_item = 3  # reloj
        if n_item == 3:
            self.icono_item = 4  # moneda

        if n_item2 == 0:
            self.icono_item2 = 1  # calavera
        if n_item2 == 1:
            self.icono_item2 = 2  # corazon
        if n_item2 == 2:
            self.icono_item2 = 3  # reloj
        if n_item2 == 3:
            self.icono_item2 = 4  # moneda

        if n_item3 == 0:
            self.icono_item3 = 1  # calavera
        if n_item3 == 1:
            self.icono_item3 = 2  # corazon
        if n_item3 == 2:
            self.icono_item3 = 3  # reloj
        if n_item3 == 3:
            self.icono_item3 = 4  # moneda

        if n_item4 == 0:
            self.icono_item4 = 1  # calavera
        if n_item4 == 1:
            self.icono_item4 = 2  # corazon
        if n_item4 == 2:
            self.icono_item4 = 3  # reloj
        if n_item4 == 3:
            self.icono_item4 = 4  # moneda

        self.item.setPixmap(QPixmap(lista[n_item]))
        self.item.setScaledContents(True)
        self.item.resize(30, 30)
        self.item.move(p.lista_aleatorios_1[randint(0, 24)], p.lista_aleatorios_2[randint(0, 10)])
        self.item2.setPixmap(QPixmap(lista[n_item2]))
        self.item2.setScaledContents(True)
        self.item2.resize(30, 30)
        self.item2.move(p.lista_aleatorios_1[randint(0, 24)], p.lista_aleatorios_2[randint(0, 10)])
        self.item3.setPixmap(QPixmap(lista[n_item3]))
        self.item3.setScaledContents(True)
        self.item3.resize(30, 30)
        self.item3.move(p.lista_aleatorios_1[randint(0, 24)], p.lista_aleatorios_2[randint(0, 10)])
        self.item4.move(p.lista_aleatorios_1[randint(0, 24)], p.lista_aleatorios_2[randint(0, 10)])
        self.item4.setPixmap(QPixmap(lista[n_item4]))
        self.item4.setScaledContents(True)
        self.item4.resize(30, 30)

    def actualizar_timer(self):
        self.label_timer.setText(str(f.actualizar_tiempo()))
        self.ejecutar_threads_item()
        # Derrota
        if int(f.retorna_tiempo()) <= 0 or int(f.retorna_vidas()) == 0:
            self.derrota()

    def actualiza_tiempo(self, evento):
        if int(self.rana.y() >= 850):
            self.pos2_actual = 850
            self.rana.move(self.pos1_actual, self.pos2_actual)
        if int(self.rana.x() < - 30):
            self.pos1_actual = -30
            self.rana.move(self.pos1_actual, self.pos2_actual)
        if int(self.rana.x() >= 1180):
            self.pos1_actual = 1180
            self.rana.move(self.pos1_actual, self.pos2_actual)
        # Quedarse encima del tronco
        if ((int(self.pos_tronco3) - 15 <= int(self.rana.x()) <= int(self.pos_tronco3) + 120) or (int(self.pos_tronco6) - 15 <= int(self.rana.x()) <= int(self.pos_tronco6) + 120)) and (760 <= self.rana.y() <= 800):
            self.pos1_actual = self.pos1_actual + 1*self.velocidad_tronco
            self.rana.move(self.pos1_actual, 780)
        if ((int(self.pos_tronco2) + 120 >= int(self.rana.x()) >= int(self.pos_tronco2) - 15) or (int(self.pos_tronco5) + 120 >= int(self.rana.x()) >= int(self.pos_tronco5) - 15)) and (710 <= self.rana.y() <= 750):
            self.pos1_actual = self.pos1_actual - 1*self.velocidad_tronco
            self.rana.move(self.pos1_actual, 730)
        if ((int(self.pos_tronco) - 15 <= int(self.rana.x()) <= int(self.pos_tronco) + 120) or (int(self.pos_tronco4) - 15 <= int(self.rana.x()) <= int(self.pos_tronco4) + 120)) and (660 <= self.rana.y() <= 700):
            self.pos1_actual = self.pos1_actual + 1*self.velocidad_tronco
            self.rana.move(self.pos1_actual, 680)

        if ((760 <= self.rana.y() < 800) and (self.rana.x() + 15 < self.tronco3.x() or self.rana.x() > self.tronco3.x() + 130)) and (self.rana.x() + 15 < self.tronco6.x() or self.rana.x() > self.tronco6.x() + 130):
            self.respawnear()
        if ((660 <= self.rana.y() <= 700) and (self.rana.x() + 15 < self.tronco.x() or self.rana.x() > self.tronco.x() + 130)) and (self.rana.x() + 15 < self.tronco4.x() or self.rana.x() > self.tronco4.x() + 130):
            self.respawnear()
        if ((710 <= self.rana.y() <= 760) and (self.rana.x() + 30 < self.tronco2.x() or self.rana.x() > self.tronco2.x() + 120)) and (self.rana.x() + 30 < self.tronco5.x() or self.rana.x() > self.tronco5.x() + 120):
            self.respawnear()
        if (700 <= self.rana.y() <= 800) and (self.rana.x() < - 29 or self.rana.x() > 1179):
            self.respawnear()
        #  Chocar con un auto
        if (460 <= self.rana.y() <= 510) and ((self.auto.x() - 30 <= self.rana.x() <= self.auto.x() + 130) or (self.auto2.x() - 30 <= self.rana.x() <= self.auto2.x() + 130)):
            self.respawnear()
        if (510 <= self.rana.y() <= 560) and ((self.auto3.x() - 20 <= self.rana.x() <= self.auto3.x() + 130) or (self.auto4.x() - 20 <= self.rana.x() <= self.auto4.x() + 130)):
            self.respawnear()
        if (560 <= self.rana.y() <= 600) and ((self.auto5.x() - 30 <= self.rana.x() <= self.auto5.x() + 130) or (self.auto6.x() - 30 <= self.rana.x() <= self.auto6.x() + 130)):
            self.respawnear()
        if (260 <= self.rana.y() <= 310) and ((self.auto7.x() - 20 <= self.rana.x() <= self.auto7.x() + 130) or (self.auto8.x() - 20 <= self.rana.x() <= self.auto8.x() + 130)):
            self.respawnear()
        if (310 <= self.rana.y() <= 360) and ((self.auto9.x() - 30 <= self.rana.x() <= self.auto9.x() + 130) or (self.auto10.x() - 30 <= self.rana.x() <= self.auto10.x() + 130)):
            self.respawnear()
        if (360 <= self.rana.y() <= 400) and ((self.auto11.x() - 20 <= self.rana.x() <= self.auto11.x() + 130) or (self.auto12.x() - 20 <= self.rana.x() <= self.auto12.x() + 130)):
            self.respawnear()

        self.pos_tronco += (1*self.velocidad_tronco / p.TIEMPO_TRONCOS)
        self.tronco.move(self.pos_tronco, 700)
        self.pos_tronco2 -= (1*self.velocidad_tronco / p.TIEMPO_TRONCOS)
        self.tronco2.move(self.pos_tronco2, 750)
        self.pos_tronco3 += (1*self.velocidad_tronco / p.TIEMPO_TRONCOS)
        self.tronco3.move(self.pos_tronco3, 800)
        self.pos_tronco4 += (1*self.velocidad_tronco / p.TIEMPO_TRONCOS)
        self.tronco4.move(self.pos_tronco4, 700)
        self.pos_tronco5 -= (1*self.velocidad_tronco / p.TIEMPO_TRONCOS)
        self.tronco5.move(self.pos_tronco5, 750)
        self.pos_tronco6 += (1*self.velocidad_tronco / p.TIEMPO_TRONCOS)
        self.tronco6.move(self.pos_tronco6, 800)

        self.pos_auto -= (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto.move(self.pos_auto, 500)
        self.pos_auto2 -= (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto2.move(self.pos_auto2, 500)
        self.pos_auto3 += (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto3.move(self.pos_auto3, 550)
        self.pos_auto4 += (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto4.move(self.pos_auto4, 550)
        self.pos_auto5 -= (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto5.move(self.pos_auto5, 600)
        self.pos_auto6 -= (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto6.move(self.pos_auto6, 600)

        self.pos_auto7 += (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto7.move(self.pos_auto7, 300)
        self.pos_auto8 += (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto8.move(self.pos_auto8, 300)
        self.pos_auto9 -= (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto9.move(self.pos_auto9, 350)
        self.pos_auto10 -= (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto10.move(self.pos_auto10, 350)
        self.pos_auto11 += (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto11.move(self.pos_auto11, 400)
        self.pos_auto12 += (1*self.velocidad_autos / p.TIEMPO_AUTOS)
        self.auto12.move(self.pos_auto12, 400)

        #  Para que los troncos y autos vuelvan a salir
        if self.pos_tronco >= 1480:
            self.pos_tronco = - 140
            self.tronco.move(self.pos_tronco, 700)
        if self.pos_tronco2 <= -150:
            self.pos_tronco2 = 1250
            self.tronco2.move(self.pos_tronco2, 750)
        if self.pos_tronco3 >= 1480:
            self.pos_tronco3 = -140
            self.tronco3.move(self.pos_tronco3, 800)
        if self.pos_tronco4 >= 1570:
            self.pos_tronco4 = p.lista_troncos[randint(0, 7)]
            self.tronco4.move(self.pos_tronco4, 700)
        if self.pos_tronco5 <= -300:
            self.pos_tronco5 = p.lista_troncos2[randint(0, 7)]
            self.tronco5.move(self.pos_tronco5, 750)
        if self.pos_tronco6 >= 1570:
            self.pos_tronco6 = p.lista_troncos[randint(0, 7)]
            self.tronco6.move(self.pos_tronco6, 800)

        if self.pos_auto <= - 300:
            self.auto_nuevo = self.crear_auto(1)
            self.auto.hide()
            self.auto = self.auto_nuevo
            self.auto.show()
            self.pos_auto = p.lista_autos2[randint(5, 8)]
            self.auto.move(self.pos_auto, 500)
        if self.pos_auto2 <= - 300:
            self.auto_nuevo2 = self.crear_auto(1)
            self.auto2.hide()
            self.auto2 = self.auto_nuevo2
            self.auto2.show()
            self.pos_auto2 = p.lista_autos2[randint(0, 4)]
            self.auto2.move(self.pos_auto2, 500)
        if self.pos_auto3 >= 1500:
            self.auto_nuevo3 = self.crear_auto(0)
            self.auto3.hide()
            self.auto3 = self.auto_nuevo3
            self.auto3.show()
            self.pos_auto3 = p.lista_autos[randint(5, 8)]
            self.auto3.move(self.pos_auto3, 550)
        if self.pos_auto4 >= 1500:
            self.auto_nuevo4 = self.crear_auto(0)
            self.auto4.hide()
            self.auto4 = self.auto_nuevo4
            self.auto4.show()
            self.pos_auto4 = p.lista_autos[randint(0, 4)]
            self.auto4.move(self.pos_auto4, 550)
        if self.pos_auto5 <= - 300:  # los últimos dos autos no cambian
            self.pos_auto5 = p.lista_autos2[randint(5, 8)]
            self.auto5.move(self.pos_auto5, 600)
        if self.pos_auto6 <= - 300:
            self.pos_auto6 = p.lista_autos2[randint(0, 4)]
            self.auto6.move(self.pos_auto6, 600)

        if self.pos_auto7 >= 1500:
            self.auto_nuevo7 = self.crear_auto(0)
            self.auto7.hide()
            self.auto7 = self.auto_nuevo7
            self.auto7.show()
            self.pos_auto7 = p.lista_autos[randint(5, 8)]
            self.auto7.move(self.pos_auto7, 300)
        if self.pos_auto8 >= 1500:
            self.auto_nuevo8 = self.crear_auto(0)
            self.auto8.hide()
            self.auto8 = self.auto_nuevo8
            self.auto8.show()
            self.pos_auto8 = p.lista_autos[randint(0, 4)]
            self.auto8.move(self.pos_auto8, 300)
        if self.pos_auto9 <= - 300:
            self.auto_nuevo9 = self.crear_auto(1)
            self.auto9.hide()
            self.auto9 = self.auto_nuevo9
            self.auto9.show()
            self.pos_auto9 = p.lista_autos2[randint(5, 8)]
            self.auto9.move(self.pos_auto9, 350)
        if self.pos_auto10 <= - 300:
            self.auto_nuevo10 = self.crear_auto(1)
            self.auto10.hide()
            self.auto10 = self.auto_nuevo10
            self.auto10.show()
            self.pos_auto10 = p.lista_autos2[randint(0, 4)]
            self.auto10.move(self.pos_auto10, 350)
        if self.pos_auto11 >= 1500:
            self.pos_auto11 = p.lista_autos[randint(5, 8)]
            self.auto11.move(self.pos_auto11, 400)
        if self.pos_auto12 >= 1500:
            self.pos_auto12 = p.lista_autos[randint(0, 4)]
            self.auto12.move(self.pos_auto12, 400)

        #  Interacción con items
        if (self.item.y() - 10 >= self.rana.y() >= self.item.y() - 30) and (self.item.x() - 30 <= self.rana.x() <= self.item.x() + 30):
            if self.icono_item == 1:  # Calavera - Item 1
                self.velocidad_tronco = float(self.velocidad_tronco*1.05)
                self.actualizar_item(self.senal_thread_item)
            if self.icono_item == 2:  # Vidas - Item 1
                f.sumar_vida()
                self.actualizar_item(self.senal_thread_item)
                self.label_vidas_num.setText(f"  {f.retorna_vidas()}    ")
            if self.icono_item == 3:  # Reloj - Item 1
                f.sumar_tiempo()
                self.actualizar_item(self.senal_thread_item)
                self.label_timer.setText(f"{f.retorna_tiempo()}    ")
            if self.icono_item == 4:  # Moneda - Item 1
                f.sumar_moneda()
                self.actualizar_item(self.senal_thread_item)
                self.label_monedas_num.setText(f"  {f.retorna_monedas()}    ")

        if (self.item2.y() - 10 >= self.rana.y() >= self.item2.y() - 30) and (self.item2.x() - 30 <= self.rana.x() <= self.item2.x() + 30):
            if self.icono_item2 == 1:  # Calavera - Item 2
                self.velocidad_tronco = float(self.velocidad_tronco*1.05)
                self.actualizar_item(self.senal_thread_item)
            if self.icono_item2 == 2:  # Vidas - Item 2
                f.sumar_vida()
                self.actualizar_item(self.senal_thread_item)
                self.label_vidas_num.setText(f"  {f.retorna_vidas()}    ")
            if self.icono_item2 == 3:  # Reloj - Item 2
                f.sumar_tiempo()
                self.actualizar_item(self.senal_thread_item)
                self.label_timer.setText(f"{f.retorna_tiempo()}    ")
            if self.icono_item2 == 4:  # Moneda - Item 2
                f.sumar_moneda()
                self.actualizar_item(self.senal_thread_item)
                self.label_monedas_num.setText(f"  {f.retorna_monedas()}    ")

        if (self.item3.y() - 10 >= self.rana.y() >= self.item3.y() - 30) and (self.item3.x() - 30 <= self.rana.x() <= self.item3.x() + 30):
            if self.icono_item3 == 1:  # Calavera - Item 3
                self.velocidad_tronco = float(self.velocidad_tronco*1.05)
                self.actualizar_item(self.senal_thread_item)
            if self.icono_item3 == 2:  # Vidas - Item 3
                f.sumar_vida()
                self.actualizar_item(self.senal_thread_item)
                self.label_vidas_num.setText(f"  {f.retorna_vidas()}    ")
            if self.icono_item3 == 3:  # Reloj - Item 3
                f.sumar_tiempo()
                self.actualizar_item(self.senal_thread_item)
                self.label_timer.setText(f"{f.retorna_tiempo()}    ")
            if self.icono_item3 == 4:  # Moneda - Item 3
                f.sumar_moneda()
                self.actualizar_item(self.senal_thread_item)
                self.label_monedas_num.setText(f"  {f.retorna_monedas()}    ")

        if (self.item4.y() - 10 >= self.rana.y() >= self.item4.y() - 30) and (self.item4.x() - 30 <= self.rana.x() <= self.item4.x() + 30):
            if self.icono_item4 == 1:  # Calavera - Item 4
                self.velocidad_tronco = float(self.velocidad_tronco*1.05)
                self.actualizar_item(self.senal_thread_item)
            if self.icono_item4 == 2:  # Vidas - Item 4
                f.sumar_vida()
                self.actualizar_item(self.senal_thread_item)
                self.label_vidas_num.setText(f"  {f.retorna_vidas()}    ")
            if self.icono_item4 == 3:  # Reloj - Item 4
                f.sumar_tiempo()
                self.actualizar_item(self.senal_thread_item)
                self.label_timer.setText(f"{f.retorna_tiempo()}    ")
            if self.icono_item4 == 4:  # Moneda - Item 4
                f.sumar_moneda()
                self.actualizar_item(self.senal_thread_item)
                self.label_monedas_num.setText(f"  {f.retorna_monedas()}    ")

        #  Evitar que troncos y autos se superpongan
        if self.tronco6.x() - 160 < self.tronco3.x() < self.tronco6.x() + 160:
            self.tronco6.move(1500, 800)
        if self.tronco4.x() - 160 < self.tronco.x() < self.tronco4.x() + 160:
            self.tronco4.move(- 300, 750)
        if self.tronco2.x() + 160 > self.tronco5.x() > self.tronco2.x() - 160:
            self.tronco5.move(1500, 700)
        if self.auto2.x() - 140 < self.auto.x() < self.auto2.x() + 140:
            self.auto2.move(- 300, 500)
        if self.auto4.x() - 140 < self.auto3.x() < self.auto4.x() + 140:
            self.auto4.move(1400, 550)
        if self.auto6.x() + 140 > self.auto5.x() > self.auto6.x() - 140:
            self.auto6.move(- 300, 600)
        if self.auto8.x() - 140 < self.auto7.x() < self.auto8.x() + 140:
            self.auto8.move(1400, 300)
        if self.auto10.x() - 140 < self.auto9.x() < self.auto10.x() + 140:
            self.auto10.move(- 300, 350)
        if self.auto12.x() + 140 > self.auto11.x() > self.auto12.x() - 140:
            self.auto12.move(1400, 400)

        #  FIN DEL NIVEL
        if self.rana.y() <= 250:
            self.ocultar()
            self.pos1_actual = randint(300, 1150)
            self.pos2_actual = 850
            self.rana.move(self.pos1_actual, self.pos2_actual)

    def respawnear(self):
        self.pos1_actual = randint(0, 1150)
        self.pos2_actual = 830
        self.rana.move(self.pos1_actual, self.pos2_actual)
        f.restar_vida()
        self.label_vidas_num.setText(f"  {f.retorna_vidas()}    ")

    def cambio_rana(self):
        self.rana_nueva = QLabel(self)
        self.rana_nueva.setPixmap(self.pixeles_rana)
        self.rana_nueva.setScaledContents(True)
        self.rana_nueva.resize(50, 50)

    def keyPressEvent(self, event):
        if str(event.text()) == "p" or str(event.text()) == "P":
            self.thread_tiempo.stop()
            print("PAUSA")

        if (str(event.text()) == "w" or str(event.text()) == "W"):
            if 680 <= self.rana.y() <= 830:
                self.ultima_tecla = "w"
                self.ejecutar_threads_up()
            else:
                self.cambio_rana()
                self.pos2_actual -= p.VELOCIDAD_CAMINAR
                self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
                self.rana_nueva.show()
                self.rana.hide()
                self.rana = self.rana_nueva
                self.ultima_tecla = "w"
                self.ejecutar_threads_up()

        if str(event.text()) == "a" or str(event.text()) == "A":
            self.cambio_rana()
            self.pos1_actual -= p.VELOCIDAD_CAMINAR
            self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
            self.rana_nueva.show()
            self.rana.hide()
            self.rana = self.rana_nueva
            self.ultima_tecla = "a"
            self.ejecutar_threads_left()

        if str(event.text()) == "s" or str(event.text()) == "S":
            if 650 <= self.rana.y() <= 800:
                self.ultima_tecla = "s"
                self.ejecutar_threads_down()
            else:
                self.cambio_rana()
                self.pos2_actual += p.VELOCIDAD_CAMINAR
                self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
                self.rana_nueva.show()
                self.rana.hide()
                self.rana = self.rana_nueva
                self.ultima_tecla = "s"
                self.ejecutar_threads_down()

        if str(event.text()) == "d" or str(event.text()) == "D":
            self.cambio_rana()
            self.pos1_actual += p.VELOCIDAD_CAMINAR
            self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
            self.rana_nueva.show()
            self.rana.hide()
            self.rana = self.rana_nueva
            self.ultima_tecla = "d"
            self.ejecutar_threads_right()

        if str(event.text()) == " ":
            self.cambio_rana()
            if self.ultima_tecla == "w":
                self.pos2_actual -= p.PIXELES_SALTO
                self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
            if self.ultima_tecla == "s":
                self.pos2_actual += p.PIXELES_SALTO
                self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
                self.ejecutar_threads_salto()
            if self.ultima_tecla == "a":
                self.pos1_actual -= p.PIXELES_SALTO
                self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
            if self.ultima_tecla == "d":
                self.pos1_actual += p.PIXELES_SALTO
                self.rana_nueva.move(self.pos1_actual, self.pos2_actual)
            self.rana_nueva.show()
            self.rana.hide()
            self.rana = self.rana_nueva
            self.ejecutar_threads_salto()

    def mousePressEvent(self, event):
        if 70 <= event.y() <= 100 and 1060 <= event.x() <= 1140:
            print("PAUSA")
        if 120 <= event.y() <= 150 and 1060 <= event.x() <= 1140:
            self.hide()
            self.musica.pausar()
            self.thread_timer.stop = True
            self.thread_tiempo.stop = True
            self.thread_item.stop = True

    def mostrar_juego(self):
        self.show()
        self.ejecutar_threads_timer()
        self.ejecutar_threads_tiempo()
        self.senal_abrir_juego.emit()
        self.musica.comenzar()

    def ocultar(self):
        self.hide()
        self.setGeometry(0, 0, 0, 0)
        self.musica.pausar()
        # Se modifican los valores para un nuevo juego
        velocidad_autos = float(self.velocidad_autos * (2 / (1 + p.PONDERACION_DIFICULTAD)))
        velocidad_troncos = float(self.velocidad_tronco * (2 / (1 + p.PONDERACION_DIFICULTAD)))
        self.tiempo_restante = f.retorna_tiempo()
        f.registrar_tiempo_sobra(self.tiempo_restante)
        f.mantener_tiempo()
        self.nuevo_juego(velocidad_troncos, velocidad_autos)

    def esconder(self):
        self.hide()

    def derrota(self):
        self.senal_abrir_post_nivel.emit()
        self.thread_timer.stop = True
        self.thread_tiempo.stop = True
        self.thread_item.stop = True
        self.item.hide()
        self.item2.hide()
        self.item3.hide()
        self.item4.hide()
        self.close()
        self.musica.pausar()

    def nuevo_juego(self, velocidad_troncos, velocidad_autos):
        f.actualizar_nivel()
        puntaje = int(f.retorna_puntaje_ronda())
        f.registrar_puntaje_ronda(puntaje)
        puntaje_agregar_total = puntaje
        f.registrar_puntaje_total(puntaje_agregar_total)
        self.label_nivel.setText(f"NIVEL:        {f.retorna_nivel()}")
        self.duracion_ronda = int(p.PONDERACION_DIFICULTAD * self.duracion_ronda)
        self.velocidad_tronco = velocidad_troncos
        self.velocidad_autos = velocidad_autos
        self.label_puntaje_num.setText(f"{f.retorna_puntaje_total()}                 ")
        self.setGeometry(350, 100, 1200, 900)
        self.senal_abrir_post_nivel.emit()
