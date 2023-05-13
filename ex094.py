pessoas = []
pessoa = {}
while True:
    nome = str(input('Nome: '))
    pessoa['nome'] = nome
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    pessoa['sexo'] = sexo
    idade = int(input('Idade: '))
    pessoa['idade'] = idade
    pessoas.append(pessoa.copy())
    pessoa.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'No total foram cadastradas {len(pessoas)} pessoas.')
total_idade = 0
for p in pessoas:
    total_idade += p['idade']
media = total_idade / len(pessoas)
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'As mulheres desse grupo são: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=', ')
print() 
print(f'Lista das pessoas com idade acima da média: ')  
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ') 