valores = []
while True:
    digitado = int(input('Digite um valor: '))
    if digitado not in valores:
        valores.append(digitado)
        print(f'Valor inserido com sucesso...')
    else:
        print('Erro! Valor já existente.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
            break
valores.sort()
print(f'Valores inseridos: {valores}')