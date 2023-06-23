fruta = ['Maçã','Banana','Abacaxi','Uva']

#adicionar a fruta no final da lista
fruta.append ('Laranja')

#inserir a fruta no lugar 1 sem tirar as outras
fruta.insert (1,'Morango')

#apagar a fruta 3 - outras maneiras:
#fruta.pop(3)
#fruta.remove('Abacaxi')
del fruta[3]

#apaga o último elemento
fruta.pop()

print(fruta)
