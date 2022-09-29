vel_atual = float(input('Qual a velocidade atual do carro em (Km/h)? '))
if vel_atual >= 80:
    print('MULTADO!  Você excedeu o limite que é de 80Km/h \n Você deve pagar uma multa de R${:.2f}'.format((vel_atual-80)*7))
print('Tenha um bom dia! Dirija com segurança!!!')