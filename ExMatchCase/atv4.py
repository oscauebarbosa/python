#Dado o nome de um animal, use o match-case para verificar se é "vaca", "galinha" ou "ovelha". Para qualquer outro animal, retorne "Animal desconhecido".

animal = str(input('Digite o animal: '))


match animal.lower():
    case ('vaca'):
        print('Digitou vaca!')
    case ('galinha'):
        print('Digitou galinha!')
    case ('ovelha'):
        print('Digitou ovelha!')
    case _:
        print('Animal desconhecido!')