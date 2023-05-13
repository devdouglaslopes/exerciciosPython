from random import randint
import time
megasena = []
jogo = []
print('-='*30)
print(f'    JOGA NA MEGASENA    ')
print('-='*30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(0, jogos):
    for n in range(0, 6):
        jogo.append(randint(0, 60))
    megasena.append(jogo[:])
    jogo.clear()
print(f'Sorteando {jogos} jogos')
for j in range(0, jogos):
    print(f'Jogo {j+1}: {megasena[j]}')
    time.sleep(1)
    