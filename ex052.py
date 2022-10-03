n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1,n + 1):
    if n % c == 0:
        print('\033[33m')
        tot += 1
    else:
        print('\033[31m')
    print(c, end='  ')
print(f'O número {n} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele \033[31mNÃO É PRIMO\033[m!')
