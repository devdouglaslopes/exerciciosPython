print(f'{" LOJAS DOUGLAS ":=^40}')
preço = float(input('Preço das compras: R$ '))
opção = int(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartâo
[ 4 ] 3x ou mais no cartão
Qual é a opção? 
"""))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f}.")
elif opção == 4:
    total = preço + (preço * 0.20)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc}x de {parcela:.2f} COM JUROS.")
print(f"Sua compra de {preço:.2f} vai custar {total:.2f} no final.")
print(f'{"":=^40}')