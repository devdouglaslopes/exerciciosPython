# Faça um programa que leia um número qualquer e mostre seu fatorial.
num = int(input('Digite um número inteiro: '))
fat = 1
i = 1
while i <= num:
    fat *= i
    i += 1
print(f'O fatorial do número {num} é {fat}.')