def adicionar():
    try:
        nome = input("Digite o nome do usuário: ")
        with open("usuarios.txt", "a") as f:
            f.write(nome + "\n")
        print("Usuário adicionado com sucesso!")
    except Exception as e:
        print("Erro ao adicionar usuário:", e)

def listar():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines() #[JAQUE, PAULO, GABRIEL]
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for u in usuarios:
            print(u.strip())
    except FileNotFoundError:
        print("Nenhum usuário cadastrado.")

def alterar():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines()
        if not usuarios:
            print("Nenhum usuário para alterar.")
            return
        listar()
        i = int(input("Número do usuário para alterar: ")) - 1
        if i < 0 or i >= len(usuarios):
            print("Número inválido.")
            return
        novo = input("Digite o novo nome: ")
        usuarios[i] = novo + "\n"
        with open("usuarios.txt", "w") as f:
            f.writelines(usuarios)
        print("Usuário alterado com sucesso!")
    except Exception as e:
        print("Erro ao alterar usuário:", e)

def excluir():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines()
        if not usuarios:
            print("Nenhum usuário para excluir.")
            return
        listar()
        i = int(input("Número do usuário para excluir: ")) - 1
        if i < 0 or i >= len(usuarios):
            print("Número inválido.")
            return
        usuarios.pop(i)
        with open("usuarios.txt", "w") as f:
            f.writelines(usuarios)
        print("Usuário excluído com sucesso!")
    except Exception as e:
        print("Erro ao excluir usuário:", e)

def menu():
    while True:
        print("\n1. Adicionar\n2. Listar\n3. Alterar\n4. Excluir\n5. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            adicionar()
        elif op == "2":
            listar()
        elif op == "3":
            alterar()
        elif op == "4":
            excluir()
        elif op == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

#adicionar()
#Pede que o usuário digite um nome.
#Abre o arquivo "usuarios.txt" no modo append ("a").
#Escreve o nome digitado no arquivO.
#Exibe mensagem de sucesso.
#Se ocorrer algum erro (por exemplo, problema no arquivo), mostra uma mensagem de erro.

#listar()
#Lê todas as linhas do arquivo e armazena numa lista.
#Exibe cada usuário numerado.
#Se o arquivo não existir ou estiver vazio, exibe mensagem indicando que não há usuários cadastrados.

#alterar()
#Lê todas as linhas do arquivo para uma lista.
#Chama a função listar() para mostrar os usuários e ajudar na escolha.
#Pede para o usuário digitar o número do usuário que deseja alterar.
#Pede o novo nome.
#Substitui o nome escolhido na lista.
#Exibe mensagem de sucesso ou erro.

#excluir()
#Pede o número do usuário que deseja excluir.
#Remove o usuário escolhido da lista.
#Reabre o arquivo no modo escrita para salvar a lista atualizada.
#Exibe mensagem de sucesso ou erro.

#menu()
#Exibe um menu com opções para o usuário escolher o que fazer.
#Recebe a opção digitada.
#Chama a função correspondente à opção escolhida.
#Continua mostrando o menu até o usuário escolher sair (opção 5).
#Se a opção digitada for inválida, exibe uma mensagem de erro.
#A última linha menu() inicia o programa exibindo o menu e permitindo interação com o usuário.

#Como o usuário é alterado no arquivo?
#O programa lê todos os usuários do arquivo para uma lista.
#Mostra os usuários numerados para o usuário escolher qual alterar.
#Recebe o número escolhido e o novo nome.
#Substitui o nome na lista.
#Reescreve o arquivo inteiro com a lista atualizada

