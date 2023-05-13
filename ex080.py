#Organizando valores de um lista sem usar o sort
valores = []
for v in range(0, 5):
    digitado = int(input('Digite um valor: '))
    if v == 0 or digitado > valores[-1]:
        valores.append(digitado)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if digitado <= valores[pos]:
                valores.insert(pos, digitado)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}')