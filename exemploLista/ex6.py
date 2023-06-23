#ver qual fruta tem mais letras

frutas = ['banana','maçã','laranjas','abacaxi']
maior = max (frutas, key=len)
menor = min (frutas, key=len)

print(f'A maior é {maior}')
print(f'A menor é {menor}')