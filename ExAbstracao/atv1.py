#Crie uma classe chamada Pessoa com os atributos nome e idade. Em seguida, crie dois objetos dessa classe representando duas pessoas diferentes.

class Pessoa:
    Nome = ''
    Idade = 0

Pessoa1 = Pessoa()
Pessoa1.Nome = 'João'
Pessoa1.Idade = 16

Pessoa2 = Pessoa()
Pessoa2.Nome = 'Maria'
Pessoa2.Idade = 20

print('O nome da 1° pessoa é', Pessoa1.Nome, 'e o da 2° pessoa é', Pessoa2.Nome)
print('A idade de', Pessoa1.Nome, 'é', Pessoa1.Idade, 'e de', Pessoa2.Nome, 'é', Pessoa2.Idade)

