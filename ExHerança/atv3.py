#Crie uma classe Forma com atributos largura e altura. Crie classes filhas como Retangulo e Triangulo que herdem da classe Forma e adicionem métodos para calcular a área.

class Forma:
    def __init__(self, largura,altura):
        self.largura=largura
        self.altura=altura

class Retangulo(Forma):
    def __init__(self,largura,altura):
        super().__init__(largura,altura)
    def calcular_area(self):
        area=self.largura*self.altura
        return area

class Triangulo(Forma):
    def __init__(self,largura,altura):
        super().__init__(largura,altura)
    def calcular_area(self):
        area=self.largura*self.altura/2
        return area

t= Retangulo(5,10)
print(t.calcular_area())