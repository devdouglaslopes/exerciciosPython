#Interrompendo laço while
n = 0
soma = 0 
cont = 0
while n != 999: 
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números digitados é {soma}')
    