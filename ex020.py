from random import shuffle
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundoo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1,n2,n3,n4]
escolhido = shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
