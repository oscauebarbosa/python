def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b

while True:
    print("==== Menu ====")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Subtrair")
    print("4 - Divisão")
    print("5 - Sair do Programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        print("Programa encerrado.")
        break

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if opcao == 1:
        resultado = somar(valor1, valor2)
        print(f"A soma dos valores é: {resultado}")
    elif opcao == 2:
        resultado = multiplicar(valor1, valor2)
        print(f"O produto dos valores é: {resultado}")
    elif opcao == 3:
        resultado = subtrair(valor1, valor2)
        print(f"A subtração dos valores é: {resultado}")
    elif opcao == 4:
        if valor2 != 0:
            resultado = dividir(valor1, valor2)
            print(f"A divisão dos valores é: {resultado}")
        else:
            print("Erro: divisão por zero!")
    else:
        print("Opção inválida. Tente novamente.")