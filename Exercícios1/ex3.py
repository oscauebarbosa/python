salario= float(input('Insira o valor do salário atual:'))
percentual= float(input('Insira o percentual de aumento:'))

aumento= percentual*salario
divisao= aumento/100
atual= salario+divisao

print('o valor atualizado é:', atual)
