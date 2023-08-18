#Crie uma classe Cachorro com os atributos nome e idade. Crie um método chamado latir que imprima "Woof!" quando chamado. Instancie um objeto da classe Cachorro e chame o método latir.

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Latir(self):
        print("Woof!")
    def Andando(self):
        print(f"{self.nome} esta andando")


Dog = Cachorro("Bob", 5)

Dog.Latir()
Dog.Andando()


