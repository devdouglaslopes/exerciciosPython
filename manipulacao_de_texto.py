#Fatiamento de String
frase = 'Curso em Vídeo Python'
print('*'*6,'Fatiamento','*'*6)
print(frase[9:14])
print(frase[9:14:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
#Análise
print('*'*6,'Análise','*'*6)
print(len(frase)) #Conta quantos caracteres possui a string
print(frase.count('o')) #Conta quantos tipos daquele caractere possui a string
print(frase.count('o',0,13)) #Conta os caracteres daquele tipo com - fatiamento (0,13)
print(frase.find('deo')) #Encontra onde começa a posição daquele pedaço de string
print(frase.find('Android')) #Quando não encontra a string ele retorna o valor -1
print('Curso' in frase) #É um operador em que se pode fazer análise, retorna valor true(se a frase possuir a string) e false(se não possuir).
#Transformação
print('*'*6,'Transformação','*'*6)
print(len(frase)) #Conta quantos caracteres possui a string
print(frase.replace('Python','Android')) #Substitui uma string por outra
print(frase.upper()) #É um método, o que for maiúsculo ele mantém, o que não for ele transforma
print(frase.lower()) #É um método, o que for minúsculo ele mantém, o que não for ele transforma
print(frase.capitalize()) #Pega uma string inteira e transforma ela toda em minúscula mas com a primeira letra da frase maiúscula.
print(frase.title()) #Onde tiver espaço ele vai fazer uma quebra de palavra e vai fazer o capitalize palavra por palavra
frase2 = '   Aprenda Python  '
print(frase2.strip()) #Remove os espaços desnecessários no início e no final da string
print(frase2.rstrip()) #r(right) Remove os espaços desnecessários no final da string
print(frase2.strip()) #l(left) Remove os espaços desnecessários no início da string
#Divisão
print('*'*6,'Divisão','*'*6)
print(frase.split()) #Gera uma lista com todas as palavras de uma cadeia de caracteres, divindo-os em várias strings diferentes
dividido = frase.split()
print(dividido[2][3]) #Seleciona primeiro a string da lista, depois o caractere da string
#Junção
print('*'*6,'Junção','*'*6)
print('-'.join(frase)) #Gera uma string única e inclui o - entre eles para fazer a junção
