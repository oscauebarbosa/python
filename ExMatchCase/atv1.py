#Escreva uma função que aceite um número inteiro e use o match-case para verificar se o número é 1, 2, ou 3. Para qualquer outro número, retorne "Outro número".

num = int(input('Digite um número: '))
match num:
    case 1:
        print('Digitou o 1')
    case 2:
        print('Digitou o 2')
    case 3:
        print('Digitou o 3')
    case _:
        print('Outro número')