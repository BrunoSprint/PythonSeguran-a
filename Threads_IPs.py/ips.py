# Importa a biblioteca ipaddress para manipulação de endereços IP e redes.
import ipaddress

# Define um endereço IP e máscara de sub-rede como uma string.
ip = '192.168.0.0/24'

# Cria um objeto de rede utilizando a função ipaddress.ip_network.
# O parâmetro strict=False permite que a função aceite formatos não estritamente IPv4 ou IPv6.
rede = ipaddress.ip_network(ip, strict=False)

# Itera sobre todos os endereços IP na rede e os imprime no console.
for endereco_ip in rede:
    print(endereco_ip)


#===========================================================

# Importa a biblioteca ipaddress para manipulação de endereços IP.
import ipaddress

# Define um endereço IP como uma string.
ip = "192.168.0.1"

# Cria um objeto de endereço IP utilizando a função ipaddress.ip_address.
endereco = ipaddress.ip_address(ip)

# Adiciona 256 ao endereço IP e imprime o resultado.
# O resultado será um novo objeto ipaddress.ip_address representando o endereço incrementado.
print(endereco + 256)
