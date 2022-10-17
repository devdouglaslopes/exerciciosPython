from random import randint
palpites = 0
print('-=-'*20)
print('Vou pensar em um número de 0 até 10. Tente adivinhar...')
print('-=-'*20)
computador = randint(0,10) #Computador "PENSA" em um número
acertou = False
while not acertou:
    jogador = int(input('Em que número eu pensei? ')) #Jogador pensa em um número
    palpites += 1
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais... Tente mais uma vez ')
        if computador < jogador:
            print('Menos... Tente mais uma vez ')
print(f'Você acertou com {palpites} tentativas.')