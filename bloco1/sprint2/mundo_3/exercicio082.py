lista = []
tot_num = 0
while True:
    num = int(input('Digite um numero: ')) 
    lista.append(num)
    tot_num += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'A quantidade de numeros digitados foi {tot_num}')
lista.sort(reverse=True)
print(f'A lista de valores ordenadas em ordem decresente {lista}')
if 5 in lista:
    print('tem o numero 5 na lista')
else:
    print('Nao tem o numero 5 na lista')