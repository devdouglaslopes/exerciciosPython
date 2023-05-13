lista = []
lista_pares = []
lista_impares = []
while True:
    digitado = int(input('Digite um valor: '))
    lista.append(digitado)
    print('Número adicionado.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
            break
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
lista.sort()
lista_pares.sort()
lista_impares.sort()
print(f'Lista com todos os números digitados: {lista}')
print(f'Lista com todos os números pares digitado: {lista_pares}')
print(f'Lista com todos os números ímpares digitado: {lista_impares}')