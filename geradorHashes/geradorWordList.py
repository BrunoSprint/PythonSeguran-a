'''
WORDLISTS, são arquivos contendo uma palavra por linha.
São ultilizados em ataques de força bruta com quebra de autenticação, pode ser usada para testar autenticação e confidencialidade.

Itertools - biblioteca que fornece condições para iterações como permutação e combinação.
Esta biblioteca será usada para gerar uma lista com vários caracteres diferente e sem repetições de palavras.

'''

import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string)) # caracteres combinaveis + numero de string
for i in resultado:
    print(''.join(i))




'''
import itertools

resultado = itertools.permutations('abcdef', 5)

for i in resultado:
    print(''.join(i))

'''