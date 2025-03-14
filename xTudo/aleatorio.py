import os

while True:
    print("               ------------------------------------------------------------")
    print("               |                                                          |")
    print("               |                     Seja Bem Vindo!                      |")
    print("               |                                                          |")
    print("               |                                                          |")
    print("               |                 O que você deseja fazer:                 |")
    print("               |                                                          |")
    print("               |    1- Criar Arquivo                2- Ler Arquivo        |")
    print("               |    3- Apagar Arquivo                                     |")
    print("               |                                                          |")
    print("               ------------------------------------------------------------")
    resposta = int(input("                                Digite o que você deseja: "))

    # Função para criar arquivo
    def criar_arquivo(arquivo_novo):
        with open(f"{arquivo_novo}.txt", "w") as arquivo:
            conteudo = input("Escreva o conteúdo do arquivo:\n")
            arquivo.write(conteudo)
            print("Arquivo criado com sucesso")

    # Função para ler arquivo
    def ler_arquivo(arquivo_novo):
        try:
            with open(f"{arquivo_novo}.txt", "r") as ler:
                conteudo = ler.read()
                print(conteudo)
        except FileNotFoundError:
            print("Arquivo não encontrado")

    # Função para apagar arquivo
    def apagar_arquivo(arquivo_novo):
        try:
            os.remove(f"{arquivo_novo}.txt")
            print("Arquivo apagado com sucesso")
        except FileNotFoundError:
            print("Arquivo não encontrado")

    # Verificar a resposta do usuário
    if resposta == 1:
        arquivo_novo = input("Digite o nome do arquivo: ")
        criar_arquivo(arquivo_novo)
    elif resposta == 2:
        arquivo_novo = input("Deseja ler qual arquivo: ")
        ler_arquivo(arquivo_novo)
    elif resposta == 3:
        arquivo_novo = input("Digite o nome do arquivo para apagar: ")
        apagar_arquivo(arquivo_novo)
    else:
        print("Opção inválida")

    # Perguntar se deseja continuar
    continuar = input("Deseja continuar? s/n \n")
    if continuar.lower() == 'n':
        break
