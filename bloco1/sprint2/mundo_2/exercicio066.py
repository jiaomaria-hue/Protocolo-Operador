soma = 0
cont = 0
maior = 0
menor = 0

while True:
    n = int(input('numero: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if resp == 'N':
        break
media = soma / cont
print(f'Média: {media}, Maior: {maior}, Menor: {menor}')
