dados_client = {}

nome = input("Digite o nome do cliente: ")
endereco = input("Digite o endereco: ")

cpf = input("Digite o CPF: ")
if len(cpf) != 11:
    print("CPF inválido")
else:
    tel = input("Digite o Telefone (somente números): ")
    if len(tel) != 10:
        print("Telefone inválido")
    else:
        # Armazenando os dados do cliente no dicionário
        dados_client = {
            'Nome': nome,
            'Cpf': cpf,
            'Telefone': tel,
            'Endereco': endereco
        }
        print(dados_client)
