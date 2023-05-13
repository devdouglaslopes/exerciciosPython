from time import sleep

acionar = input('Acionar fogos de artifício? (S/n)')
if acionar.upper() == 'S':
    print('Fogos de artifício acionados.')
    for cont in range(10,-1,-1):
        print(f'-> {cont}')
        sleep(1)
    print('Bumm!! Buumm!! Poww!!')
else:
    print('Fogos de artifício não acionados.')