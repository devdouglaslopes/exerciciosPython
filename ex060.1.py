num = int(input('Digite um número inteiro: '))
fat = 1

for i in range(1, num+1):
    fat *= i
print(f'O fatorial do número {num} é {fat}.')