def piramide(num):
    for x in range(1, num+1):
        for y in range(1, x+1):
            print(x, end='')
        print()

def piramide2(num):
    for x in range(1, num+1):
        for y in range(1, x+1):
            print(y, end='')
        print()

def vogais(texto):
    cont=0
    for x in texto:
        if x in 'aeiouAEIOU':
            cont+=1
    print(cont)