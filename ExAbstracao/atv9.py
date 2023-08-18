#Crie uma classe Carro com os atributos marca, modelo e ano. Crie um método chamado mostrar_informacoes que exibe as informações do carro. Instancie um objeto da classe e chame o método.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano= ano


Mitsubishi = Carro('Mitsubishi', 'Lancer Evolution', 2015)
print('O carro é da marca', Mitsubishi.marca)
print('O', Mitsubishi.marca, 'é um', Mitsubishi.modelo)
print('Este veículo é de', Mitsubishi.ano)