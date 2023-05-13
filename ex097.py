def escreva(txt): #Modelo de print
    for i in range(0, len(txt)+6):
        print(f'-', end='')
    print()
    print(f'   {txt:^}   ')
    for i in range(0, len(txt)+6):
        print(f'-', end='')
    print()
        
    

escreva('Olá Mundo!')
escreva('Bispo de Constantinopla')
escreva('Oi')