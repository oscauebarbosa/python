#Crie uma classe Produto com os atributos nome, preco e estoque. Crie um método chamado vender que recebe a quantidade de itens vendidos e atualiza o estoque. Crie um método chamado mostrar_estoque que exibe a quantidade atual em estoque de um produto. Instancie um objeto da classe e realize operações de venda e exibição de estoque.

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        self.estoque -= quantidade

    def mostrar(self):
        print(self.estoque)

produto = Produto('viola', 500, 50)

produto.vender(10)

print(produto.mostrar())