#Ajuda interativa do Python
help(print) #O comando help() mostra a descrição completa do comando
help(input.__doc__) #o comando .__doc__ também mostra a descrição do comando
#
#Criando uma docstring (manual da função)
def contador(i, f, p): #Aspas duplas 3x depois da declaração da def incia a documentação
    """
    => Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Final da contagem
    :param p: Passo da contagem
    :return: Retorno da contagem
    Função criada por Douglas Carneiro.
    """
#Aspas duplas 3x depois da declaração da def incia a documentação
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')

#Parâmetro Opcional
def somar(a=0, b=0, c=0): #Caso não seja inserido todos os 3 valores
    s = a + b + c
    print(f'A soma é igual a: {s}')
#somar(b=4, c=2)


def test(b):
    # a = 0
    global a #Chamando uma variável global para dentro da função
    b += 4 #Se não chamasse a variável 'a' global, seria utilizado para somar, a variável 'a' local
    c = 6 #Variável local
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    

def somar(a=0, b=0, c=0): #Função com retorno
    s = a + b + c
    
    return s


r1 = somar(2, 3, 8)
r2 = somar(4, 3)
r3 = somar(6)
print(f'Os resultados das somas foram {r1}, {r2}, {r3}')




a = 3
test(a)