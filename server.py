########################################################################################
####################################### SERVER #########################################
########################################################################################

"""
server.py:
    Configuracion del servidor para la comunicacion con el cliente. Envia mensaje de bienvenida al sevidor cuando se genera la conexion.
"""


import socket


def start_server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.1.13"  # Esta es la IP del servidor
    port = 9999  # Puerto en el cual estoy escuchado
    print("Abriendo servidor desde: ", host)
    serversocket.bind((host, port))
    serversocket.listen(3)
    while True:
        # Inicia la conexión
        clientsocket, address = serversocket.accept()
        print(type(address))
        # address es una tupla de dos valores
        print(0, '---', address[0])  # Dirección IP
        print(1, '---', address[1])  # Número de conexión

        print("Recibo la conexión desde: " + str(address[0]))
        # Mensaje Enviado
        mensaje = b'Hola Bienvenido a nuestro servidor' + b'\r\n'
        clientsocket.send(mensaje)
        clientsocket.close()
