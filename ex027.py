nome_completo = str(input('Digite seu nome completo:')).strip()
nome = nome_completo.split()
print('''
Muito prazer em te conhecer!
Seu primeiro nome é:{}
E seu último nome é:{}
'''.format(nome[0],nome[len(nome)-1]))
