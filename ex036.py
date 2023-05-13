val_casa =  float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
qtd_anos = int(input('Quantos anos de financiamento? '))
qtd_parcelas = qtd_anos*12

prestação = val_casa/qtd_parcelas

print('Para pagar uma casa de R${:.2f} em {} anos'.format(val_casa,qtd_anos))
print('a prestação será de R${:.2f}.'.format(prestação)) 
if prestação < salario*0.30:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')