from random import randint
from time import sleep
def sorteio(lista):
    print('Sorteando 5 números...')
    sleep(1)
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print('Os números sorteados foram:', end=' ')
    for i in lista:
        print(i, end=' ')
        sleep(0.8)
    print()
    
    
def somaPares(lista):
    print('A soma dos valores pares sorteados:', end=' ')
    soma = 0
    for i in lista:
        if i % 2 == 0:
            print(i, end=' ')
            soma += i
    print(f'é igual a {soma}.')
    
    
numeros = []
sorteio(numeros)
somaPares(numeros)
            
            
    
    
    
numeros = []