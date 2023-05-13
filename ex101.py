def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade < 16:
        return 'Voto NEGADO'
    if idade == 16 or idade == 17:
        return 'Voto OPCIONAL'
    if idade >= 18:
        return 'Voto OBRIGATÓRIO'


ano_nasc = int(input('Digite seu ano de nascimento: ')) 
situação = voto(ano_nasc)
print(f'Nas eleições atuais você tem {situação}.')


    