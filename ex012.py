p = float(input('Qual é o preço do produto? R$'))
calc = (p*5)/100
desc = p - calc
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(p,desc))