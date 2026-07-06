lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(lista)
print(lista_par)
print(lista_impar)
    