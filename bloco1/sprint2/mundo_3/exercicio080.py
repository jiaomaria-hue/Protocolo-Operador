lista = []
while True:
    numero = int(input('Digite um valor: '))
    if numero in lista:
        print('Esse valor já existe na lista, nao foi registrado.')
    else:
        print('Valor registrado')
        lista.append(numero)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
lista.sort()
print(f'Vocẽ digitou os valores {lista}')