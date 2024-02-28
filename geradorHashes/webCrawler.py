''' WebCrawler : Ferramenta usada para encontrar, ler e indexar páginas. capitura informações de cada um dos links que encontra
pela frente, cadastra e compreende o que é mais relevante.(palavras-chaves)

Muito Utilizado em levantamento de informações em um PENTEST.


bibliotecas:

BeautifulSoup - biblioteca de extração de dados de arquivos HTML e XML.

operator - exporta um conjunto de funções eficientes correspondentes aos operadores intrínsecos do Python como: +-*/ not and

collections - nos ajuda a preencher e manipular eficientemente as estruturas de dados como tuplas, dicionários e listas.



'''

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    # Lista para armazenar as palavras extraídas da página web
    wordlist = []
    
    # Obtém o código-fonte HTML da URL fornecida
    source_code = requests.get(url).text
    
    # Utiliza BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(source_code, 'html.parser')

    # O texto na página web é armazenado sob as tags div com a classe 'entry-content'
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        # Converte o conteúdo para minúsculas e divide em palavras
        words = content.lower().split()

        # Adiciona cada palavra à lista de palavras
        for each_word in words:
            wordlist.append(each_word)
        
        # Chama a próxima função para limpar a lista de palavras
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    # Lista para armazenar as palavras limpas
    clean_list = []
    
    # Itera sobre cada palavra na lista
    for word in wordlist:
        # Define os caracteres especiais a serem removidos
        symbols = '!@#$%¨&*()_-+={[]}|\;:"<>?/., '

        # Remove os caracteres especiais de cada palavra
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        # Adiciona a palavra à lista limpa se tiver comprimento maior que 0
        if len(word) > 0:
            clean_list.append(word)
    
    # Chama a próxima função para criar o dicionário de contagem
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    # Dicionário para armazenar a contagem de cada palavra
    word_count = {}

    # Itera sobre cada palavra na lista limpa
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Imprime as palavras e suas contagens, ordenadas por contagem
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print("%s: %s" % (key, value))

    # Utiliza Counter para encontrar as 10 palavras mais comuns e as imprime
    c = Counter(word_count)
    top = c.most_common(10)
    print(top)

# Ponto de entrada do programa
if __name__ == '__main__':
    # Chama a função principal com a URL fornecida
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")

















