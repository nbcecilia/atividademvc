import psycopg2

class ProdutoModel:
  def __init__(self):
    try:
      self.conexao = psycopg2.connect(
        host="localhost",
        database="meubanco",
        user="postgres",
        password="alunocceia",
      )
    except Exception as e:
      print("Erro ao conectar ao banco:", e)

  def listar_produtos(self):
    try:
      cursor = self.conexao.cursor()
      cursor.execute("SELECT id, nome, preco FROM produtos ORDER BY id;")
      produtos = cursor.fetchall()
      cursor.close()
      return produtos
    except Exception as e:
      print("Erro ao listar produtos:", e)
      return []

  def inserir_produto(self, nome, preco):
    try:
      cursor = self.conexao.cursor()
      cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (%s, %s);",
        (nome, preco),
      )
      self.conexao.commit()
      cursor.close()
      return True
    except Exception as e:
      print("Erro ao inserir produto:", e)
      return False

  def atualizar_produto(self, id_produto, nome, preco):
    try:
      cursor = self.conexao.cursor()
      cursor.execute(
        "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s;",
        (nome, preco, id_produto),
      )
      self.conexao.commit()
      cursor.close()
      return True
    except Exception as e:
      print("Erro ao atualizar produto:", e)
      self.conexao.rollback()
      return False

  def excluir_produto(self, id_produto):
    try:
      cursor = self.conexao.cursor()
      cursor.execute(
        "DELETE FROM produtos WHERE id = %s;",
        (id_produto,),
      )
      self.conexao.commit()
      cursor.close()
      return True
    except Exception as e:
      print("Erro ao excluir produto:", e)
      self.conexao.rollback()
      return False