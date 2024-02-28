# Importa o módulo phonenumbers para lidar com números de telefone
import phonenumbers

# Importa a função geocoder do módulo phonenumbers para obter informações de localização
from phonenumbers import geocoder

# Solicita ao usuário que insira um número de telefone no formato internacional específico
phone = input('Digite o telefone no formato +5511xxxxxxxxx: ')

# Analisa o número de telefone fornecido pelo usuário e o armazena em uma variável
phone_numbers = phonenumbers.parse(phone)

# Obtém a descrição geográfica associada ao número de telefone fornecido
# O segundo argumento ('pt') indica que queremos a descrição em português
description = geocoder.description_for_number(phone_numbers, 'pt')

# Imprime a descrição geográfica obtida na saída padrão (console)
print(description)
