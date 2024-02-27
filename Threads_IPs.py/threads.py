from threading import Thread
import time

# Definição da função que representa o comportamento de um carro em movimento
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} km: {}\n'.format(piloto, trajeto))

# Criação de duas threads para representar dois carros com diferentes velocidades e pilotos
t_carro1 = Thread(target=carro, args=(1, 'Bruno'))  # Corrigido: Adicionado vírgula entre os argumentos
t_carro2 = Thread(target=carro, args=(2, 'Python')) # Corrigido: Adicionado vírgula entre os argumentos

# Inicia as threads para que os carros comecem a se mover simultaneamente
t_carro1.start()
t_carro2.start()  # Corrigido: 'T_carro2' alterado para 't_carro2' para corresponder à declaração anterior


