homemOld = " "
idadeHomemOld = 0
mulherMenos20 = []

for i in range(3):
    nome = input(f'Digite o nome da pessoa {i+1}: ')
    idade = int (input(f'Digite a idade da pessoa {i + 1}: '))
    sexo = input(f'Digite o sexo da pessoa {i + 1} (M ou F): ')

    if sexo.upper() == "M" and idade > idadeHomemOld:
        homemOld = nome
        idadeHomemOld = idade

    if sexo.upper() == "F" and idade < 20:
        mulherMenos20.append(nome)

print(f"\nO homem mais velho é {homemOld}")

print('As mulheres mais novas são',mulherMenos20)




