'''
Desenvolvendo um Ocultador de arquivos.

'''


import ctypes

pasta = input("Digite o Caminho da Pasta a ser Ocultada ex (C:/pasta): ")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)   #'ocultar.txt'

if retorno: 
    print("pasta foi Ocultado")                #arquivo
else:
    print("pasta não Foi Ocultado")            #arquivo

