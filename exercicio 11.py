hora01 = int(input('digite  a primeira hora'))
min1 = int(input('digite o primeiro minuto'))
hora02 = int(input('digite a 2 hora'))
min2 = int(input('digite a 2 min'))

soma1 = min1+min2
mintotal = soma1 % 60
hora = hora01+hora02
horas = hora % 12
horaadd = horas+1

if soma1 > 60:
    print(f"{horaadd}:0{mintotal}")
else:
    print(f"{horas:0{mintotal}}")
