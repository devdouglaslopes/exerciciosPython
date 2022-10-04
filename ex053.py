from audioop import reverse

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso da frase {frase} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
    