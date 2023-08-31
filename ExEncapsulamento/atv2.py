#Crie uma classe Conta com atributos: saldo(privado) e titular(publico). Implemente métodos para depositar e sacar

class Conta:
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.titular = titular
        print(self.__saldo)

    def sacar(self, saque):
        self.__saldo -= saque

    def depositar(self, deposito):
        self.__saldo += deposito

    def Exibir(self):
        print(self.__saldo)

a = Conta(1000.00, "João")
a.sacar(100)
a.Exibir()
