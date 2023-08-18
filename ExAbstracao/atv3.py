#Crie uma classe ContaBancaria com os atributos titular, saldo e numero. Crie métodos para depositar, sacar e exibir o saldo da conta. Crie dois objetos dessa classe e realize operações de depósito e saque.

class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def Depositar(self, valor):
        self.saldo+=valor

    def Sacar(self, valor):
        self.saldo -= valor

    def Saldo(self):
        print(self.saldo)

João = ContaBancaria("João", 100, 500)
João.Depositar(200)
João.Sacar(100)
João.Saldo()
