Res = 'S'
while Res == 'S':
    num = int (input('Digite: '))
    if num == 999:
        print(('Número muito grande'))
        break
    Res = str (input('Deseja continuar? (S/N): '))