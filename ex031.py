dist = float(input('Qual é a distância da sua viagem em Km? '))
print('Você está prestes a fazer uma viagem de {:.1f}Km.'.format(dist))
if dist <= 200:
    print('E o preço da sua passagem é de R${:.2f}'.format(dist*0.50))
elif dist > 200:
    print('E o preço da sua passagem é de R${:.2f}'.format(dist*0.45))