a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
if b>a and c>a and b>c:
    menor = a
    maior = b
    print('O menor valor é {}.'.format(menor))
    print('O maior valor é {}.'.format(maior))
if a>b and b>c and a>c:
    menor = c 
    maior = a
    print('O menor valor é {}.'.format(menor))
    print('O maior valor é {}.'.format(maior))
if a>b and c>b and c>a:
    menor = b 
    maior = c
    print('O menor valor é {}.'.format(menor))
    print('O menor valor é {}.'.format(menor))
