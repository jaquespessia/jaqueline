#Eu como um dono de conceaaionária de carros importados, preciso de um sistema para controlar
#meu estoque de veiculos. para me organizar melhor, além do nome gostaria de guaradar o ano, quilometragem,
#marca, preço, cor e quantidade de cada veiculo. quero um menu, onde eu possa cadastrar, alterar, excluir e listar meus veiculos
#para me sentir especial quero que o nome da minha loja apareça no topo do menu 
#nome da loja: moya's imports



import json
NOME_ARQUIVO = 'moya_imports.json'

def carregar_estoque():
    try:
        with open(NOME_ARQUIVO, 'r') as arquivo:
            estoque_veiculos = json.load(arquivo)
            
            proximo_id = 1
            if estoque_veiculos:
                maior_id_encontrado = 0
                for veiculo in estoque_veiculos:
                    if veiculo['id'] > maior_id_encontrado:
                        maior_id_encontrado = veiculo['id']
                proximo_id = maior_id_encontrado + 1
            
            print("Estoque de veículos carregado com sucesso!")
            return estoque_veiculos, proximo_id
    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo de estoque não encontrado ou corrompido. Criando um novo.")
        return [], 1

def salvar_estoque(estoque):
    with open(NOME_ARQUIVO, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)
    print("Estoque salvo!")

def exibir_menu():
    print("=" * 30)
    print("       Moya's Imports")
    print("=" * 30)
    print("\n[1] Cadastrar novo veículo")
    print("[2] Alterar veículo")
    print("[3] Excluir veículo")
    print("[4] Listar veículos")
    print("[5] Sair")
    print("=" * 30)

def cadastrar_veiculo(estoque, proximo_id):
    print("\n--- CADASTRAR NOVO VEÍCULO ---")
    nome = input("Nome do veículo: ")
    marca = input("Marca: ")
    ano = int(input("Ano: "))
    quilometragem = int(input("Quilometragem: "))
    cor = input("Cor: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    novo_veiculo = {
        'id': proximo_id,
        'nome': nome,
        'marca': marca,
        'ano': ano,
        'quilometragem': quilometragem,
        'cor': cor,
        'preco': preco,
        'quantidade': quantidade
    }

    estoque.append(novo_veiculo)
    print(f"\nVeículo '{nome}' cadastrado com sucesso! (ID: {novo_veiculo['id']})")
    
    return estoque, proximo_id + 1

def listar_veiculos(estoque):
    print("\n--- ESTOQUE MOYA'S IMPORTS ---")
    if not estoque:
        print("Nenhum veículo no estoque.")
        return

    for veiculo in estoque:
        print(f"\n[ID: {veiculo['id']}] - {veiculo['nome'].upper()} ({veiculo['marca']})")
        print(f"    Ano: {veiculo['ano']}")
        print(f"    Quilometragem: {veiculo['quilometragem']} km")
        print(f"    Cor: {veiculo['cor']}")
        print(f"    Preço: R$ {veiculo['preco']:.2f}")
        print(f"    Quantidade: {veiculo['quantidade']}")

def alterar_veiculo(estoque):
    listar_veiculos(estoque)
    if not estoque:
        return estoque

    try:
        id_alterar = int(input("\nDigite o ID do veículo que deseja alterar: "))
        veiculo_encontrado = None
        for veiculo in estoque:
            if veiculo['id'] == id_alterar:
                veiculo_encontrado = veiculo
                break

        if veiculo_encontrado:
            print(f"\nAlterando: {veiculo_encontrado['nome'].upper()} (ID: {veiculo_encontrado['id']})")
            veiculo_encontrado['nome'] = input(f"Novo nome ({veiculo_encontrado['nome']}): ") or veiculo_encontrado['nome']
            veiculo_encontrado['marca'] = input(f"Nova marca ({veiculo_encontrado['marca']}): ") or veiculo_encontrado['marca']
            veiculo_encontrado['ano'] = int(input(f"Novo ano ({veiculo_encontrado['ano']}): ") or veiculo_encontrado['ano'])
            veiculo_encontrado['quilometragem'] = int(input(f"Nova quilometragem ({veiculo_encontrado['quilometragem']}): ") or veiculo_encontrado['quilometragem'])
            veiculo_encontrado['cor'] = input(f"Nova cor ({veiculo_encontrado['cor']}): ") or veiculo_encontrado['cor']
            veiculo_encontrado['preco'] = float(input(f"Novo preço ({veiculo_encontrado['preco']:.2f}): ") or veiculo_encontrado['preco'])
            veiculo_encontrado['quantidade'] = int(input(f"Nova quantidade ({veiculo_encontrado['quantidade']}): ") or veiculo_encontrado['quantidade'])
            
            print("\nVeículo alterado com sucesso!")
        else:
            print("ID de veículo não encontrado.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números.")

    return estoque

def excluir_veiculo(estoque):
    listar_veiculos(estoque)
    if not estoque:
        return estoque

    try:
        id_excluir = int(input("\nDigite o ID do veículo que deseja EXCLUIR: "))
        veiculo_removido = None
        
        novo_estoque = [v for v in estoque if v['id'] != id_excluir]

        if len(novo_estoque) < len(estoque):
            for veiculo in estoque:
                if veiculo['id'] == id_excluir:
                    veiculo_removido = veiculo
                    break
            print(f"\nVeículo '{veiculo_removido['nome'].upper()}' (ID: {veiculo_removido['id']}) removido com sucesso!")
            return novo_estoque
        else:
            print("ID de veículo não encontrado.")
            return estoque
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return estoque

def menu():
    estoque_veiculos, proximo_id = carregar_estoque()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            estoque_veiculos, proximo_id = cadastrar_veiculo(estoque_veiculos, proximo_id)
            salvar_estoque(estoque_veiculos)
        elif escolha == '2':
            estoque_veiculos = alterar_veiculo(estoque_veiculos)
            salvar_estoque(estoque_veiculos)
        elif escolha == '3':
            estoque_veiculos = excluir_veiculo(estoque_veiculos)
            salvar_estoque(estoque_veiculos)
        elif escolha == '4':
            listar_veiculos(estoque_veiculos)
        elif escolha == '5':
            print("Saindo do sistema. Obrigado por usar a Moya's Imports!")
            break
        else:
            print("Opção inválida. Tente novamente.")

    menu()