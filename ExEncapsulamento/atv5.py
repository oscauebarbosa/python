#Crie uma classe Restaurante com atributos de instância nome ,tipo, gasto mensal . Crie métodos para obter esses atributos e um método para mudar o tipo do restaurante. Gasto mensal deve ser um atributo privado.

class restaurante:
    def __init__(self, nome,tipo,gastoMensal):
        self.nome= nome
        self.tipo= tipo
        self.__gastoMensal = gastoMensal

    def atualizarrestaurante(self,tipo2):
        self.tipo=tipo2

p1 = restaurante("Mafi"," - Bar e Restaurante - ", 1000.00)
p1.atualizarrestaurante("Cachorro Quente")
print(p1.nome, p1.tipo)