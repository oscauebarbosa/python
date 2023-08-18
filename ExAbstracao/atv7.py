#Crie uma classe Produto com os atributos nome, preco e quantidade. Crie um método chamado calcular_total que retorna o valor total do estoque desse produto. Instancie um objeto da classe e calcule o valor total.

class Produto:
    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade
    def total(self):
        return self.preco * self.quantidade

valor_total = Produto(20,5)

tot = valor_total.total()

print(f'O valor total do produto é R${tot}')