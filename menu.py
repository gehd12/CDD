num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo  numero: '))
opcoes = int(input(f'selecione a operaçao\n'
                   f'1 para soma\n'
                   f'2 para subtraçao\n'
                   f'3 para multiplicaçao\n'
                   f'4 para divisao\n'
                   f'5 para digitar um novo numero\n'
                   f'6 para sair\n'
                   f'digite aqui: '))
while opcoes == 5:
    num1 = int(input('digite o primeiro numero: '))
    num2 = int(input('digite o segundo  numero: '))
    opcoes = int(input(f'selecione a operaçao\n'
                       f'1 para soma\n'
                       f'2 para subtraçao\n'
                       f'3 para multiplicaçao\n'
                       f'4 para divisao\n'
                       f'5 para digitar um novo numero\n'
                       f'6 para sair\n'
                       f'digite aqui: '))
    if opcoes != 5:
        break
if opcoes == 1 :
    soma = (num1+num2)
    print(f"o resultado da soma foi {soma}")
elif opcoes == 2 :
    sub = (num1-num2)
    print(f"o resultado da subtraçao foi {sub}")
elif opcoes == 3 :
    mult = (num1*num2)
    print (f"o resultado da multiplicaçao {mult}")
elif opcoes == 4 :
    divi = (num1/num2)
    print(f"o resultada da divisao foi {divi}")
else:
    print("voce saiu")