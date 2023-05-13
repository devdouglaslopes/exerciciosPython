valores = []
for v in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='' )
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...',end=' ')
print(f'\n')
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end=' ')