#Crie uma classe Produto com atributos nome e preco. Crie classes filhas como Livro e Eletronico que herdem da classe Produto e adicionem atributos específicos, como autor e voltagem.

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class livro (produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class eletronico (produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


p1 = livro('Opa', 10.00, "Mafi Boina")
print(p1.nome, p1.preco, p1.autor)