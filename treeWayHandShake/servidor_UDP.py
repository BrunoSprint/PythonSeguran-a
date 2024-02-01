import socket

s = socket.socket(socket.AF.INET, socket.SOCK_DGRAM)

print('Socket Criado com Sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = 'Servidor: Olá Cliente!!!'

while 1:
    dados, endereco = s.recvfrom(4096)

if dados:
    print('Servidor Enviando Mensagem...')
    s.sendto(dados + (mensagem.encode()), end)

