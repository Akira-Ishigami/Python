while True:

    #boas vindas
    print ("Olá, seja bem vindo.")
    print("Vamos calcular quanto o funcionario ira receber por diarias.")
    
    #informações
    string1 = input("Qual o nome do funcionario? ")
    print("Ok")
    print ("Vamos calcular o valor das diarias do funcionario " ,string1)
    print ("Preencha as informações abaixo.")
    salario = int(input("Qual o valor das diarias? "))
    dias = int(input("Trabalhou por quantas diarias? "))
    print("Ok, vamos calcular")

    #calculo
    reais = salario * dias 

    #resultado
    print("R$",reais)
    
    #loop
    continuar = input("Deseja calcular as diarias de outro funcionário? (s/n): ")
    if continuar.lower() != 's':
        break