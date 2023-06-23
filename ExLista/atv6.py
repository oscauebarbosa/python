numeros = []
while True:
    num = int(input('Digite um número (0 para encerrar): '))
    if num == 0:
        break
    numeros.append(int(num))

nao = ""

if 5 not in numeros:
    nao = "não"

print('Quantidade de números: ', len(numeros))
print('Valores em ordem decrescente: ', sorted(numeros, reverse=True))
print(f'O valor 5 {nao} está na lista.')





