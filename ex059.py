operacao = 0
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
while operacao != 5:
    operacao = int(input('''Qual operação deseja realizar?
[1] Somar
[2] Multiplicar
[3] Mostra o maior número
[4] Digitar novos números
[5] Sair do programa               
: '''))
    if operacao == 1:
        soma = v1 + v2
        print(f'A soma dos valores digitados é {soma}')
     
    elif operacao == 2:
        multiplicacao = v1 * v2
        print(f'A multiplicação dos valores digitados é {multiplicacao}')
    elif operacao == 3:
        if v1 > v2:
            print(f'O maior valor digitado é {v1}')
        else:
            print(f'O maior valor digitado é {v2}')
    elif operacao == 4:
        v1 = int(input('Digite o novo primeiro valor: '))
        v2 = int(input('Digite o novo segundo valor: '))
print('Finalizando...')