from re import S


s = float(input('Qual é o salário do funcionário? R$'))
d = float(input('Qual o desconto que você deseja aplicar(em %):'))
calc = s + (s*d)/100
print('Um funcionário que ganhava R${:.2f}, com ({}%) de aumento passa a receber R${:.2f}.'.format(s,d,calc))