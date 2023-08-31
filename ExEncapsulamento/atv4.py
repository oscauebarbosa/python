#Crie uma classe Livro com atributos de instância titulo, autor, ano e preço de produção. Implemente métodos para obter esses atributos e um método para atualizar o ano do livro. O Atributo preço de produção deve ser privado

class Livro:
    def __init__(self, titulo, autor,ano, precoProducao):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__precoProducao = precoProducao
    def atualizarAno(self,atual):
        self.ano = atual

livro = 'Harry Potter', 'J.K Rowling', 2000, 60.00
print(livro)