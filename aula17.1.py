valores = [] #Ou valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) #Armazenando valores na lista
for c, v in enumerate(valores): #A variável c recebe a enumeração dos valores e a variável v recebe o valor de cada enumeração
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

a = [2, 3, 4, 7]
b = a #A partir do momente que você iguala um lista á outra, o python cria um ligação entre elas
b = a[:] #Cria uma cópia dos valores de outra lista, assim não criando uma ligação entre as listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')