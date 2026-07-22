
soma = 0
contador = 0
while True:
    n = int(input('Digite um numero: '))

    if n == 999:
        break

    soma += n
    contador += 1

print(f'Vocẽ digitou {contador} numeros e a soma entre eles é {soma}')