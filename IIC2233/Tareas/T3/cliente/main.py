import socket
import sys
from PyQt5.QtWidgets import QApplication
from cliente import Cliente

if __name__ == "__main__":
    HOST = socket.gethostname()
    PORT = 9000

    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    CLIENTE = Cliente(HOST, PORT)

    app.exec()
