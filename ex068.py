#Par ou ímpar
from random import randint
ganhando = True
n_jogador = 0
n_computador = randint(0,10)
cont = 0

while ganhando == True:
    n_jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).upper()
    soma = n_jogador + n_computador
    if soma % 2 == 0 and escolha == 'P':
        print(f'Você jogou {n_jogador} e o computador jogou {n_computador}, Total de {soma}. DEU PAR! Você venceu.')
    elif soma % 2 == 1 and escolha == 'I':
        print(f'Você jogou {n_jogador} e o computador jogou {n_computador}, Total de {soma}. DEU ÍMPAR! Você venceu.')
    elif soma % 2 == 0 and escolha == 'I':
        print(f'Você jogou {n_jogador} e o computador jogou {n_computador}, Total de {soma}. DEU PAR! Você perdeu.')
        break
    elif soma % 2 == 1 and escolha == 'P':
        print(f'Você jogou {n_jogador} e o computador jogou {n_computador}, Total de {soma}. DEU ÍMPAR! Você perdeu.')
        break
    cont += 1
print(f'Você teve um total de {cont} vitórias consecutivas.')
    
        
    
    