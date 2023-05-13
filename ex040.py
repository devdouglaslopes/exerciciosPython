nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
media = (nota1 + nota2) / 2

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}.')
if 7 > media >= 5:
    print("O aluno está de RECUPERAÇÂO.")
elif media < 5:
    print("O aluno está REPROVADO.")
elif media >= 7:
    print("O aluno está APROVADO.") 