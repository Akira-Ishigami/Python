# calcular vogais
frase = input("Digite uma frase: ")

espacos_em_branco = frase.count(' ')

vogais = 'aeiou'
contagem_vogais = {vogal: frase.lower().count(vogal) for vogal in vogais}

print(f"Espaços em branco: {espacos_em_branco}")
print("Contagem de vogais:")
for vogal, contagem in contagem_vogais.items():
    print(f"{vogal}: {contagem}")
