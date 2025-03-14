dados_biblioteca = {}

nome_livro = input("Qual o nome do livro: ")

edição = input(f"Qual a edição do livro {nome_livro}: ")

editora = input(f"Qual o nome da editora do livro {nome_livro}: ")

editor = input(f"Qual o nome do autor do livro {nome_livro}: ")

isbn = input(f"Qual o ISBN do livro {nome_livro}: ")

ano = input(f"Qual o ano de publicação do livro {nome_livro}: ")

dados_biblioteca = {
    'Nome do livro': nome_livro,
    'Edição': edição,
    'Editora': editora,
    'Autor': editor,
    'ISBN': isbn,
    'Ano de publicação': ano
}

print(dados_biblioteca)