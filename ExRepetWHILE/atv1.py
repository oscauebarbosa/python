num = 1
qtnotas = 0
soma = 0

while num > 0:
    nota = float(input('Insira a nota (digite um número negativo para parar o processo: '))
    if nota < 0:
        break

    qtnotas +=1
    soma += nota

if qtnotas > 0:
    media = soma / qtnotas
    print(f'A média das notas é:{media}')
else:
    print('Nenhuma nota foi inserida.')