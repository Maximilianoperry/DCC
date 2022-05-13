import os
from random import randint


MIN_CARACTERES = 4
MAX_CARACTERES = 15
DURACION_RONDA_INICIAL = 90
POS_INICIO_ITEM = (randint(0, 1200), randint(0, 900), 10, 10)
PONDERACION_DIFICULTAD = 0.7
VELOCIDAD_CAMINAR = 20
PIXELES_SALTO = 50
VIDAS_INICIO = 5
VELOCIDAD_TRONCOS = 1
VELOCIDAD_AUTOS = 5
TIEMPO_TRONCOS = 1  # no son segundos, solo un parámetro
TIEMPO_AUTOS = 1
TIEMPO_OBJETO = 20
CANTIDAD_MONEDAS = 10

# paths
RUTA_LOGO = os.path.join("sprites", "Logo.png")
RUTA_PASTO = os.path.join("sprites", "Mapa", "areas", "pasto.png")
RUTA_RIO = os.path.join("sprites", "Mapa", "areas", "rio.png")
RUTA_CARRETERA = os.path.join("sprites", "Mapa", "areas", "carretera.png")
RUTA_CANCION = os.path.join("canciones", "musica.wav")
RUTA_RANA = os.path.join("sprites", "Personajes", "Verde", "still")

RUTA_UP1 = os.path.join("sprites", "Personajes", "Verde", "up_1")
RUTA_UP2 = os.path.join("sprites", "Personajes", "Verde", "up_2")
RUTA_UP3 = os.path.join("sprites", "Personajes", "Verde", "up_3")

RUTA_RIGHT1 = os.path.join("sprites", "Personajes", "Verde", "right_1")
RUTA_RIGHT2 = os.path.join("sprites", "Personajes", "Verde", "right_2")
RUTA_RIGHT3 = os.path.join("sprites", "Personajes", "Verde", "right_3")

RUTA_LEFT1 = os.path.join("sprites", "Personajes", "Verde", "left_1")
RUTA_LEFT2 = os.path.join("sprites", "Personajes", "Verde", "left_2")
RUTA_LEFT3 = os.path.join("sprites", "Personajes", "Verde", "left_3")

RUTA_DOWN1 = os.path.join("sprites", "Personajes", "Verde", "down_1")
RUTA_DOWN2 = os.path.join("sprites", "Personajes", "Verde", "down_2")
RUTA_DOWN3 = os.path.join("sprites", "Personajes", "Verde", "down_3")

RUTA_JUMP1 = os.path.join("sprites", "Personajes", "Verde", "jump_1")
RUTA_JUMP2 = os.path.join("sprites", "Personajes", "Verde", "jump_2")
RUTA_JUMP3 = os.path.join("sprites", "Personajes", "Verde", "jump_3")

RUTA_TRONCO = os.path.join("sprites", "Mapa", "elementos", "tronco.png")

RUTA_CALAVERA = os.path.join("sprites", "Objetos", "Calavera.png")
RUTA_CORAZON = os.path.join("sprites", "Objetos", "Corazon.png")
RUTA_MONEDA = os.path.join("sprites", "Objetos", "Moneda.png")
RUTA_RELOJ = os.path.join("sprites", "Objetos", "Reloj.png")

RUTA_AMARILLO_LEFT = os.path.join("sprites", "Mapa", "autos", "amarillo_left")
RUTA_AMARILLO_RIGHT = os.path.join("sprites", "Mapa", "autos", "amarillo_right")
RUTA_AZUL_LEFT = os.path.join("sprites", "Mapa", "autos", "azul_left")
RUTA_AZUL_RIGHT = os.path.join("sprites", "Mapa", "autos", "azul_right")
RUTA_BLANCO_LEFT = os.path.join("sprites", "Mapa", "autos", "blanco_left")
RUTA_BLANCO_RIGHT = os.path.join("sprites", "Mapa", "autos", "blanco_right")
RUTA_MORADO_LEFT = os.path.join("sprites", "Mapa", "autos", "morado_left")
RUTA_MORADO_RIGHT = os.path.join("sprites", "Mapa", "autos", "morado_right")
RUTA_NEGRO_LEFT = os.path.join("sprites", "Mapa", "autos", "negro_left")
RUTA_NEGRO_RIGHT = os.path.join("sprites", "Mapa", "autos", "negro_right")
RUTA_PLATA_LEFT = os.path.join("sprites", "Mapa", "autos", "plata_left")
RUTA_PLATA_RIGHT = os.path.join("sprites", "Mapa", "autos", "plata_right")
RUTA_ROJO_LEFT = os.path.join("sprites", "Mapa", "autos", "rojo_left")
RUTA_ROJO_RIGHT = os.path.join("sprites", "Mapa", "autos", "rojo_right")

lista_aleatorios_1 = [- 10, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160]
lista_aleatorios_2 = [290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790]
lista_troncos = [- 600, - 550, - 500, - 450, - 400, - 350, - 300, -250]
lista_troncos2 = [1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700]
lista_autos = [- 780, - 730, - 680, - 630, - 450, - 400, - 350, - 300, -250]
lista_autos2 = [1350, 1400, 1450, 1500, 1680, 1730, 1780, 1830, 1880]

# skin roja
RUTA_RANA_ROJA = os.path.join("sprites", "Personajes", "Rojo", "still")

RUTA_UP1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "up_1")
RUTA_UP2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "up_2")
RUTA_UP3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "up_3")

RUTA_RIGHT1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "right_1")
RUTA_RIGHT2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "right_2")
RUTA_RIGHT3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "right_3")

RUTA_LEFT1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "left_1")
RUTA_LEFT2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "left_2")
RUTA_LEFT3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "left_3")

RUTA_DOWN1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "down_1")
RUTA_DOWN2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "down_2")
RUTA_DOWN3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "down_3")

RUTA_JUMP1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "jump_1")
RUTA_JUMP2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "jump_2")
RUTA_JUMP3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "jump_3")

#  skin naranja
RUTA_RANA_NARANJA = os.path.join("sprites", "Personajes", "Naranjo", "still")

RUTA_UP1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "up_1")
RUTA_UP2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "up_2")
RUTA_UP3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "up_3")

RUTA_RIGHT1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "right_1")
RUTA_RIGHT2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "right_2")
RUTA_RIGHT3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "right_3")

RUTA_LEFT1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "left_1")
RUTA_LEFT2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "left_2")
RUTA_LEFT3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "left_3")

RUTA_DOWN1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "down_1")
RUTA_DOWN2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "down_2")
RUTA_DOWN3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "down_3")

RUTA_JUMP1_ROJO = os.path.join("sprites", "Personajes", "Rojo", "jump_1")
RUTA_JUMP2_ROJO = os.path.join("sprites", "Personajes", "Rojo", "jump_2")
RUTA_JUMP3_ROJO = os.path.join("sprites", "Personajes", "Rojo", "jump_3")
