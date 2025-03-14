while True:
    mensagem_boas_vindas = "Olá, seja bem vindo!"
    print(mensagem_boas_vindas)
    mensagem_nome = input("Qual o seu nome? ")
    peso = float(input("Informe o seu peso (kg): "))
    altura = float(input("Informe a sua altura (centímetros): "))
    
    imc = (altura * altura) / peso
    
    print(f"{mensagem_nome}, o seu IMC é de {imc:3f}")
    
    continuar = input("Deseja calcular o IMC de outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break
