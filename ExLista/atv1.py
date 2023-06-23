numero = []
while True:
    num = int(input('Digite um número (0 para encerrar): '))
    if num == 0:
        break
    numero.append(num)

soma = sum(numero)
multiplicacao = 1
maior = max(numero)
menor = min(numero)

for num in numero:
    multiplicacao *= num


print(f'Soma:{soma}')
print("Multiplicação: ", multiplicacao)
print(f'A maior é {maior}')
print(f'A menor é {menor}')

