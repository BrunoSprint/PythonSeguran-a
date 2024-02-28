'''
WebScraper coleta dados web, em forma de mineração que permite extração de dados de sites da web convertendo-os em 
informação estruturada para posterior análise.

bibliotecas:

BeautifulSoup: é uma biblioteca de extração de dados de arquivos html e xml.

Requests: permite que você envie solicitações em http em python.


'''

from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteudo da requisição http do site

soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html

print(soup.prettify())
#transforma html em string e o print vai exibir o html
'''
temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(temperatura.string)

print(soup.title.string)

print(soup.find('admin'))

#WebScraping é um analisador
'''