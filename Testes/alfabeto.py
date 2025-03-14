# alfabeto
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

digita = int(input("Digite um número (1 a 26):  "))

if 1 <= digita <= 26:
    print(f"A letra correspondente ao número {digita} é {alfabeto[digita - 1]}")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 26.")