import json

produtos = []
categorias = []

id_categoria = 0
id_produto = 0

def carregar_arquivo(arquivo):
    try:
        with open(arquivo, "r") as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return []

def salvar_arquivo(arquivo, dados):
    with open(arquivo, "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

def exibir_menu():
    print("\n......... Loja Eletrônico .........")
    print("1. Cadastrar Categoria")
    print("2. Listar Categorias")
    print("3. Cadastrar Produto")
    print("4. Listar Produtos")
    print("5. Sair")

def listar_categorias():
    if categorias:
        print("CATEGORIAS:")
        for categoria in categorias:
            print(f"ID: {categoria['id_categoria']} - Nome: {categoria['nome_categoria']}")
    else:
        print("Nenhuma categoria cadastrada.")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return
    
    print("PRODUTOS:")
    for produto in produtos:
        nome_categoria = "Categoria Desconhecida"
        for categoria in categorias:
            if categoria["id_categoria"] == int(produto["id_categoria_associada"]):
                nome_categoria = categoria["nome_categoria"]
                break

        print(f"\nID: {produto['id_produto']}")
        print(f"Nome: {produto['nome_produto']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Categoria: {nome_categoria}")

def cadastrar_categoria():
    global id_categoria
    print("\n/cadastrar categoria:")
    nome_categoria = input("Nome: ")
    id_categoria += 1

    nova_categoria = {
        "nome_categoria": nome_categoria,
        "id_categoria": id_categoria
    }

    categorias.append(nova_categoria)
    print(f"Categoria '{nome_categoria}' cadastrada com sucesso!")

def cadastrar_produto():
    global id_produto
    if not categorias:
        print("Cadastre uma categoria antes de cadastrar um produto.")
        return

    print("\n/cadastrar produto:")
    id_produto += 1
    nome_produto = input("Nome: ")

    try:
        preco = float(input("Preço: "))
    except ValueError:
        print("Preço inválido! Definindo como 0.0")
        preco = 0.0

    listar_categorias()
    id_categoria_associada_input = input("ID da categoria associada: ")

    try:
        id_categoria_associada = int(id_categoria_associada_input)
    except ValueError:
        print("ID da categoria inválido. Produto não cadastrado.")
        id_produto -= 1
        return

    categoria_encontrada = False
    for categoria in categorias:
        if categoria["id_categoria"] == id_categoria_associada:
            categoria_encontrada = True
            break

    if not categoria_encontrada:
        print("Categoria não encontrada. Produto não cadastrado.")
        id_produto -= 1
        return

    novo_produto = {
        "nome_produto": nome_produto,
        "id_produto": id_produto,
        "preco": preco,
        "id_categoria_associada": id_categoria_associada
    }

    produtos.append(novo_produto)
    print(f"Produto '{nome_produto}' cadastrado com sucesso!")

while True:
    exibir_menu()
    opcao = input("Escolha: ")

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        listar_categorias()
    elif opcao == '3':
        cadastrar_produto()
    elif opcao == '4':
        listar_produtos()
    elif opcao == '5':
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida.")
