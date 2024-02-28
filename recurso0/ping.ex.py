# ICMP (Iternet Control Message Protocol) um protocolo integrante do Protocólo IP Ultilizado para fornecer relatórios de erros à #fonte original.

# REQUEST - REPLAY


# Ping Simples
import os #importa módulo ou bibliotéca OS(Integra os programas e recursos do S.O)


print("#" * 60)
# imprimindo o # 60x

ip_ou_host = input("Digite o ip ou host a ser verificado:")
# váriavel que vai receber do usuario um ip

print("-" * 60)
# imprimondo o - 60x

os.system(' ping -n 6 {}' .format(ip_ou_host)) 
# chamando System da biblioteca OS - comando ping -n - num de pacotes que serão 6 {}

print("-" * 60) # imprimondo o - 60x




# PING MULTIPLO


