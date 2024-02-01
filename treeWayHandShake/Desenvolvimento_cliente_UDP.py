import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # IPV4 e UDP 


print('Cliente Socket Criado com Sucesso!!!')

host = 'localhost'
porta = 5433    #porta de conexão
mensagem = 'Olá Servidor'

try:
    print( 'Cliente:' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

dados, servidor = s.recvfrom(4096)
dados = dados.decode()
print("Cliente: " + dados)

finally:
    print('Cliente: Fechando a Conexão')
    s.close()


# tree-way-handshake


