cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0
while True:
    saque = int(input("Qual o valor a ser sacado? "))
    while saque >= 50:
        cedulas50 += 1
        saque = saque - 50
        if saque < 50:
            break
    while saque >= 20:
        cedulas20 += 1
        saque = saque - 20
        if saque < 20:
            break
    while saque >= 10:
        cedulas10 += 1
        saque = saque - 10
        if saque < 10:
            break
    while saque >= 1:
        cedulas1 += 1
        saque = saque - 1
        if saque < 1:
            break
    print(f'{cedulas50:.0f} cédulas de 50 reais.')
    print(f'{cedulas20:.0f} cédulas de 20 reais.')
    print(f'{cedulas10:.0f} cédulas de 10 reais.')
    print(f'{cedulas1:.0f} cédulas de 1 real.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
        
        