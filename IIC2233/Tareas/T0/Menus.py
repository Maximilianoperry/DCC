from datetime import time
class Menu:
    def __init__(self):
        tiempo = []
    def impresion(self):
        print(""" 
               ****** Menú Inicio ******
        
               [1] Ingresar sesión
               [2] Registrar usuario
               [3] Ingresar como usuario anónimo
               [x] Salir
         """)

    def impr_men_pri(self):
        print("""
               ****** Menú Principal ******
        
               [1] Menú de Publicaciones
               [2] Menú de Publicaciones Realizadas
               [x] Volver
         """)
