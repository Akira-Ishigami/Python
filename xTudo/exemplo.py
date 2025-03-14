inserir_nome = input("Qual o seu nome: ")
inserir_idade = int(input(f"{inserir_nome} insira a sua idade: "))

if inserir_idade <= 17:
    print(f"{inserir_nome} é menor de idade")

elif inserir_idade >= 18:
    print(f"{inserir_nome} você já é de maior de idade")