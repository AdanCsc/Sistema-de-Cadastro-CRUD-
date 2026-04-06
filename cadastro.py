usuarios = []

def cadastrar():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()

    if not nome or not idade:
        print("Erro: Nome e idade são obrigatórios.\n")
        return

    usuarios.append({"nome": nome, "idade": idade})
    print("Usuário cadastrado com sucesso!\n")


def listar():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    for i, usuario in enumerate(usuarios):
        print(f"[{i}] Nome: {usuario['nome']} | Idade: {usuario['idade']}")
    print()


def editar():
    print("\n--- Editar Usuário ---")
    listar()

    if not usuarios:
        return

    try:
        indice = int(input("Digite o índice do usuário: "))
        if indice < 0 or indice >= len(usuarios):
            raise IndexError

        novo_nome = input("Novo nome: ").strip()
        nova_idade = input("Nova idade: ").strip()

        if novo_nome:
            usuarios[indice]["nome"] = novo_nome
        if nova_idade:
            usuarios[indice]["idade"] = nova_idade

        print("Usuário atualizado com sucesso!\n")

    except (ValueError, IndexError):
        print("Erro: índice inválido.\n")


def excluir():
    print("\n--- Excluir Usuário ---")
    listar()

    if not usuarios:
        return

    try:
        indice = int(input("Digite o índice para excluir: "))
        if indice < 0 or indice >= len(usuarios):
            raise IndexError

        usuarios.pop(indice)
        print("Usuário removido com sucesso!\n")

    except (ValueError, IndexError):
        print("Erro: índice inválido.\n")


def menu():
    while True:
        print("===== MENU =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            excluir()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    menu()