notas = {}
continua = True

while continua:
    nota = float(input("Digite a nota: "))
    notas[len(notas) + 1] = nota

    resposta = input("Deseja continuar? (S/N): ")
    if resposta in "Nn":
        break

media = sum(notas.values()) / len(notas)
print("Média:", media)