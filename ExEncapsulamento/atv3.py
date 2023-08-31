#Crie uma classe Carro com atributos privados: marca e modelo. Crie métodos para obter esses atributos e um método para alterar o modelo do carro.

class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def exibir(self):
        print(self.modelo, self.marca)

    def alterar_modelo(self):
        mudar = input()
        self.modelo = mudar
        print(self.modelo)


car = Carro("Lancer", "carro")
car.alterar_modelo()