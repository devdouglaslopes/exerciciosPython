from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número de 0 até 5. Tente adivinhar...')
print('-=-'*20)
computador = int(input('Em que número eu pensei? ')) #Jogador pensa em um número
jogador = randint(0,5) #Computador "PENSA" em um número
print('Processando...')
sleep(3)
if computador == jogador:
    print('PARABÈNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não {}.'.format(computador,jogador))