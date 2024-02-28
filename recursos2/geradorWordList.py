'''
WORDLISTS, são arquivos contendo uma palavra por linha.
São ultilizados em ataques de força bruta com quebra de autenticação, pode ser usada para testar autenticação e confidencialidade.

Itertools - biblioteca que fornece condições para iterações como permutação e combinação.
Esta biblioteca será usada para gerar uma lista com vários caracteres diferente e sem repetições de palavras.

'''

# Importa a biblioteca itertools, que fornece ferramentas para criar iteradores para operações eficientes em combinações e permutações.
import itertools

# Solicita ao usuário que insira a string a ser permutada.
string = input("String a ser permutada: ")

# Utiliza a função permutations do itertools para gerar todas as permutações da string.
# O segundo argumento é o comprimento das permutações, que é definido como o comprimento da string.
resultado = itertools.permutations(string, len(string))

# Itera sobre as permutações geradas e imprime cada permutação.
for i in resultado:
    # Utiliza ''.join(i) para unir os caracteres da tupla de permutação em uma string.
    print(''.join(i))





'''
import itertools

resultado = itertools.permutations('abcdef', 5)

for i in resultado:
    print(''.join(i))

'''