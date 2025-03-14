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

    # Criar arquivo
    
    def criar_arquivo(Novo_arquivo):
        with open(f"{Novo_arquivo}.txt", "w") as arquivo:
            conteudo = input("Escreva o conteudo do arquivo:\n")
            arquivo.write(conteudo)
            print("Arquivo criado com sucesso")

    # Ler arquivo
    
    def ler_arquivo(Novo_arquivo):
        try:
            with open(f"{Novo_arquivo}.txt", "r") as ler:
                conteudo = ler.read()
                print(conteudo)
        except FileNotFoundError:
            print("Arquivo não encontrado")

    # Apagar arquivo
    
    def apagar_arquivo(Novo_arquivo):
        try:
            os.remove(f"{Novo_arquivo}.txt")
            print("Arquivo apagado com sucesso")
        except FileNotFoundError:
            print("Arquivo não encontrado")

    # Resposta 1, 2 ou 3
    
    if resposta == 1:
        Novo_arquivo = input("Digite o nome do arquivo: ")
        criar_arquivo(Novo_arquivo)
        
    elif resposta == 2:
        Novo_arquivo = input("Deseja ler qual arquivo: ")
        ler_arquivo(Novo_arquivo)
        
    elif resposta == 3:
        Novo_arquivo = input("Digite o nome do arquivo que deseja apagar: ")
        apagar_arquivo(Novo_arquivo)
        
    else:
        print("Opção inválida")

    # Laço de repetição
    
    continuar = input("Deseja continuar? s/n \n")
    if continuar.lower() == 'n':
        break
