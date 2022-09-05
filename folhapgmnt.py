valor_da_hora = float(input('Digite o valor da hora: R$'))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))
salário_bruto = valor_da_hora * horas_trabalhadas
ir = salário_bruto * 0.05
inss = salário_bruto * 0.10
fgts = salário_bruto * 0.11
total_de_descontos = ir + inss
salário_líquido = salário_bruto - total_de_descontos
print('''Salário Bruto: ({} * {})        : R$ {:.2f}
        (-) IR (5%)                     : R$   {:.2f}
        (-) INSS ( 10%)                 : R$  {:.2f}
        FGTS (11%)                      : R$  {:.2f}
        Total de descontos              : R$  {:.2f}
        Salário Liquido                 : R$  {:.2f}'''.format(valor_da_hora, horas_trabalhadas, salário_bruto,ir,inss,fgts,total_de_descontos,salário_líquido))

