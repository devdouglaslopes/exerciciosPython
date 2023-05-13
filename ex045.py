from random import randint
from time import sleep
itens = ['PEDRA', 'PAPEL', 'TESOURA']
computador = randint(0, 2)
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
> Qual é a sua jogada? '''))
print('-='*12)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*12)
print(f'''Computador jogou {itens[computador]}.
Jogador jogou {itens[jogador]}.''')
print('-='*12)
if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 1: #Computador jogou papel
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    elif jogador == 0:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 2: #Computador jogou tesoura
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
