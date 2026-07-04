n = s = 0
cont = 0
while True:
    n = int(input('DIgite um numero (999 para parar): '))
    cont += 1
    if n == 999:
        break
    s += n
print(f'A soma dos {cont - 1} foi de {s}')