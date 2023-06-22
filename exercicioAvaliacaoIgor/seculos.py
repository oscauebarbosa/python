#Aluno: Cauê Barbosa - Questão: "Exercício de História"

#Aqui é uma entrada clássica para o usuário inserir o ano.
ano= int(input('Insira o ano do século que quer descobrir: '))

#Aqui no "If" usei o % pra ver se o número inserido era divisível por 100.
#Se o resto da divisão por 100 for zero, é um ano múltiplo de 100.
#Então, já que é divisível, divide o ano por 100, aí já dá o resultado do século e mostra no print.
if ano % 100 == 0:
    sec = ano // 100

#Aqui serve só se o número não for divisível por 100, sendo ímpar, ai soma 1, para o tornar par novamente99.
else:
    sec = ano // 100 + 1

print('Século', sec)
