#Crie uma classe Retangulo com os atributos base e altura. Crie um método chamado calcular_area que retorna a área do retângulo. Instancie um objeto da classe e calcule sua área.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

ret = Retangulo(2,8)

area = ret.calcular_area()

print(area)