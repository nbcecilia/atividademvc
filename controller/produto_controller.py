from model.produto_model import ProdutoModel, UsuarioModel
from view.produto_view import mostrar_produtos, mostrar_usuarios, mensagem, solicitar_dados_usuario, solicitar_id



class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()

    def listar(self):
        try:
            produtos = self.model.listar_produtos()
            mostrar_produtos(produtos)
        except Exception as e:
            mensagem(f"Erro ao listar produtos: {e}")

    def cadastrar(self):
        try:
            nome, preco = solicitar_dados_usuario()
            if not nome or not preco:
                mensagem("Nome e preço são obrigatórios!")
                return
            self.model.inserir_produto(nome, preco)
            mensagem("Produto cadastrado com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao cadastrar produto: {e}")

    def atualizar(self):
        try:
            id_produto = solicitar_id()
            if id_produto is None:
                return
            nome, preco = solicitar_dados_usuario()
            self.model.atualizar_produto(id_produto, nome, preco)
            mensagem("Produto atualizado com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao atualizar produto: {e}")

    def excluir(self):
        try:
            id_produto = solicitar_id()
            if id_produto is None:
                return
            self.model.excluir_produto(id_produto)
            mensagem("Produto excluído com sucesso!")
        except Exception as e:
            mensagem(f"Erro ao excluir produto: {e}")