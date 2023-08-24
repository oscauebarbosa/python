#Crie uma classe Bebida com atributos nome e tipo. Crie classes filhas como Refrigerante e Cafe que herdem da classe Bebida e adicionem atributos específicos.

class Bebida:
    def __init__(self, nome, tipo):
        self.nome=nome
        self.tipo = tipo

class Refrigerantec(Bebida):
    def __init__(self,cnome, tipo, preco):

        super().__init__(nome, tipo)
        self.preco = preco

class Cafe (Bebida):
    def __init__(self, nome, tipo, marca):
        super().__init__(nome, tipo)
        self.marca = marca

Bebida1 = Refrigerante('Coca-Cola', "Original", 100.00)
Bebida2 = Cafe('Café', 'Natural', 'Café Birigui')
print(Bebida1.tipo)