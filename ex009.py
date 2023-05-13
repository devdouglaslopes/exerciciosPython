n = int(input('Digite um número para ver sua tabuada:'))
#Consultar a tabuada
print('A tabuada de {} é:'.format(n))
print('-'*12)
for i in range(1,11):
    print('{} x {:2} = {}'.format(n,i,n*i))