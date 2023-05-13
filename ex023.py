numero = input('Digite um número de 0 a 9999:')
num = numero.split()
print(''' 
Esse número possui:
unidade:{}
dezena:{}
centena:{}
milhar:{}
'''.format((num[0][3]),(num[0][2]),(num[0][1]),(num[0][0])))