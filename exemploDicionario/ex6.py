dicio = {}
while True:
    a = str(input('Digite a Chave: '))
    dicio[a] = str(input('Digite o valor: '))
    res = str(input('Deseja continuar S/N: '))

    if res in 'Nn':
        break
print(dicio)