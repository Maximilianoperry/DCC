from random import randint
from PyQt5.QtCore import QObject, pyqtSignal, QRect, QTimer
from PyQt5.QtGui import QPixmap
from threading import Thread
from time import sleep
import parametros as p


class MiThread(Thread):

    def __init__(self, senal_actualizar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.senal_actualizar = senal_actualizar
        self.stop = False

    def run(self):
        for i in range(3):
            sleep(0.2)
            self.senal_actualizar.emit(str(i))
            if self.stop:
                break


class Tiempo(Thread):

    def __init__(self, senal_tiempo, tiempo):
        super().__init__()
        self.tiempo = tiempo
        self.senal_tiempo = senal_tiempo
        self.stop = False

    def run(self):
        for i in range(int(self.tiempo/0.005), -1, -1):
            sleep(0.005)
            self.senal_tiempo.emit(int(i))
            if self.stop:
                break


class Timer(Thread):

    def __init__(self, senal_tiempo, tiempo):
        super().__init__()
        self.tiempo = tiempo
        self.senal_tiempo = senal_tiempo
        self.stop = False

    def run(self):
        for i in range(self.tiempo, -1, -1):
            self.senal_tiempo.emit(int(i))
            sleep(1)
            if self.stop:
                break


class Item(Thread):

    def __init__(self, senal_actualizar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.senal_actualizar = senal_actualizar
        self.stop = False

    def run(self):
        for i in range(4):
            sleep(p.TIEMPO_OBJETO)
            self.senal_actualizar.emit(str(i))
            if self.stop:
                break
