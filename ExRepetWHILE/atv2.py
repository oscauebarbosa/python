soma = 0
qtnum = 0

while True:
    num = float(input('Insira um número (digite 0 para parar): '))
    qtnum += 1

    if num == 0:
        break
    elif num % 2 == 0:
        soma += num

print(f'A soma dos números pares é:{soma}')
