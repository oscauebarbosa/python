#Crie uma classe Empregado com atributos nome e salario. Crie uma classe filha Gerente que herde da classe Empregado e adicione um atributo setor.

class Empregado:
    def __init__(self, nome, salario):
        self.nome=nome
        self.salario = salario

class Gerente (Empregado):
    def __init__(self, nome, salario, setor):

        super() . __init__ (nome, salario)
        self.setor = setor

g1 = Gerente('Boina', 10.00, "gerente")
print(g1.nome, g1.salario)