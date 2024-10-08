while True:
    string1 = "Funcionário de número"
    string2 = "trabalhou"
    string3 = "horas por dia, e teve"
    string4 = "horas extra."
    string5 = "Seu salário será R$"

    print("Olá, seja bem-vindo")
    numero_funcionario = int(input("Informe o número do funcionário: "))
    print("Olá funcionário", numero_funcionario)

    hr_extra = int(input("Quantas horas extra foram trabalhadas: "))
    hr = 8

    salario = 1650 + 30 * hr_extra 

    print(string1, numero_funcionario, string2, hr, string3, hr_extra, string4)
    print(string5, salario)

    continuar = input("Deseja calcular o salário de outro funcionário? (s/n): ")
    if continuar.lower() != 's':
        break
