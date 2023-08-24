#Crie uma classe Instrumento com um método tocar(). Crie classes filhas como Violino, Piano e Flauta que herdem da classe Instrumento e sobrescrevam o método tocar().

class Instrumento:
    def tocar(self):
        return 'Tocando o instrumento'

class violino (Instrumento):
    def tocar(self):
        return 'Tocando o violino'

class piano (Instrumento):
    def tocar(self):
        return 'Tocando o piano'

class flauta (Instrumento):
    def tocar(self):
        return 'Tocando a flauta'

violino = violino()
piano = piano()
flauta = flauta()

print(violino.tocar())
print(piano.tocar())
print(flauta.tocar())
