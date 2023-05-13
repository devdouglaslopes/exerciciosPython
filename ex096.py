def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area}m².')


area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))