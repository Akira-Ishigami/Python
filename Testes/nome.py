# separar nome e sobrenome
while True:
    nome_completo = input("Digite seu nome completo: ").strip()

    nomes = nome_completo.split()

    primeiro_nome = nomes[0]

    ultimo_nome = nomes[-1]

    print("Primeiro nome:", primeiro_nome)
    print("Sobrenome completo:", ' '.join(nomes[1:]))
    print("Último nome:", ultimo_nome)
    
    continuar = input("Deseja continuar? S/N: ")
    if continuar.lower() != 's':
        break
