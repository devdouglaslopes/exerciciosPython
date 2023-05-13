def adicionarHerói():
    personagens = []
    heróis = {} 
    while True:
        classe = str(input('A qual classe de heróis deseja adicionar?: ')).strip().upper()
        while True:  
            heroi = str(input('Digite o nome herói: ')).strip().upper()
            heróis['Nome'] = heroi
            heróis['Classe'] = classe
            if classe == 'MAGO':
                tipo_de_dano = 'AP'
            else:
                tipo_de_dano = str(input('Digite o tipo de dano desse herói ("AD" para dano físico e "AP" para dano mágico): ')).strip().upper()
            heróis['Dano'] = tipo_de_dano
            range_de_ataque = str(input('Qual a distância dos ataques desse herói (C para Curto, M para Médio, L para Longe): ')).strip().upper()
            heróis['Range'] = range_de_ataque
            personagens.append(heróis.copy())
            heróis.clear()        
            continuar = ' '
            while continuar not in 'SN':
                continuar = str(input('Quer adicionar outro herói? [S/N]')).upper().strip()
            if continuar == 'N':
                break   
        adicionar_outra_classe = ' '
        while adicionar_outra_classe not in 'SN':
            adicionar_outra_classe = str(input('Quer adicionar outra classe? [S/N]')).upper().strip()
        if adicionar_outra_classe == 'N':
            break   
    return personagens

def calculoDePick(classe, tipo_de_dano):
    global personagens
    print(f'Heróis recomendados:', end=' ')
    for p in personagens:
        if p['Classe'] == classe and p['Dano'] == tipo_de_dano:
            print(f'{p["Nome"]}', end=', ')     
    print()  
 
    
#Programa Principal    
personagens = [{'Nome': 'ALICE', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'C'}, {'Nome': 'NANA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'EUDORA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'GORD', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'KAGURA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'CYCLOPS', 'Classe': 
'MAGO', 'Dano': 'AP', 'Range': 'C'}, {'Nome': 'AURORA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'VEXANA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 
'HARLEY', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'ODETTE', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'ZHASK', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'VALIR', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'PHARSA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': "CHANG'E", 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'SELENA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'VALE', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'LUNOX', 
'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'KIMMY', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'HARITH', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, 
{'Nome': 'KADITA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'FARAMIS', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'LYLIA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'CECILION', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'LUO YI', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'YVE', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'VALENTINA', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'XAVIER', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'L'}, {'Nome': 'GUSION', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'M'}, {'Nome': 'JULIAN', 'Classe': 'MAGO', 'Dano': 'AP', 'Range': 'C'}]
print('Bem vindo ao SGPPB (Sistema de Gerenciamento de Personagens e Picks e Bans)!')
while True:
    opção = int(input('''Digite a opção que deseja usar: 
1 - Cadastrar heróis
2 - Mostrar opções de pick
3 - Sair
: '''))
    if opção == 1:
        personagens = adicionarHerói()
        print(personagens)
    if opção == 2:
        calculoDePick(str(input('Classe: ')), str(input('Tipo de dano: [AD/AP]')).upper())
    if opção == 3:
        break