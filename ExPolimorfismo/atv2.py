#Crie uma classe base chamada Item com atributos nome e preco. Crie duas subclasses, Produto e Servico, que herdam de Item e sobrescrevem o método calcular_valor() para calcular o valor total do produto ou serviço com base em suas características específicas (quantidade para produtos e horas para serviços)

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_valor(self):
        return self.preco

class Produto(Item):
    def __init__(self, nome, preco, quant):
        self.quant = quant
        super().__init__(nome, preco)

    def calcular_valor(self):
        return self.preco * self.quant

class Servico(Item):
    def __init__(self, nome, preco, horas):
        self.horas = horas
        super().__init__(nome, preco)

    def calcular_valor(self):
        return self.preco * self.horas

produto = Produto("Pregos", 10, 1)
servico = Servico("Conserto", 50, 2)

print(f"Valor do produto {produto.nome}: R${produto.calcular_valor()}")
print(f"Valor do serviço {servico.nome}: R${servico.calcular_valor()}")
