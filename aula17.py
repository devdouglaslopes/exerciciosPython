#Manipulando Listas
lanches = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim'] #Listas são entre colchetes
lanches[3] = 'Picolé' #Substituindo um item da lista
print(lanches)
item = 'Hambúrguer' #Mostrando a posição de um item da lista
posicao = lanches.index(item) 
print(posicao)
lanches.append('Bolo') #Adicionando um item á lista
print(lanches)
lanches.insert(0,'Pão') #Adicionando um item com posição
print(lanches)
del lanches[3] #Eliminando item por posição com del
print(lanches)
lanches.pop() #Eliminiando último item da lista
print(lanches)
lanches.pop(1) #Eliminando item por posição com pop
print(lanches)
lanches.remove('Pão') #Eliminando o (primeiro) item pelo valor dele
print(lanches)
if 'Pizza' in lanches: #Verificando se um item da lista existe
    lanches.remove('Pizza')
    print(lanches)
valores = list(range(4,11)) #Criando uma lista com list() e range()
print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() #Organizando os valores da lista
print(valores)
valores.sort(reverse=True) #Reverso da ordem dos valores
print(valores)
print(len(valores)) #Mostra a quantidade de itens da lista