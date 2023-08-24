#Crie uma classe Veiculo com atributos marca, modelo e ano. Crie classes filhas como Carro e Moto que herdem da classe Veiculo e adicionem atributos específicos.

class veiculo:
    def __init__(self,  marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class carro (veiculo):
    def __init__(self, marca, modelo, ano, portas):

        super().__init__(marca, modelo, ano)
        self.portas = portas

class moto (veiculo):
    def __init__(self, marca, modelo, ano, rodas):

        super().__init__(marca, modelo, ano)
        self.rodas = rodas

v1 = carro('Citroen',"C3", 2023, 4)
print(v1.marca)