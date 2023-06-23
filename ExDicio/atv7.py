from random import randint

jogadores = {'Jogador 1': 0, 'Jogador 2': 0, 'Jogador 3': 0, 'Jogador 4' : 0}
jogadores['Jogador 1'] = randint(1,6)
jogadores['Jogador 2'] = randint(1,6)
jogadores['Jogador 3'] = randint(1,6)
jogadores['Jogador 4'] = randint(1,6)

print(jogadores)