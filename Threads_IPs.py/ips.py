import ipaddress

ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)


#===========================================================


import ipaddress

ip = "192.168.0.1"

endereco = ipaddress.ip_address(ip)

print(endereco + 256)