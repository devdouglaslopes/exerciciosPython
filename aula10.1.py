#Calcular a média aritmética
n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
m = (n1+n2)/2
print('A média de {:.1f} e {:.1f} é igual a {:.1f}'.format(n1,n2,m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')