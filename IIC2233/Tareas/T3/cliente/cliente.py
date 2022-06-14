import socket
import threading
import json
from interfaz import Controlador

# parámetros
with open("parametros.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

HOST = jsonObject['host']
PUERTO = jsonObject['port']


class Cliente:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nombre_cliente = ""

        self.controlador = Controlador(self)
        self.controlador.ofrecer_reto_signal.connect(self.enviar_info_reto)
        self.controlador.enviar_info_juego_cliente_signal.connect(self.enviar_info_juego)

        try:
            self.controlador.mostrar_login()
            self.socket_cliente.connect((self.host, self.port))
            thread = threading.Thread(target=self.escuchar_servidor, daemon=True)
            thread.start()
        except ConnectionRefusedError:
            self.socket_cliente.close()

    def recibir_mensaje(self, mensaje):
        print(f'Enviando mensaje: {mensaje}')
        self.enviar(mensaje)

    def escuchar_servidor(self):
        try:
            while True:
                mensaje = self.recibir()
                print(f'Mensaje recibido: {mensaje}')
                self.manejar_mensaje_recibido(mensaje)
        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            self.socket_cliente.close()

    def recibir(self):
        largo_bytes_mensaje = self.socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='little')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            bytes_mensaje += self.socket_cliente.recv(80)
        bytes_mensaje_limpios = bytes_mensaje.strip(b'\x00')
        mensaje = self.decodificar_mensaje(bytes_mensaje_limpios)
        return mensaje

    def enviar(self, mensaje):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        while len(bytes_mensaje) % 80 != 0:
            bytes_mensaje += b'\x00'
        largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='little')
        # print(f"Enviando bytes: {largo_bytes_mensaje + bytes_mensaje}")
        self.socket_cliente.sendall(largo_bytes_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        try:
            n = 0
            X = mensaje.encode('UTF-8')
            A = b''
            B = b''
            C = b''
            for i in range(0, len(X), 3):
                A += X[i:i + 1]
            for i in range(1, len(X), 3):
                B += X[i:i + 1]
            for i in range(2, len(X), 3):
                C += X[i:i + 1]
            if B[0] >= C[0]:
                n = 0
            elif B[0] < C[0]:
                n = 1
            suma = A + B + C
            mensaje_bytes = b''
            for i in range(len(suma)):
                if suma[i:i+1] == b'3':
                    mensaje_bytes += b'5'
                elif suma[i:i+1] == b'5':
                    mensaje_bytes += b'3'
                else:
                    mensaje_bytes += suma[i:i + 1]
            if n == 1:
                mensaje_bytes += b'1'
            elif n == 0:
                mensaje_bytes += b'0'
            # print(mensaje_bytes)
            contador = "0"  # si se envian bytes grandes, sumarle 1
            largo_bytes_mensaje = len(contador.encode("utf-8")).to_bytes(4, byteorder='big')
            return largo_bytes_mensaje + mensaje_bytes

        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje')
            return b''

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            # print(f"Bytes recibidos:{bytes_mensaje}")
            filtrado_bytes = b''
            for i in range(len(bytes_mensaje)):
                if bytes_mensaje[i:i + 1] == b'3':
                    filtrado_bytes += b'5'
                elif bytes_mensaje[i:i + 1] == b'5':
                    filtrado_bytes += b'3'
                else:
                    filtrado_bytes += bytes_mensaje[i:i + 1]
            filtrado_bytes = filtrado_bytes[1:len(filtrado_bytes) - 1]
            rango = len(filtrado_bytes)//3
            bytes_ordenados = b''
            if len(filtrado_bytes) % 3 == 1:
                for i in range(0, rango, 1):
                    bytes_ordenados += filtrado_bytes[i:i + 1]
                    bytes_ordenados += filtrado_bytes[i + rango + 1:i + rango + 2]
                    bytes_ordenados += filtrado_bytes[i + 2*rango + 1:i + 2*rango + 2]
                bytes_ordenados += filtrado_bytes[rango:rango + 1]
            elif len(filtrado_bytes) % 3 == 2:
                for i in range(0, rango + 1, 1):
                    bytes_ordenados += filtrado_bytes[i:i + 1]
                    bytes_ordenados += filtrado_bytes[i + rango + 1:i + rango + 2]
                    bytes_ordenados += filtrado_bytes[i + 2*rango + 2:i + 2*rango + 3]
            else:
                for i in range(0, rango, 1):
                    bytes_ordenados += filtrado_bytes[i:i + 1]
                    bytes_ordenados += filtrado_bytes[i + rango:i + rango + 1]
                    bytes_ordenados += filtrado_bytes[i + 2*rango:i + 2*rango + 1]
            mensaje = bytes_ordenados.decode("UTF-8")
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje')
            return ''

    def manejar_mensaje_recibido(self, mensaje):
        codigo_mensaje = ""
        estado = ""
        if mensaje[0] == "[":  # ventana inicio
            agregar = True
            for letra in mensaje[1:]:
                if letra == "]":
                    agregar = False
                if agregar is True:
                    codigo_mensaje += letra
                if agregar is False:
                    estado += letra
            nombre = estado[5:]
            estado = estado[1:5]
            if mensaje[1:6] == "LLENO":  # servidor lleno
                self.controlador.ventana_inicio.edit_usuario.setText("")
                self.controlador.ventana_inicio.edit_usuario.setPlaceholderText("SERVIDOR LLENO")
                self.controlador.ventana_inicio.edit_nacimiento.setText("")
                self.controlador.ventana_inicio.edit_nacimiento.setPlaceholderText("NO PODRÁS INGRESAR")

            if mensaje[1:5] == "RETO":  # sala principal
                retador = mensaje[5:]
                self.controlador.mostrar_ventana_reto_signal.emit(retador)
            if mensaje[1:6] == "RRETO": # ventana invitacion
                self.controlador.mostrar_rechazo_invitacion()
            if mensaje[1:6] == "RACEP":
                self.controlador.aceptar_invtiacion(mensaje[7:])
        if codigo_mensaje == "RUSUARIO":  # ventana inicio
            if estado == "TRUE":
                print("USUARIO VERIFICADO")
                self.controlador.mostrar_ventana_principal_signal.emit()
                self.nombre_cliente = str(nombre)
            else:
                print("USUARIO INVÁLIDO")
                self.controlador.label_usuario()
        if str(mensaje[0]) == "0" or str(mensaje[0]) == "1" or str(mensaje[0]) == "2" or str(mensaje[0]) == "3":  # sala principal
            mensaje_separado = mensaje.split("-")
            # checks para verificar si se llenaron los cupos
            check_jug1 = False
            check_jug2 = False
            check_jug3 = False
            check_jug4 = False
            # se actualizan los labels
            if len(mensaje_separado[0]) != 1:
                check_jug1 = True
                self.controlador.sala_principal.jug_1.setText(f"1. {mensaje_separado[0][1:]}")
                self.controlador.sala_principal.jug_1.setStyleSheet("border-radius: 2px;"
                                                                    "color: white")
            if len(mensaje_separado[1]) != 1:
                check_jug2 = True
                self.controlador.sala_principal.jug_2.setText(f"2. {mensaje_separado[1][1:]}")
                self.controlador.sala_principal.jug_2.setStyleSheet("border-radius: 2px;"
                                                                    "color: white")
            if len(mensaje_separado[2]) != 1:
                check_jug3 = True
                self.controlador.sala_principal.jug_3.setText(f"3. {mensaje_separado[2][1:]}")
                self.controlador.sala_principal.jug_3.setStyleSheet("border-radius: 2px;"
                                                                    "color: white")
            if len(mensaje_separado[3]) != 1:
                check_jug4 = True
                self.controlador.sala_principal.jug_4.setText(f"4. {mensaje_separado[3][1:]}")
                self.controlador.sala_principal.jug_4.setStyleSheet("border-radius: 2px;"
                                                                    "color: white")
            if check_jug1 is True and check_jug2 is True and check_jug3 is True and check_jug4 is True:
                self.controlador.crear_retos_signal.emit(self.nombre_cliente)
        print(f'Acción asociada al mensaje: {mensaje}')

    def enviar_info_reto(self, info):
        self.enviar(info)

    def enviar_info_juego(self, info):
        self.enviar(info)
