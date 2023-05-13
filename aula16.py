lanche =  'Hambúrguer','Pizza','Suco','Pudim','Batata Frita'
#Tuplas são imutáveis
print(lanche)
#print(lanche[1:3])

#print(len(lanche),'\n')
#OU
for cont in range(0,len(lanche)):
    print(cont)
    
#for comida in lanche:
#    print(f'Eu vou comer {comida}')
#OU  
#for cont in range(0,len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
#OU    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
    
print(sorted(lanche))

