import socket # Proporciona la funcionalidad que permite realizar interacciones por medio de sockets
import threading # Maneja las conexiones de los clientes, es decir, los usuarios que ingresan

# Configuración del servidor
HOST = '127.0.0.1' # Establece la dirección IP en la que el servidor escuchará (localhost en este caso)
PORT = 3030 # Establece el puerto en el que el servidor escuchará

# Lista de usuarios conectados
usuarios_conectados = ["Poli01", "Poli02", "Poli03"] # Inicializa una lista con algunos nombres de usuario

# Función para manejar la conexión de un cliente
def manejar_cliente(client_socket):
    # Recibe el nombre de usuario del cliente
    nombre_usuario = client_socket.recv(1024).decode()
    usuarios_conectados.append(nombre_usuario) # Agrega el nombre de usuario a la lista de usuarios conectados

    print(f'Usuario "{nombre_usuario}" conectado')

    while True:
        mensaje = client_socket.recv(1024).decode() # Recibe mensajes del cliente
        if mensaje == "chao":
            print(f'El usuario "{nombre_usuario}" abandonó')
            usuarios_conectados.remove(nombre_usuario) # Elimina al usuario de la lista de usuarios conectados cuando se desconecta
            break
        else:
            print(f'{nombre_usuario}: {mensaje}')
            # Envía el mensaje a todos los usuarios conectados excepto al remitente
            for usuario in usuarios_conectados:
                if usuario != nombre_usuario:
                    enviar_mensaje = f'{nombre_usuario}: {mensaje}'
                    client_socket.send(enviar_mensaje.encode())

    client_socket.close()

# Función principal del servidor
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un socket de servidor
    server.bind((HOST, PORT)) # Enlaza el servidor a la dirección IP y puerto especificados
    server.listen(5) # Escucha hasta 5 conexiones entrantes
    print('Servidor iniciado y contestando ok, PUERTO ' + str(PORT))

    while True:
        client_socket, addr = server.accept() # Acepta una conexión entrante desde un cliente
        cliente_thread = threading.Thread(target=manejar_cliente, args=(client_socket,)) # Crea un nuevo hilo para manejar al cliente
        cliente_thread.start() # Inicia el hilo para atender al cliente

if __name__ == '__main__':
    main() # Inicia la función principal del servidor cuando se ejecuta el script
