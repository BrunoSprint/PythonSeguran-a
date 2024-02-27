import socket

# Cria um socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Exibe mensagem indicando que o servidor socket foi criado com sucesso
print('Socket Criado com Sucesso')

# Define o endereço do servidor (localhost) e a porta a ser utilizada
host = 'localhost'
porta = 432

# Associa o socket a um endereço e porta
s.bind((host, porta))

# Define a mensagem que o servidor enviará ao cliente
mensagem = 'Servidor: Olá Cliente!!!'

while True:
    # Recebe dados e o endereço do cliente
    dados, endereco = s.recvfrom(4096)

    # Verifica se há dados
    if dados:
        print('Servidor Enviando Mensagem...')
        # Envia os dados recebidos de volta para o cliente, adicionando a mensagem do servidor
        s.sendto(dados + mensagem.encode(), endereco)


