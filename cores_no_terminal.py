#Style:
print('-='*6,'Style','-='*6)
print('\033[0mOlá, Mundo!\033[m') #0 (Normal)
print('\033[1mOlá, Mundo!\033[m') #1 (Negrito)
print('\033[4mOlá, Mundo!\033[m') #4 (Sublinhado)
print('\033[7mOlá, Mundo!\033[m') #7 (Inversão da cor da fonte e do fundo).
#Cores Texto:
print('-='*6,'Colors','-='*6)
print('\033[0;30mOlá, Mundo!\033[m') #Branco
print('\033[0;31mOlá, Mundo!\033[m') #Vermelho
print('\033[0;32mOlá, Mundo!\033[m') #Verde
print('\033[0;33mOlá, Mundo!\033[m') #Amarelo
print('\033[0;34mOlá, Mundo!\033[m') #Azul
print('\033[0;35mOlá, Mundo!\033[m') #Roxo
print('\033[0;36mOlá, Mundo!\033[m') #Ciano
print('\033[0;37mOlá, Mundo!\033[m') #Cinza
#Background:
print('-='*6,'Background','-='*6)
print('\033[0;30;40mOlá, Mundo!\033[m') #Branco
print('\033[0;30;41mOlá, Mundo!\033[m') #Vermelho
print('\033[0;30;42mOlá, Mundo!\033[m') #Verde
print('\033[0;30;43mOlá, Mundo!\033[m') #Amarelo
print('\033[0;30;44mOlá, Mundo!\033[m') #Azul
print('\033[0;30;45mOlá, Mundo!\033[m') #Roxo
print('\033[0;30;46mOlá, Mundo!\033[m') #Ciano
print('\033[0;30;47mOlá, Mundo!\033[m') #Cinza
print('-='*18)
# Para terminar a linha com a configuração de cor apenas coloque \033[m
print('Exemplo:')
print('Os valores são \033[4;33m3\033[m e \033[4;36m5\033[m .')