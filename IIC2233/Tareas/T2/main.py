import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

import parametros as p
import backend.funciones as f
from backend.logica_inicio import LogicaInicio
from frontend.ventana_inicio import VentanaInicio
#from backend.logica_ranking import LogicaRanking
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post_nivel import VentanaPostNivel
from frontend.ventana_tienda import VentanaTienda
from frontend.ventana_comprar_vida import VentanaComprarVida
from frontend.ventana_comprar_vida import VentanaSkin
from frontend.ventana_comprar_vida import VentanaNoMonedas

f.llenar_archivos()  # Se rellena el archivo para llenar labels

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventanas
    tamano_ventana = QRect(550, 300, 800, 600)
    ventana_inicio = VentanaInicio(tamano_ventana)
    ventana_ranking = VentanaRanking()
    ventana_juego = VentanaJuego()
    ventana_post_nivel = VentanaPostNivel()
    ventana_tienda = VentanaTienda()
    ventana_comprar_vida = VentanaComprarVida()
    ventana_skin = VentanaSkin()
    ventana_insuficiente = VentanaNoMonedas()

    # Instanciación de lógica
    logica_inicio = LogicaInicio()

    # ~~ Conexiones de señales ~~

    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)

    ventana_inicio.senal_enviar_login.connect(
        logica_inicio.comprobar_contrasena
    )

    ventana_juego.senal_abrir_post_nivel.connect(ventana_post_nivel.abrir_ventana_post_nivel)

    ventana_inicio.senal_abrir_ranking.connect(ventana_ranking.mostrar_ranking)  # descomentar

    ventana_ranking.senal_cerrar_ranking.connect(ventana_inicio.mostrar)

    ventana_inicio.senal_abrir_juego.connect(ventana_juego.mostrar_juego)

    ventana_post_nivel.senal_abrir_juego.connect(ventana_juego.mostrar_juego)

    ventana_post_nivel.senal_cerrar_juego.connect(ventana_juego.derrota)

    ventana_post_nivel.senal_abrir_tienda.connect(ventana_tienda.mostrar)

    ventana_tienda.senal_abrir_post_nivel.connect(ventana_post_nivel.show)

    ventana_tienda.senal_sumar_vida.connect(ventana_comprar_vida.show)

    ventana_tienda.senal_skin.connect(ventana_skin.show)

    ventana_tienda.senal_insuficiente.connect(ventana_insuficiente.show)

    ventana_inicio.mostrar()
    app.exec()
