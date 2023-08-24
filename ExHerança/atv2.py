#Crie uma classe Animal com um método fazer_som(). Em seguida, crie classes filhas como Cachorro, Gato e Vaca que sobrescrevam o método fazer_som().

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print('som')

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def fazer_som(self):
        print("Wolf!")

Bob = Cachorro("bob")
Bob.fazer_som()