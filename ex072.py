while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        print('Tente novamente. Digite um número entre 0 e 20: ')    
    extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    print(f'O número {num} por extenso é {extenso[num]}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break