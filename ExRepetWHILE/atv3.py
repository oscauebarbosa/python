num = 0


while True:
    num = int (input('Digite: '))
    if num == 999:
        print(('Você digitou 999. Processo interrompido!'))
        break

    if num < 0:
        print('Você digitou 0. Processo interrompido!')
        break