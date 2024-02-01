import socket

# Cria um objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket a um endereço e porta
server_socket.bind(('localhost', 12345))

# Coloca o servidor em modo de escuta
server_socket.listen(5)

while True:
    # Aguarda uma conexão
    client_socket, address = server_socket.accept()
    print(f"Conexão recebida de {address}")

    # Envia uma mensagem de volta para o cliente
    client_socket.send(b"Obrigado por se conectar!")

    # Fecha a conexão com o cliente
    client_socket.close()