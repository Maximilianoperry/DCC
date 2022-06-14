from os import truncate
import threading
import socket
import json
import funciones as f
from random import randint


class Servidor:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.clientes_conectados = [["", "-", "", "", "", ""], ["", "-", "", "", "", ""], ["", "-", "", "", "", ""], ["", "-", "", "", "", ""]]
        self.id_cliente = 0

        print(f'Servidor escuchando en {self.host}:{self.port}')

        thread = threading.Thread(target=self.aceptar_clientes)
        thread.start()

    def aceptar_clientes(self):
        while True:
            try:
                socket_cliente, address = self.socket_servidor.accept()
                self.clientes_conectados[self.id_cliente] = [socket_cliente, self.id_cliente]
                print(f'Cliente con dirección {address} se ha conectado al servidor')
                thread_cliente = threading.Thread(target=self.escuchar_cliente, args=(socket_cliente,), daemon=True)
                thread_cliente.start()
            except IndexError:
                self.enviar("[LLENO]", socket_cliente)

    def escuchar_cliente(self, socket_cliente):
        try:
            while True:
                mensaje = self.recibir(socket_cliente)
                respuesta = self.manejar_mensaje_recibido(mensaje)
                print(f'Enviando respuesta: {respuesta}')
                self.enviar(respuesta, socket_cliente)
        except ConnectionResetError:
            print('Error de conexión con el cliente')

    def recibir(self, socket_cliente):
        largo_bytes_mensaje = socket_cliente.recv(4)
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder='little')
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            bytes_mensaje += socket_cliente.recv(80)
        bytes_mensaje_limpios = bytes_mensaje.strip(b'\x00')
        mensaje = self.decodificar_mensaje(bytes_mensaje_limpios)
        return mensaje

    def enviar(self, mensaje, socket_cliente):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        while len(bytes_mensaje) % 80 != 0:
            bytes_mensaje += b'\x00'
        largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder='little')
        socket_cliente.sendall(largo_bytes_mensaje + bytes_mensaje)

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
            contador = "0"  # si se envian bytes grandes, sumarle 1
            largo_bytes_mensaje = len(contador.encode("utf-8")).to_bytes(4, byteorder='big')
            return largo_bytes_mensaje + mensaje_bytes

        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje')
            return b''

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje_acortado = bytes_mensaje[:len(bytes_mensaje) - 1]
            filtrado_bytes = b''
            agregar = False
            for i in range(len(mensaje_acortado)):
                if mensaje_acortado[i:i + 1] == b'[':
                    agregar = True
                if agregar:
                    if mensaje_acortado[i:i + 1] == b'3':
                        filtrado_bytes += b'5'
                    elif mensaje_acortado[i:i + 1] == b'5':
                        filtrado_bytes += b'3'
                    else:
                        filtrado_bytes += mensaje_acortado[i:i + 1]
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
        if f.leer_tipo_mensaje(mensaje) == "USUARIO":
            mensaje = mensaje[9:]
            if f.revisar_repetidos(mensaje) is True:
                print("USUARIO REPETIDO")
                self.enviar("[RUSUARIO]FALSE", self.clientes_conectados[self.id_cliente][0])
                # envío mensaje que el usuario es inválido
            else:
                self.clientes_conectados[self.id_cliente] += [str(mensaje)]
                f.agregar_participante(mensaje)
                info_enviar = "[RUSUARIO]TRUE" + str(mensaje)
                self.enviar(info_enviar, self.clientes_conectados[self.id_cliente][0])
                # se envian todos los jugadores registrados hasta el momento
                jug1 = str(0) + str(self.clientes_conectados[0][2])
                jug2 = str(1) + str(self.clientes_conectados[1][2])
                jug3 = str(2) + str(self.clientes_conectados[2][2])
                jug4 = str(3) + str(self.clientes_conectados[3][2])
                jugadores = f"{jug1}-{jug2}-{jug3}-{jug4}"
                sockets_existentes = []
                for dato in self.clientes_conectados:
                    if dato[1] != '-':
                        sockets_existentes += [dato]
                for sock in sockets_existentes:
                    self.enviar(jugadores, sock[0])
                self.id_cliente += 1
        if f.leer_tipo_mensaje(mensaje) == "RETO":
            mensaje = mensaje[6:]
            retador = mensaje.split("-")[0]
            retado = mensaje.split("-")[1]
            for dato in self.clientes_conectados:
                if dato[2] == retador:
                    socket_retador = dato[0]
                if dato[2] == retado:
                    socket_retado = dato[0]
            msg_retado = "[RETO]" + str(retador)
            self.enviar(msg_retado, socket_retado)
        if f.leer_tipo_mensaje(mensaje) == "RRETO":  # rechazar reto
            mensaje = mensaje[7:]
            respuesta = mensaje.split("-")[0]
            retador = mensaje.split("-")[1]
            for dato in self.clientes_conectados:
                if dato[2] == retador:
                    socket_retador = dato[0]
            if respuesta == "RECHAZADO":
                self.enviar("[RRETO]Rechazado", socket_retador)
        if f.leer_tipo_mensaje(mensaje) == "RACEP":  # aceptar reto
            mensaje = mensaje[7:]
            respuesta = mensaje.split("-")[0]
            retador = mensaje.split("-")[1]
            retado = mensaje.split("-")[2]
            for dato in self.clientes_conectados:
                if dato[2] == retador:
                    socket_retador = dato[0]
                if dato[2] == retado:
                    socket_retado = dato[0]
            if respuesta == "ACEPTADO":
                primero = randint(0, 1)
                msg_reto_orden = f"[RACEP]{retador}-{retado}-{primero}"
                self.enviar(msg_reto_orden, socket_retador)
                self.enviar(msg_reto_orden, socket_retado)
                # se actualiza la lista para que funcione durante el juego
                for i in range(len(self.clientes_conectados)):
                    self.clientes_conectados[i] += "", "", "WAIT"
        if f.leer_tipo_mensaje(mensaje) == "PARTIDA":  # rondas partida
            mensaje = mensaje[9:]
            es_par = mensaje.split("-")[0]
            num_apostado = mensaje.split("-")[1]
            apostador = mensaje.split("-")[2]
            rival = mensaje.split("-")[3]
            canicas = mensaje.split("-")[4]
            for dato in self.clientes_conectados:
                if dato[2] == apostador:
                    id_apostador = dato[1]
                    socket_apostador = dato[1]
                if dato[2] == rival:
                    id_rival = dato[1]
                    socket_rival = dato[0]
            self.clientes_conectados[id_apostador][3] = es_par
            self.clientes_conectados[id_apostador][4] = num_apostado
            self.clientes_conectados[id_apostador][5] = "PLAY"
            self.clientes_conectados[id_apostador] += [canicas]

            if self.clientes_conectados[id_rival][5] == "PLAY":
                canicas__totales_apostador = int(self.clientes_conectados[id_apostador][6])
                par_apostador = self.clientes_conectados[id_apostador][3]
                num_canicas_apostador = int(self.clientes_conectados[id_apostador][4])
                canicas_totales_rival = int(self.clientes_conectados[id_rival][6])
                par_rival = self.clientes_conectados[id_apostador][3]
                num_canicas_rival = int(self.clientes_conectados[id_apostador][4])
                revisar_apostador = True
                revisar_rival = True

                # apostador
                if par_apostador == "par" and int(num_canicas_rival)//2 == 0 and revisar_apostador is True:
                    print(f"GANÓ {self.clientes_conectados[id_apostador][2]}")
                    canicas__totales_apostador += num_canicas_rival
                    print(f"CANICAS TOTALES: {canicas__totales_apostador}")
                    num_canicas_apostador_antes_operacion = num_canicas_rival
                    num_canicas_rival_antes_operacion = num_canicas_rival
                    canicas_totales_rival -= num_canicas_rival
                    print(f"CANICAS TOTALES OPONENTE: {canicas_totales_rival}")
                    revisar_apostador = False

                if par_apostador == "par" and int(num_canicas_rival)//2 == 1 and revisar_apostador is True:
                    print(f"PERDIÓ {self.clientes_conectados[id_apostador][2]}")
                    canicas__totales_apostador -= num_canicas_apostador
                    print(f"CANICAS TOTALES: {canicas__totales_apostador}")
                    num_canicas_rival_antes_operacion = num_canicas_rival
                    canicas_totales_rival += num_canicas_apostador
                    print(f"CANICAS TOTALES OPONENTE: {canicas_totales_rival}")
                    revisar_apostador = False

                if par_apostador == "impar" and int(num_canicas_rival)//2 == 0 and revisar_apostador is True:
                    print(f"PERDIÓ {self.clientes_conectados[id_apostador][2]}")
                    canicas__totales_apostador -= num_canicas_apostador
                    print(f"CANICAS TOTALES: {canicas__totales_apostador}")
                    num_canicas_rival_antes_operacion = num_canicas_rival
                    canicas_totales_rival += num_canicas_apostador
                    print(f"CANICAS TOTALES OPONENTE: {canicas_totales_rival}")
                    revisar_apostador = False

                if par_apostador == "impar" and int(num_canicas_rival)//2 == 1 and revisar_apostador is True:
                    print(f"GANÓ {self.clientes_conectados[id_apostador][2]}")
                    canicas__totales_apostador += num_canicas_rival
                    print(f"CANICAS TOTALES: {canicas__totales_apostador}")
                    num_canicas_rival_antes_operacion = num_canicas_rival
                    canicas_totales_rival -= num_canicas_rival
                    print(f"CANICAS TOTALES OPONENTE: {canicas_totales_rival}")
                    revisar_apostador = False

                # rival
                if par_rival == "par" and int(num_canicas_apostador)//2 == 0 and revisar_rival is True:
                    print(f"GANÓ {self.clientes_conectados[id_rival][2]}")
                    canicas_totales_rival += num_canicas_apostador
                    print(f"CANICAS TOTALES: {canicas_totales_rival}")
                    canicas__totales_apostador -= num_canicas_apostador
                    print(f"CANICAS TOTALES OPONENTE: {canicas__totales_apostador}")
                    revisar_rival = False

                if par_rival == "par" and int(num_canicas_apostador)//2 == 1 and revisar_rival is True:
                    print(f"PERDIÓ {self.clientes_conectados[id_rival][2]}")
                    canicas_totales_rival -= num_canicas_rival
                    print(f"CANICAS TOTALES: {canicas_totales_rival}")
                    canicas__totales_apostador += num_canicas_rival
                    print(f"CANICAS TOTALES OPONENTE: {canicas__totales_apostador}")
                    revisar_rival = False

                if par_rival == "impar" and int(num_canicas_apostador)//2 == 0 and revisar_rival is True:
                    print(f"PERDIÓ {self.clientes_conectados[id_rival][2]}")
                    canicas_totales_rival -= num_canicas_rival
                    print(f"CANICAS TOTALES: {canicas_totales_rival}")
                    canicas__totales_apostador += num_canicas_rival
                    print(f"CANICAS TOTALES OPONENTE: {canicas__totales_apostador}")
                    revisar_rival = False

                if par_rival == "impar" and int(num_canicas_apostador)//2 == 1 and revisar_rival is True:
                    print(f"GANÓ {self.clientes_conectados[id_rival][2]}")
                    canicas_totales_rival += num_canicas_apostador
                    print(f"CANICAS TOTALES: {canicas_totales_rival}")
                    canicas__totales_apostador -= num_canicas_apostador
                    print(f"CANICAS TOTALES OPONENTE: {canicas__totales_apostador}")
                    revisar_rival = False
                # juego terminado (alguno queda con 0 canicas)

                # volver a como estaba

        return f'Respuesta asociada al mensaje "{mensaje}"'
