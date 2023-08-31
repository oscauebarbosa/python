#Crie uma classe base chamada AnimalAquatico com um método nadando(). Crie duas subclasses, Peixe e Tartaruga, que herdam de AnimalAquatico e sobrescrevem o método nadando() para exibir mensagens diferentes.

class AnimalAquatico:
    def Acao(self):
        pass

class Peixe(AnimalAquatico):
    def Acao(self):
        print('O peixe está nadando')

class Tartaruga(AnimalAquatico):
    def Acao(self):
        print('A tartaruga bate suas nadadeiras')

fish = Peixe()
fish.Acao()

turtle = Tartaruga()
turtle.Acao()