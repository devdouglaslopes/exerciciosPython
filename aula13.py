# O for é utilizado quando se sabe o limite
#Laço com variável de controle
c = int(input('Digite um número de 0 a 25: '))
for c in range(c,26):
    print(c)
print('FIM')

#Laço com variável de controle (e intervalo)
c = int(input('Digite um número de 0 a 25: '))
for c in range(c,26,2):
    print(c)
print('FIM')