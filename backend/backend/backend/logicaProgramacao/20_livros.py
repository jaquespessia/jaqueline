#Contexto: A biblioteca precisa de um sistema para catalogar os livros da escola.
#Crie um sistema que salve e liste os livros que devem ser salvos no arquivo
#biblioteca.json

#Atributos necessarios
#titulo, autor, editora, ano_publicado, genero, numero_paginas, idioma


import json

livros = []

try:
    with open('biblioteca.json', 'r') as arquivo:
        livros = json.load(arquivo)
        print("Livros carregados com sucesso!\n")
except FileNotFoundError:
    print("Nenhum livro cadastrado ainda.\n")

while True:
    print("---- Cadastrar novo livro ----")
    titulo = input("Título: ")
    autor = input("Autor: ")
    editora = input("Editora: ")
    ano = int(input("Ano da publicação: "))
    genero = input("Gênero: ")
    paginas = int(input("Número de páginas: "))
    idioma = input("Idioma: ")

    livro = {
        "Título": titulo,
        "Autor": autor,
        "Editora": editora,
        "Ano": ano,
        "Gênero": genero,
        "Páginas": paginas,
        "Idioma": idioma
    }

    livros.append(livro)

    print(f"\nLivro '{titulo}' cadastrado com sucesso!")

    continuar = input("Deseja cadastrar outro livro? (s/n): ").lower().upper()
    if continuar != 's':
        break

with open('biblioteca.json', 'w') as arquivo:
    json.dump(livros, arquivo, indent=4)

print("\nTodos os livros foram salvos com sucesso!")