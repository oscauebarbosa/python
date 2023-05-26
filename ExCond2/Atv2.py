compra= float(input('Insira o valor: '))
prestacoes= int(input('Insira o valor da taxa: '))

valor = compra / prestacoes

if valor > 500:
    print('Você não consegue pagar!')
else:
    print('Você consegue pagar!')

