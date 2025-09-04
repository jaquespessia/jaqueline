#Contexto: A biblioteca precisa de um sistema para catalogar os livros da escola.
#Crie um sistema que salve e liste os livros que devem ser salvos no arquivo
#biblioteca.json

#Atributos necessarios
#titulo, autor, editora, ano_publicado, genero, numero_paginas, idioma


import json
ARQUIVO = "biblioteca.json"

def carregar_livros():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_livros(livros):
    with open(ARQUIVO, "w") as f:
        json.dump(livros, f, indent=4)

def adicionar_livro():
    livro = {
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "editora": input("Editora: "),
        "ano_publicado": input("Ano de Publicação: "),
        "genero": input("Gênero: "),
        "numero_paginas": input("Número de Páginas: "),
        "idioma": input("Idioma: ")
    }

    livros = carregar_livros()
    livros.append(livro)
    salvar_livros(livros)
    print(" Livro adicionado com sucesso!\n")

def listar_livros():
    livros = carregar_livros()
    if not livros:
        print(" Nenhum livro cadastrado.\n")
        return
    print("\n Lista de Livros:")
    for i, livro in enumerate(livros, 1):
        print(f"\nLivro {i}:")
        for chave, valor in livro.items():
            print(f"  {chave}: {valor}")
    print()

def menu():
    while True:
        print("=== Biblioteca Escolar ===")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

menu()