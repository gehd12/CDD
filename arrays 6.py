a = [0] * 10
tam = len(a)
cont = 0
for x in range(tam):
    a[x] = int(input('digite um numero: '))
j=int(input('informe outro numero: '))
for i in range(tam):
    if a[i] == j:
        cont += 1
print (cont)