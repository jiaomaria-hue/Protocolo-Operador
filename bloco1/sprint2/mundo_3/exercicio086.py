lista = [[], []]
for p in range(0, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print('-=' * 20)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares foram: {lista[1]}')