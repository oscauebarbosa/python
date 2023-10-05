#Escreva uma função que aceite um dia da semana (string) e use o match-case para verificar se é um dia útil ("segunda", "terça", etc.) ou fim de semana ("sábado" ou "domingo"). Retorne uma mensagem apropriada para cada dia.

dia = str (input('Digite o dia da semana: '))

match dia.lower():
    case ("segunda"):
        print('Segunda é um dia de semana!')
    case ("terça"):
        print('Terça é um dia de semana!')
    case ("quarta"):
        print('Quarta é um dia de semana!')
    case ("quinta"):
        print('Quinta é um dia de semana!')
    case("sexta"):
        print('Sexta é um dia de semana!')
    case ("sábado"):
        print('Sábado é fim de semana!')
    case ("domingo"):
        print('Domingo é fim de semana!')