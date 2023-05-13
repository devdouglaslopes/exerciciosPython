#Listas dentro de lista
pessoa1 = ['Antônio', 24]
pessoas = [['Maria', 18], ['João', 21], ['Carlos', 19]]
pessoas.append(pessoa1[:]) #Adicionando os dados de uma lista em outra
print(pessoas)
print(pessoas[1])
print(pessoas[1][0])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos.')
galera = []
dados = [] #Lista para armazenamento temporário
for c in range(0,3):
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(int(input('Digite a idade da pessoa: ')))
    galera.append(dados[:]) #Importante ser [:]!
    dados.clear() #Limpando a lista temporária
totmai = totmen = 0
for g in galera:
    if g[1] >= 21:
        print(f'{g[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{g[0]} é menor de idade.')
        totmen += 1
print(f'No total há {totmai} maiores e {totmen} menores de idade.')