ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
                break
print('-' * 30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for n, dados in enumerate(ficha):
    print(f'{n:<4}{dados[0]:<10}{dados[2]:>8.1f}')
print('-' * 30)
continuar2 = 0 
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1: #Verificando se a opção é menor ou igual a quantidade de items da lista
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< Volte Sempre! >>>')
