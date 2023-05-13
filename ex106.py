from time import sleep
c = ('\033[m',        #0 - Sem cor
     '\033[0;30;41m', #1 - Vermelho
     '\033[0;30;42m', #2 - Verde
     '\033[0;30;43m', #3 - Amarelo
     '\033[0;30;44m', #4 - Azul
     '\033[0;30;45m', #5 - Roxo
     '\033[0;30;46m', #6 - Ciano
     '\033[0;30;47m',  #7 - Cinza
     '\033[0;30;40m'  #8 - Branco
    )


def ajuda(cmd):
    título(f'Acessando o manual do comando. \'{cmd}\'', 4)
    print(c[6], end='')
    help(cmd)
    print(c[0], end='')
    sleep(2)
    
def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    título('SISTEMA DE AJUDA DO PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)