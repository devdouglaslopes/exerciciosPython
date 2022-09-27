from datetime import date
ano_nasc = int(input("Ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f"O atleta tem tem {idade} anos.")
if idade <= 9:
    print(f"Classificação: MIRIRM")
elif idade <= 14:
    print(f"Classificação: INFANTIL")
elif idade <= 19:
    print(f"Classificação: JÚNIOR")
elif idade <= 25:
    print(f"Classificação: SÊNIOR")
else:
    print(f"Classificação: MASTER")
