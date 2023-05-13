num = int(input('Me diga um número qualquer: '))
resultado = num % 2
if resultado == 0:
    print('O número {} é PAR.'.format(num))
elif resultado == 1:
    print('O número {} é ÍMPAR.'.format(num))
