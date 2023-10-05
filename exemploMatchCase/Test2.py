login = str (input('Digite seu Login: '))
senha = str (input('Digite sua Senha: '))

match (login, senha):
    case ('Caue', '123'):
        print('Logado com sucesso!')
    case _:
        print('Login ou senha incorreto')