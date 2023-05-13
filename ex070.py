produtos = totG = totMil = barato = preco_item_atual = 0
p_barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$'))
    produtos += 1
    totG += preco
    if preco > 1000:
        totMil += 1 
    if produtos == 1 or preco < barato:
        barato = preco
        p_barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''No total foram adicionados {produtos} produtos. 
      O valor total do(s) produto(s) é R${totG:.2f}.
      No total {totMil} produtos custam acima de 1000 reais.
      O produto mais barato é {p_barato}, custando apenas R${barato:.2f}''')
