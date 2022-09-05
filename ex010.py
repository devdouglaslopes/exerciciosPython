from curses.ascii import isalnum


d = float(input('Quanto dinheiro você tem na carteira? R$'))
c = d / 5.16
print('Com {:.2f} você pode comprar U${:.2f}.'.format(d,c))
