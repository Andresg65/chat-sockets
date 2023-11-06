import socket  # Importa el módulo socket para la comunicación en red

HOST = '127.0.0.1'  # Establece la dirección IP del servidor al que el cliente se conectará (localhost en este caso)
PORT = 3030  # Establece el puerto del servidor al que el cliente se conectará

nombre_usuario = input('Ingrese su nombre de usuario: ')  # Solicita al usuario que ingrese un nombre de usuario

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket de cliente

# Conecta el socket del cliente al servidor usando la dirección IP y el puerto
client_socket.connect((HOST, PORT))
client_socket.send(nombre_usuario.encode())  # Envía el nombre de usuario al servidor

while True:
    mensaje = input()  # Espera a que el usuario ingrese un mensaje desde la consola
    client_socket.send(mensaje.encode())  # Envía el mensaje al servidor

    if mensaje == "chao":  # Si el usuario ingresa "chao", termina el bucle
        break

client_socket.close()  # Cierra el socket del cliente al salir del bucle