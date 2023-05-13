p = float(input('Digite o valor do produto: R$'))
parc = int(input('Em quantas vezes você deseja parcelar?'))
desc = p - (p*10)/100
aumento = p + (p*8)/100
calparc = aumento/parc
print('Esse produto parcelado em {}x custa em parcelas de R${} sendo no total R${} e a vista custa R${:.2f}.'.format(parc,calparc,aumento,desc))


