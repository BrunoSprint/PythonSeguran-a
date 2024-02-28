# Importa a biblioteca hashlib, que fornece algoritmos de hash seguros.
import hashlib

# Solicita ao usuário que insira o texto a ser gerado o hash.
string = input("Digite o texto a ser gerado a hash: ")

# Apresenta um menu para o usuário escolher o tipo de hash a ser gerado.
menu = int(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
                 1) MD5
                 2) SHA1
                 3) SHA256
                 4) SHA512
                 Digite o número do hash a ser gerado: '''))

# Verifica a escolha do usuário e calcula a hash correspondente.
if menu == 1:
    # Utiliza o algoritmo MD5 para calcular a hash.
    resultado = hashlib.md5(string.encode('utf-8'))
    # Imprime a hash MD5 resultante.
    print('A hash MD5 da string:', string, 'é:', resultado.hexdigest())
elif menu == 2:
    # Utiliza o algoritmo SHA-1 para calcular a hash.
    resultado = hashlib.sha1(string.encode('utf-8'))
    # Imprime a hash SHA-1 resultante.
    print('A hash SHA1 da string:', string, 'é:', resultado.hexdigest())
elif menu == 3:
    # Utiliza o algoritmo SHA-256 para calcular a hash.
    resultado = hashlib.sha256(string.encode('utf-8'))
    # Imprime a hash SHA-256 resultante.
    print('A hash SHA256 da string:', string, 'é:', resultado.hexdigest())
elif menu == 4:
    # Utiliza o algoritmo SHA-512 para calcular a hash.
    resultado = hashlib.sha512(string.encode('utf-8'))
    # Imprime a hash SHA-512 resultante.
    print('A hash SHA512 da string:', string, 'é:', resultado.hexdigest())
else:
    # Se o usuário inserir uma escolha inválida, exibe uma mensagem de erro.
    print('Algo de errado não está certo, tente novamente.')

