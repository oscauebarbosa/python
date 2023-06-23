num = []

for i in range(5):
    valor = int(input("Digite um número: "))
    num.append(valor)

num_ordem = sorted(num)

print("Valores digitados: ", num)
print("Valores ordenados: ", num_ordem)
