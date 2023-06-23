num = []
while True:
    numero = int(input('Digite um número (0 para encerrar): '))

    if numero == 0:
        break

    if numero not in num:
        num.append(numero)


num.sort()

print('Ordem crescente:')
for numero in num:
    print(numero)
