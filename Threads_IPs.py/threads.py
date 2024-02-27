from threading import Thread
import time

def carro1(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('piloto: {} km: {} \n'.format(piloto, trajeto))

t_carro1 = Thread(target=carro1, args=[1 'Bruno'])
t_carro2 = Thread(target=carro2, args=[2 'Python'])

t_carro1.start()
T_carro2.start()

