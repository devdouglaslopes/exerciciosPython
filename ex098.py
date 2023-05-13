from time import sleep
def linha():
    print('=-' * 20)
    
    
def contador():
    linha()
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11, 1):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')
    linha()
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, 0, -2):
        print(i, end=' ')
        sleep(0.3)
    print('FIM!')
    linha()
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: ')) 
    while passo == 0:
        print('Passo 0 é inválido, digite outro valor.')
        passo = int(input('Passo: '))
    if passo < 0:
        if inicio < fim:
            while passo < 0:
                print(f'Passo negativo é inválido para essa contagem, digite um valor positivo para passo.')
                passo = int(input('Passo: '))
        if fim < inicio:
            passo = abs(passo)
    if passo > 0: 
        if inicio < fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            for i in range(inicio, fim, passo):
                print(i, end=' ')
            print('FIM!')
        if fim < inicio:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            passo = passo - (passo * 2)
            for i in range(inicio, fim, passo):
                print(i, end=' ')
            print('FIM!')
    

contador()
        
    
    
    