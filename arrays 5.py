nome = [0] * 5
senha = [0] * 5
tam = len(nome)
x=['']
for x in range(tam):
    nome[x] = input('digite um nome: ')
    senha[x] = input('digite a senha: ')
for i in range(tam):
    print(i, nome[i],  senha[i])

