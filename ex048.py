print('Soma entre todos os números ímpares que são múltiplos de três entre 1 e 500: ')
soma = 0
cont = 0
for n in range(1,501,2):
    if n % 3 == 0:
        soma += n #Acumulador
        cont = cont + 1 #Contador
print(f'A soma de todos os {cont} valores solicitados é: {soma}')