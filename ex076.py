# Definição da tupla com nomes de produtos e seus respectivos preços
produtos = (
    ('Arroz', 10.99),
    ('Feijão', 8.99),
    ('Óleo de Soja', 4.99),
    ('Açúcar', 3.49),
    ('Café', 7.99),
    ('Leite', 2.29),
    ('Pão de Forma', 4.49),
    ('Queijo Mussarela', 25.99),
    ('Presunto', 15.99),
    ('Manteiga', 7.99),
)

# Impressão da listagem de preços em forma tabular
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for produto, preco in produtos:
    print(f'{produto:.<30}R$ {preco:>7.2f}')
print('-' * 40)

