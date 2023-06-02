totalgasto = 0
produtocaro = ""
precocaro = 0

while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    totalgasto += preco

    if preco > precocaro:
        produtocaro = produto
        precocaro = preco

    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() != "s":
        break

print(f"\nTotal gasto na compra: R${totalgasto:.2f}")
print(f"Produto mais caro: {produtocaro} (R${precocaro:.2f})")