#Dado um login e senha, use o match-case para verificar se eles correspondem a uma das seguintes combinações: ("admin", "admin_pass") ("user", "user_pass") ("guest", _). Retorne uma mensagem apropriada para cada combinação, e uma mensagem de erro se não houver correspondência.

login = str (input('Digite seu Login: '))
senha = str (input('Digite sua Senha: '))

match (login, senha):
    case ("admin", "admin_pass"):
        print('Login: admin | Senha: admin_pass | São cadastrados!')
    case ("user", "user_pass"):
        print('Login: user | Senha: user_pass | São cadastrados!')
    case ("guest", _):
        print('Login: guest | Senha:', senha,'| São cadastrados!')
    case _:
        print('Login ou senha incorreto!')