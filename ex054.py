from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {pess}° pessoa nasceu? '))
    idade = atual - ano_nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'''Ao todo tivemos {totmaior} pessoas maiores de idade.
E também tivemos {totmenor} pessoas menores de idade. 
''')