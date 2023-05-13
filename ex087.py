matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
col3 = soma = maior = 0
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = int(input(f'Digite um valor para a posição {x, c}: '))
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[x][c]:^5}]', end='')
        if matriz[x][c] % 2 == 0:
            soma += matriz[x][c]
    print()
print(f'A soma de todos os valores pares digitados é {soma}')
for x in range(0, 3):
    col3 += matriz[x][2]
print(f'A soma de todos os valores da terceira coluna é {col3}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é [{maior}])]')