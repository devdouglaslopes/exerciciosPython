pessoas = homens = maior_18 = mulher_20 = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]
    idade = int(input('Digite a idade da pessoa: '))
    pessoas += 1
    if idade >= 18:
        maior_18 += 1 
    if sexo == 'M':
        homens += 1 
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''No total foram cadastradas {pessoas} pessoas. 
      {maior_18} pessoa(s) possuem mais de 18 anos.
      {homens} pessoa(s) são do sexo masculino.
      {mulher_20} pessoa(s) do sexo feminino com idade menor que 20 anos.''')
