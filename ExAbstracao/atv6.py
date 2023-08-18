#Crie uma classe Lampada com um atributo ligada (booleano). Crie métodos para ligar, desligar e verificar o estado da lâmpada. Instancie um objeto da classe e realize operações de ligar e desligar.

class Lampada:
    def __init__(self, nome, on):
        self.nome = nome
        self.estado = on

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.estado = False

    def exibir(self):
        if self.estado:
            print('A lâmpada está acesa!')
        else:
            print('A lâmpada está apagada!')


lampQuarto = Lampada("Quarto", False)
lampSala = Lampada("Sala", False)
lampCozinha = Lampada("Cozinha", False)

lampadas = {
    "quarto": lampQuarto,
    "sala": lampSala,
    "cozinha": lampCozinha
}

while True:
    Comodos = input('Digite o cômodo em que deseja acender ou apagar a lâmpada (ou "sair" para encerrar): ')

    if Comodos.lower() == "sair":
        break

    lampada = lampadas.get(Comodos.lower())

    if lampada:
        lampada.exibir()
        acao = input("Digite 'ligar' para acender ou 'desligar' para apagar a lâmpada: ")

        if acao.lower() == "ligar":
            if not lampada.estado:
                lampada.ligar()
                print("Lâmpada acesa!")
            else:
                print("A lâmpada já está acesa.")
        elif acao.lower() == "desligar":
            if lampada.estado:
                lampada.desligar()
                print("Lâmpada apagada!")
            else:
                print("A lâmpada já está apagada.")
        else:
            print("Cômodo inválido!")
    else:
        print("Cômodo inválido!")



