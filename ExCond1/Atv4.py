nascimento = int(input('Digite o ano de nascimento: '))

atual = 2023

idade= atual - nascimento

if idade <= 17:
    print(f'Você é menor de idade, tendo {idade} anos')
else:
    print(f'Você é maior de idade, tendo {idade} anos')