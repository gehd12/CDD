a = [0] * 10
tamanhos = len(a)
x=['']
m = [0]*10
for x in range(tamanhos):
    a[x]=int(input('infrome um numero: '))
x=int(input('informe o numero de x: '))
for i in range(tamanhos):
    m[i]=a[i]*x

print(a)
print(x)
print(m)


