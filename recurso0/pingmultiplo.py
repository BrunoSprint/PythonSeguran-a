import os
import time

# Abre o arquivo 'hosts.txt' para leitura
with open('hosts.txt') as file:
    # Lê o conteúdo do arquivo
    dump = file.read()
    
    # Divide as linhas do arquivo em uma lista
    dump = dump.splitlines()

    # Itera sobre cada IP na lista
    for ip in dump:
        print('Verificando o ip: ', ip)
        print("-" * 60)

        # Executa o comando 'ping' para verificar a conectividade com o IP
        os.system('ping -n 2 {}'.format(ip))

        print('-' * 60)

        # Aguarda 2 segundos antes de verificar o próximo IP
        time.sleep(2)
