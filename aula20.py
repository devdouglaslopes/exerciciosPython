#Funções
#A recomendação é separar as def's uma da outra e do programa principal por 2 linhas
def linha(): #Definindo uma função
    print('-' * 30)
    
    
def título(txt): #Definindo uma função com variável
    print('-' * 30)
    print(f'{txt.upper():^30}')
    print('-' * 30)
    
    
def soma(a, b): #Função com 2 (ou mais) parâmetros
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma é igual a {s}')    


def contador(*num): #Desempacotando parâmetros (*variável) (Para vários valores)
    print(f'Recebi os valores', end=' ')
    for numero in num: #Foi criada um tupla com os números digitados
        print(f'{numero}', end=' ')
    print(f'e ao todo são {len(num)} números. Soma igual a {sum(num)}')


def dobra(lista): #Dobrando os valores de um lista
    pos = 0  #Começando pela posição do item 0 da lista
    print(f'Lista antes de dobrar: {lista}')
    while pos < len(lista):  #Laço while para passar por todos os itens da lista
        lista[pos]*=2  
        pos += 1
    print(f'Lista dobrada: {lista}')
#   
#Programa Principal   
linha()
#
título('sistema de alunos')
#
soma(234, 456)  #Sem explicitar os parâmetros
#OU
soma(b=234, a=456)  #Explicitando os parâmetros, porém se você explicitar 1 valor, deve explicitar todos os outros
#
contador(4, 5, 2, 3,)
#
lista = [2, 3, 7, 4]
dobra(lista)  #Chamando a def para dobrar os números da lista