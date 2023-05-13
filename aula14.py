# Estrutura de repetição while (usado quando não se sabe o limite)
n = 1
while n != 0: # Enquanto o valor 0 não for digitado, continuará repetindo o input 
    n = int(input('Digite um valor:'))
print('Fim')

r = 'S'
while r == 'S': # Enquando a resposta for S (sim) ele continuará executando o laço
    v = int(input('Digite um valor: '))
    r = str(input('Você quer continuar? [S/N] ')).upper()
print('Fim.')