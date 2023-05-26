valor= float(input('Insira o valor: '))
taxa= float(input('Insira o valor da taxa: '))
tempo= int(input('Insira o tempo: '))

prestacao = valor + (valor * (taxa / 100) * tempo)

print('O valor da prestação é:', prestacao)

