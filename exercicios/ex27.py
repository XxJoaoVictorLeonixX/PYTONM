from random import randint
from time import sleep
computador = randint(0,5)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
jogador = int(input('Em que numero eu pensei?'))

print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABENS!! você acertou.')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}'.format(computador, jogador))