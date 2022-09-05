from calendar import month
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Data e hora atual
p = float(input('Digite o valor do produto: R$'))
parc = int(input('Em quantas vezes você deseja parcelar?'))

atual = datetime.now()
calc = atual.month + 1
calc2 = calc + 1
new = atual.strftime("%d/{}/%Y".format(calc))

count = 0
while count <= parc:
    count += 1
    if count > parc: break
    
    print("{}° parcela: {}".format(count,new))