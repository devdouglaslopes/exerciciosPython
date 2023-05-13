continuar_usando = True

while continuar_usando:
  #Criando um menu de opções
  print('''SELECIONE A OPERAÇÃO DESEJADA
  + para Adição
  - para Subtração
  * para Multiplicação
  / para Divisão
  ** para Potenciação
  **/  para Radiciação
  // para Divisão Inteira
  % para Resto da Divisão
  ''')


  # Interação com o usuário
  operacao = input("\nQual operação você deseja realizar? ")

  #Criando as operações e as apresentações de respostas

  #Adição
  if operacao == "+":
    a1 = float(input("\nDigite o primeiro valor: "))
    a2 = float(input("Digite o segundo valor: "))
    adicao = a1 + a2
    print("\nA soma entre",a1,"e",a2,"é:",adicao,"\n")
    print("*"*33,"\n")
    input_usuario = input("Gostaria de fazer outra operação? 1 para Sim ou 2 para Não ")
    if input_usuario.isnumeric():
        if continuar_usando == 1:
            continue
        elif continuar_usando == 2:
            print("Obrigado por utilizar nossa calculadora")
            continuar_usando = False # ou break( sair do laço/loop)
        else:
            print("Resposta invalida! Favor escolha uma das opções...")
            continuar_usando = True
        print("*"*33,"\n")
    else:
        print("Valor digitado {input_usuario} não é numerico. Digite um valor numerico, 1 ou 2")


  #Subtração
  if operacao == "-":
    b1 = float(input("\nDigite o primeiro valor: "))
    b2 = float(input("Digite o segundo valor: "))
    subtracao = b1 - b2
    print("\nA subtração entre",b1,"e",b2,"é:",subtracao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #Multiplicação
  if operacao == "*":
    c1 = float(input("\nDigite o primeiro valor: "))
    c2 = float(input("Digite o segundo valor: "))
    multiplicacao = c1 * c2
    print("\nA multiplicação entre",c1,"e",c2,"é:",multiplicacao,"\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #Divisão
  if operacao == "/":
    d1 = float(input("\nDigite o primeiro valor: "))
    d2 = float(input("Digite o segundo valor: "))
    while d2 == 0:                  #Garantindo que d2 não seja zero!!
      print("O segundo valor não pode ser zero!")
      d2 = float(input("\nDigite o segundo valor (diferente de zero): "))
    divisao = d1 / d2
    print("\nA divisão entre",d1,"e",d2,"é:",divisao,"\n") 
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

    #Potenciação
  if operacao == "**":
    primeiro = 'primeiro'
    segunda = 'segunda'
    p1 = float(input("Digite o {} número: ".format(primeiro)))
    p2 = float(input("Digite o {} elevado: ".format(segunda)))
    potenciacao = p1 ** p2
    print("\nO resultado da potenciação de",p1,"elevado á",p2,"é:",potenciacao, "\n")
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

     #Radiciação
  if operacao == "**/":
    r1 = float(input("\nDigite o número: "))
    r2 = float(input("Digite a raíz: "))
    x = r1
    n = r2
    n = 1/n
  
    radiciacao = r1 ** n
    while r2 == 2:
      r2 = 'quadrada'
      quadrada = print("\nA raiz",r2,"de",r1,"é",radiciacao,)

    while r2 == 3:
      r2 = 'cubica'
      cubica = print("\nA raiz",r2,"de",r1,"é",radiciacao,)
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")
    
    #Divisão Inteira
  if operacao == "//":
    di1 = float(input("\nDigite o primeiro valor: "))
    di2 = float(input("Digite o segundo valor: "))
    while di2 == 0:                  #Garantindo que d2 não seja zero!!
      print("O segundo valor não pode ser zero!")
      di2 = float(input("\nDigite o segundo valor (diferente de zero): "))
    divisaoint = di1 // di2
    print("\nA divisão inteira entre",di1,"e",di2,"é:",divisaoint,"\n") 
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")
  
  #Resto da Divisão
  if operacao == "%":
    rd1 = float(input("\nDigite o primeiro valor: "))
    rd2 = float(input("Digite o segundo valor: "))
    while rd2 == 0:                  #Garantindo que d2 não seja zero!!
      print("O segundo valor não pode ser zero!")
      rd2 = float(input("\nDigite o segundo valor (diferente de zero): "))
    restodiv = rd1 % rd2
    print("\nNa divisão de",rd1,"por",rd2,"sobra:",restodiv,"\n") 
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")