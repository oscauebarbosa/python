#Crie uma classe Cliente com atributo privado código. Implemente métodos para obter e definir o código do cliente.

class Cliente:
    def __init__(self, codigo):
        self.__codigo = codigo
    def MostrarCodigo(self):
            print(self.__codigo)
a = Cliente(10)
a.MostrarCodigo()