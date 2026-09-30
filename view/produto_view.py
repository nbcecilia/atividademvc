def menu_principal():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Listar produtos cadastrados")
    print("2 - Cadastrar um novo produto (nome e preço)")
    print("3 - Atualizar os dados de um produto existente")
    print("4 - Excluir um produto pelo ID")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def mostrar_produtos(lista):
    print("\n=== Lista de Produtos ===")
    if not lista:
        print("Nenhum produto encontrado.")
    else:
        for produto in lista:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: {produto[2]}")


def solicitar_dados_produto():
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    return nome, preco

def mensagem(texto):
    print(texto)

def solicitar_id():
    try:
        return int(input("Informe o ID do produto: "))
    except ValueError:
        print("ID inválido! Deve ser um número inteiro.")
        return None