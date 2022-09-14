salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    salario_novo = salario + (salario*0.15)
    print('Quem ganhava R${:.2f} passou a ganhar R${:.2f} agora.'.format(salario,salario_novo))
elif salario > 1250:
    salario_novo = salario + (salario*0.10)
    print('Quem ganhava R${:.2f} passou a ganhar R${:.2f} agora.'.format(salario,salario_novo))