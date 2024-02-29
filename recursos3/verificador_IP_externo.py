'''

bibliotecas:

re - Permite operações com expressões regulares.

json - Fornece operação de codificação e decodificação JSON

urllib.request import urlopen - Funções e classes que ajudam a abrir URLs

http://ipinfo.io/json   checagem de ip.

'''

import re
import json
from urllib.request import urlopen


url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print('IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrg.: {0}'.format(org,regiao,pais,cid,ip))

'''
import re
import json
from urllib.request import urlopen

# Define a URL de onde os dados JSON serão obtidos
url = 'https://ipinfo.io/json'

# Abre a conexão com a URL e obtém a resposta
with urlopen(url) as resposta:
    # Carrega os dados JSON da resposta
    dados = json.load(resposta)

# Extrai as informações relevantes do dicionário de dados
ip = dados.get('ip', 'N/A')
org = dados.get('org', 'N/A')
cid = dados.get('city', 'N/A')
pais = dados.get('country', 'N/A')
regiao = dados.get('region', 'N/A')

# Imprime os detalhes do IP externo formatados
print('Detalhes do IP externo\n')
print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cid}\nOrg.: {org}')
'''