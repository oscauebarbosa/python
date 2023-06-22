#Aluno: Cauê Barbosa - Questão: "Batmain"

#para ele conseguir repetir quantas vezes quiser a pergunta
repeticoes = int(input("Repetições: "))

for i in range(repeticoes):

#input para o usuário inserir o nome do vilao
    nome= str(input('Digite o nome do vilão: '))

#nome lower é para o usuário colocar letras maiúsculas e minúsculas e mesmo assim, independentemente, aparecer o nome cadastrado correto!
#então, no print fica a informação se o vilão específico já foi ou não preso!
    if nome.lower() == 'coderinga':
        print('Está cadastrado! Nunca foi preso')

    if nome.lower() == 'pistoleiro':
        print('Está cadastrado! Já foi preso')

    if nome.lower() == 'crocodilo':
        print('Está cadastrado! Nunca foi preso')

    if nome.lower() == 'duas-caras':
        print('Está cadastrado! Já foi preso')

    if nome.lower() == 'espantalho':
        print('Está cadastrado! Já foi preso')