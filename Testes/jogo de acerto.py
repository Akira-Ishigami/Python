# jogo do acerto
import random

numero_secreto = random.randint(1, 200)

print("Seja bem-vindo!")
nome = input("Digite o seu nome: ")
print('Adivinhe o número de 1 a 200!!')

while True:
    palpite = int(input("Chute o número de 1 a 200!! "))

    if palpite > numero_secreto:
        print("Número alto, chute um número mais baixo!!")
    
    elif palpite < numero_secreto:
        print("Número baixo, chute um número mais alto!!")

    else:
        print("Parabéns, você acertou!!")
        continuar = input("Deseja continuar jogando? (s/n): ")
        if continuar.lower() != 's':
            break
        else:
            numero_secreto = random.randint(1, 200)  # Resetando o número secreto para o próximo jogo

print("Fim de jogo,", nome)
