numeros = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')), int(input('Digite o quinto valor: ')))
print(f'Os valores digitados foram {numeros}')
print(f'O valor 9 apareceu um total de {numeros.count(9)} vezes')
print(f'O valor 3 apareceu primeiro na posição {numeros.index(3)}')
print(f'E os numeros pares digitados foram: ')
for n in numeros:
    if n % 2 == 0:
        print(n)