login = []
senha = []

while True:
    print('MENU\n'
          '1 - CADASTRO\n'
          '2 - LOGIN\n'
          '3 - MOSTRAR USUARIOS CADASTRADOS\n'
          '4 - PARA SAIR\n')

    menu = int(input('Escolha uma opção: '))

    if menu == 1:
        usuario2 = input('Cadastre um suário: ')
        chave = input('Cadastre uma senha: ')
        login.append(usuario2)
        senha.append(chave)
        print('Cadastro realizado com sucesso!')

    elif menu == 2:
        usuario2 = input('Digite seu usuário: ')
        chave = input('Digite sua senha: ')
        if usuario2 in login:
            index = login.index(usuario2)
            if senha[index] == chave:
                print(f'Login realizado com sucesso! Bem-vindo(a), {usuario2}.')
            else:
                print('Erro, senha incorreta.')
        else:
            print('Erro,usuário não encontrado.')

    elif menu == 3:
        if login:
            print('Usuários cadastrados:')
            for i in range(len(login)):
                print(f'Usuário: {login[i]}')
        else:
            print('Nenhum usuário cadastrado, digite um usuário válido.')

    elif menu == 4:
        print('Saindo...')
        break

    else:
        print('Opção inválida!')