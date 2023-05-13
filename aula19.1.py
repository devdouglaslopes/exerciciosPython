estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #.copy() é o comando para fazer a cópia de um dicionário
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')