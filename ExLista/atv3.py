numero = []
while True:
    num = int(input('Digite um número (0 para encerrar): '))
    if num == 0:
        break
    numero.append(num)


soma = sum(numero)

menor = min(numero)

print(f'Soma:{soma}')
print(f'A menor é {menor}')