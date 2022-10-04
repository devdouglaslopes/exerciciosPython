soma_idade = 0
med_idade = 0
mais_velho = 0
menos_20 = 0
nome_mais_velho = ''
for p in range(1,5):
    print('-'*5,f'{p}° PESSOA','-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo  [M/F]: ')).upper().strip()
    soma_idade += idade
    if p == 1 and sexo == 'M':
        mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        menos_20 +=1
med_idade = soma_idade / 4
print(f'A média de idade do grupo é de {med_idade} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {menos_20} mulheres com menos de 20 anos.')
