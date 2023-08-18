#Crie uma classe Pessoa com os atributos nome, idade e sexo. Crie um método chamado mostrar_detalhes que exibe as informações da pessoa. Instancie um objeto da classe e chame o método.

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


mostrar_detalhes = Pessoa('Aparecida', 70, 'Feminino')
print('O nome da pessoa cadastrada é', mostrar_detalhes.nome)
print(mostrar_detalhes.nome, 'tem', mostrar_detalhes.idade, 'anos de idade')
print('O sexo de', mostrar_detalhes.nome,  'é', mostrar_detalhes.sexo)
