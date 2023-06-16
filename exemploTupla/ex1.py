fruta = ('Maçã','Banana','Abacaxi','Uva')

fruta2 = ('Laranja','Morango','Melancia')
fruta3 = fruta + fruta2

print(fruta3)

for c in fruta3:
    print(c)

print(fruta3[4])
print(fruta3[0:4])
print(fruta3[1:])
print(fruta3[-1])
print(len(fruta3))

print(sorted(fruta3))
print(fruta3.index('Banana'))
print(fruta3.count('Banana'))

del (fruta3)
print(fruta3)