#Crie uma classe Aluno com os atributos nome, nota1 e nota2. Crie um método chamado calcular_media que retorna a média das notas do aluno. Instancie um objeto da classe e calcule sua média.

class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        mediaNota = (self.nota1 + self.nota2) / 2
        print(f'{self.nome} teve a média de {mediaNota}')

resp = aluno('José Maria', 10, 5)
resp.media()