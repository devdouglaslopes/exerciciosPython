#Dicionários
#Definindo um dicionário
dados = dict() 
#Ou
dados = {} #Chaves representam um dicionário
#
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
#
#Inserindo dados
dados['sexo'] = 'M'
print(dados)
#
#Deletando uma chave junto com o elemento dele
del dados['idade']
print(dados)
#
#Exemplo de dicionário
filme = {'título':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
    }
#
#Utilizando apenas os valores
print(filme.values())
#
#Utilizando apenas as chaves
print(filme.keys())
#
#Utilizando os valores e as chaves do dicionário
print(filme.items())
#Exemplo com for
for k, v in filme.items():
    print(f'O {k} é {v}')
#
#Dicionários dentro de listas
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1]['sigla'])