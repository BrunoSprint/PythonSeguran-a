import socket

# Cria um socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Exibe mensagem indicando que o cliente socket foi criado com sucesso
print('Cliente Socket Criado com Sucesso!!!')

# Define o endereço do servidor (localhost) e a porta a ser utilizada
host = 'localhost'
porta = 5432

# Define a mensagem a ser enviada ao servidor
mensagem = 'Olá Servidor'

try:
    # Exibe a mensagem que será enviada ao servidor
    print('Cliente:' + mensagem)

    # Envia a mensagem codificada para o servidor no endereço especificado
    s.sendto(mensagem.encode(), (host, porta))

    # Recebe dados do servidor (4096 bytes)
    dados, servidor = s.recvfrom(4096)

    # Decodifica os dados recebidos e exibe a mensagem do servidor
    dados = dados.decode()
    print("Cliente: " + dados)

finally:
    # Exibe mensagem indicando o fechamento da conexão
    print('Cliente: Fechando a Conexão')

    # Fecha o socket
    s.close()
