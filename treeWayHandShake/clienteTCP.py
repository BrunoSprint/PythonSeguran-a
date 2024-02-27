import socket
import sys

# Função principal que realiza a conexão TCP com um host e porta específicos
def main():
    try:
        # Cria um socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    # Solicita ao usuário que insira o Host e a Porta para a conexão
    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        # Tenta conectar ao host e porta especificados
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: " + HostAlvo + " e na Porta: " + PortaAlvo)
    except socket.error as e:
        # Em caso de falha na conexão, exibe uma mensagem de erro
        print("Não foi possível conectar no Host: " + HostAlvo + " - Porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()




