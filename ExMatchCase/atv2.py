#Dado um nome de cor (string), use o match-case para verificar se é "vermelho", "azul" ou "verde". Para qualquer outra cor, retorne "Cor desconhecida".

cor = str(input('Digite a cor: '))


match cor.lower():
    case ('vermelho'):
        print('Digitou vermelho!')
    case ('azul'):
        print('Digitou azul!')
    case ('verde'):
        print('Digitou verde!')
    case _:
        print('Cor desconhecida!')