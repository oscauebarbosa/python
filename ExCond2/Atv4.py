num1= float(input('Insira o primeiro número: '))
num2= float(input('Insira o segundo número: '))
conta= str(input('Insira a conta desejada (adicao, subtracaoo, divisao ou multiplicacao: '))

adicao= num1 + num2
subtracao= num1 - num2
divisao= num1 / num2
multiplicacao= num1 * num2

if conta == 'adicao':
    print('O valor da adição é', adicao)
elif conta == 'subtracao':
    print('O valor da subtração é', subtracao)
elif conta == 'divisao':
    print('O valor da divisão é', divisao)
elif conta == 'multiplicacao':
    print('O valor da multiplicação é', multiplicacao)



