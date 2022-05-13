from os import closerange
from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(tuple)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_contrasena(self, credenciales):
        usuario = str(credenciales)
        valido = False
        if p.MIN_CARACTERES < len(usuario) <= p.MAX_CARACTERES and not "," in usuario:
            valido = True
        self.senal_respuesta_validacion.emit((usuario, valido))
