notas = [0] * 5
tamanhos =  len(notas)
soma=0
conta=0
for x in range(tamanhos):
    notas[x]=float(input('informe uma nota: '))
for i in range(tamanhos):
    soma += notas[i]
media = soma/tamanhos
for y in range(tamanhos):
    if notas[y]>media:
        conta=conta+1
print(f'a media da sala é {media} e {conta} alunos tem notas acima da media')

