import hashlib

# Define os nomes dos arquivos a serem comparados
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

# Cria objetos de hash usando o algoritmo de hash RIPEMD-160
hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

# Calcula o hash do conteúdo do arquivo1 e atualiza o objeto hash1
hash1.update(open(arquivo1, 'rb').read())

# Calcula o hash do conteúdo do arquivo2 e atualiza o objeto hash2
hash2.update(open(arquivo2, 'rb').read())

# Compara os hashes digest para verificar se os arquivos são iguais
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2} ')
else:
    print(f'O arquivo : {arquivo1} é igual ao arquivo: {arquivo2} ')
