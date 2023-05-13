continuar_usando = 1
lista_de_tarefas = []

while continuar_usando == 1:

    opcao_do_menu = 0 

    def menu():
     print('''\n    Selecione o que quer fazer:
     1 - Incluir nova tarefa,
     2 - Ver lista de tarefas,
     3 - Excluir tarefa salva,
     4 - Sair
     ''')
     

    #Receber a opção do usuario
    menu()
    opcao_do_menu = int(input('Qual o número ação você quer fazer? '))
   

    if opcao_do_menu == 1:
        print('Opção escolhida: 1 - Incluir nova tarefa.')
        opcao_do_menu = 0
        tarefa = input('\nDigite tarefa a ser adicionada: ')
        lista_de_tarefas.append(tarefa)
        print('\nSua lista de tarefas')
        print(lista_de_tarefas)
        continuar_usando1 = input("\nDeseja continuar incluindo? 1 para continuar, 2 para voltar para o menu ou 'sair' para sair: ")
        if continuar_usando1.isnumeric():
            while continuar_usando1 == '1':
                tarefa = input('\nDigite tarefa a ser adicionada: ')
                lista_de_tarefas.append(tarefa)
                print(lista_de_tarefas)
            else:
                continuar_usando1= input('\nDeseja continuar incluindo? 1 para continuar, 2 para voltar para o menu ou 3 para sair: ')
        else:
            print('Digite um valor das opções.')
            break
            

    elif opcao_do_menu == 2:
        print('Opção escolhida: 2 - Ver lista de tarefa.')
        opcao_do_menu = 0
        print('\nSua lista de tarefas')
        print(lista_de_tarefas)
        continuar_usando1 = input('\nInsira 1 para voltar para o menu ou PARE para sair: ')
        if continuar_usando1.isnumeric():
          if continuar_usando1 == '1':
            tarefa = input('\nDigite tarefa a ser adicionada: ')
            lista_de_tarefas.append(tarefa)
            print(lista_de_tarefas)
          elif continuar_usando1 == '2':
            continue
          else:
            continuar_usando1= input('\nDeseja continuar incluindo? 1 para continuar, 2 para voltar para o menu ou PARE para sair: ')
        else:
           break  

    elif opcao_do_menu == 3:
        print('Opção escolhida: 3 - Excluir tarefa salva.')
        opcao_do_menu = 0
        print(lista_de_tarefas)
        tarefaremovida = input('Qual tarefa você deseja remover? ')
        lista_de_tarefas.remove(tarefaremovida)
        print(lista_de_tarefas)
        menu()
        opcao_do_menu = int(input('Qual o número ação você quer fazer? '))    

    elif opcao_do_menu == 4:
        print('Opção escolhida: 4 - Sair.')
        respostadesaida = str(input('Quer mesmo sair? S/N ').upper())
        if (respostadesaida == 'S') or (respostadesaida == 'SIM'):
            break
        else: 
            print('\n')
            menu()
            opcao_do_menu = int(input('Qual o número ação você quer fazer? '))   