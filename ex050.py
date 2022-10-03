soma = 0
cont = 0
for n in range(1,7):
    n = int(input(f'Digite o {n} número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')