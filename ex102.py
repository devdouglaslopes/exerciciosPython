def fatorial(num, show=False):
    if show in 'S':
        show = True
    else:
        show = False
    from time import sleep
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    print(f'O fatorial de {num} é igual a {fat}.')
    if show == True:
        print(f'Mostrando processo de cálculo do fatorial...')
        sleep(1)
        fat = 1
        print(f'{num}! =>', end=' ')
        for c in range(num, 0, -1):
            if c != 1:
                fat *= c
                print(f'{c}', end=' x ')
            else:
                print(f'{c} = {fat}')
        

resp = fatorial(int(input('Qual número deseja saber o fatorial? ')), str(input('Quer ver o processo de cálculo do fatorial? [S/N]')).upper().strip())