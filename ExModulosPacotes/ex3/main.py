from jogo_da_sorte import *

sortear = numero_secret()
tentativas = 0


while True:
    tentativa = int(input('Digite a sua tentativa: '))
    tentativas += 1
    if tentativa < sortear:
        print("Tente um número maior!")

    elif tentativa > sortear:
        print('Tente um número menor! ')

    else:
        print('Parabéns! Acertou! ')