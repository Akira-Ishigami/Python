while True:
    string1 = "Funcionario de número"
    string2 = "trabalhou"
    string3 = "horas por dia, e teve "
    string4 = "horas extra."
    string5 = "Seu salario será R$"

    print("Olá, seja bem vindo") 
    numero_Funcionario = int(input("Informe o número do funcionario:" ))

    print("Olá funcionario de numero " , numero_Funcionario)
    hr_extra = int(input("Quantas horas extra trabalhadas: "))
    hr = 8

    salario = 1650 + 30 * hr_extra 

    print(string1 , numero_Funcionario , string2 , hr , string3 , hr_extra , string4)
    print( string5 , salario) 

    continuar = input("Deseja fazer calculo de outro funcionario? N/S: ")
    if continuar.lower () != 's':
       break
