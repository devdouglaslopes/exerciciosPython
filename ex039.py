from datetime import date
ano_nasc = int(input("Ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc
ano_alistamento = ano_nasc + 18
print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.")
if idade > 18:
    deveria_alistar_ha = idade - 18
    print(f"Você já deveria ter se alistado há {deveria_alistar_ha} anos.")
    print(f"Seu alistamento foi em {ano_alistamento}.")
elif idade < 18:
    anos_falta_para_alistar = 18 - idade
    print(f"Ainda faltam {anos_falta_para_alistar} para o alistamento.")
    print(f"Seu alistamento será em {ano_alistamento}.")
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

