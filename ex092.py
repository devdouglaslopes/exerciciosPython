from datetime import date
ano_atual = date.today().year
dados = {}
nome = str(input('Nome: '))
dados['nome'] = nome
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
dados['idade'] = idade
ctps = int(input('Carteira de trabalho (0 não tem): '))
dados['ctps'] = ctps
if ctps != 0:
    contratação = int(input('Ano de contratação: '))
    dados['contratação'] = contratação
    salario = int(input('Salario: '))
    dados['salario'] = salario
    aposentadoria = (contratação - ano_nascimento) + 35
    dados['aposentadoria'] = aposentadoria
print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')