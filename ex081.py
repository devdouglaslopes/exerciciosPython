lista = []
cont = 0
digitado_5 = 0
while True:
    digitado = int(input('Digite um valor: '))
    lista.append(digitado)
    cont += 1
    if digitado == 5:
        digitado_5 += 1
    print('Valor adicionado.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
            break
print(f'No total foram digitados {cont} números.')
lista.sort(reverse=True)
print(f'A lista dos números em ordem decrescente: {lista}')
if digitado_5 > 0:
    print(f'O valor 5 foi digitado {digitado_5} vezes', end=' ')
else:
    print('O valor 5 não foi digitado')
if 5 in lista: #Verificando se um item da lista existe
    print(f'e está na lista nas posições ', end='')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i}...',end=' ')
else:
    print(f'O valor 5 não está na lista.')