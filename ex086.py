matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = int(input(f'Digite um valor para a posição {x, c}: '))
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[x][c]:^5}]', end='')
    print()
