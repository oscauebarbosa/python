#Crie uma classe Pessoa com atributos nome e idade. Em seguida, crie uma classe Aluno que herde da classe Pessoa e adicione um atributo matricula.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):

        super() . __init__(nome, idade)
        self.matricula = matricula

Boina = Aluno('Mafi Boina', 64, "matriculado")
print(Boina.matricula)