idade= int(input('Insira a idade do nadador: '))

if idade >= 5 and idade <= 7:
    print('Está na turma Infantil A')
elif idade >= 8 and idade <= 11:
    print('Está na turma Infantil B')
elif idade >= 12 and idade <= 13:
    print('Está na turma Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Está na turma Juvenil B')
else:
    print('Está na turma Adultos')

