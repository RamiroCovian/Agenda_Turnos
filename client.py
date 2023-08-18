########################################################################################
####################################### CLIENTE ########################################
########################################################################################

"""
client.py:
    Configuracion del cliente para la comunicacion con el server.
"""

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.13"
port = 9999
clientsocket.connect((host, port))
mensaje = clientsocket.recv(1024)
print(mensaje.decode("UTF-8"))

clientsocket.close()
