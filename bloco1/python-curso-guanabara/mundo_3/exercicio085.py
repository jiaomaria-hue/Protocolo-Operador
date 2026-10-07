galera = list()
dado = list()
totmaipes = totmenpes = 0
totcas = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('peso: ')))
    totcas += 1
    galera.append(dado[:])
    dado.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
lista_pesos = []
for p in galera:
    lista_pesos.append(p[1])
maior = max(lista_pesos)
menor = min(lista_pesos)
nomes_pesados = []
for p in galera:
    if p[1] == maior:
        nomes_pesados.append(p[0])
nomes_magros = []
for p in galera:
    if p[1] == menor:
        nomes_magros.append(p[0])
print('-=' * 20)
print(f'Ao todo, vocẽ cadastrou {totcas} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de {nomes_pesados}')
print(f'O menor peso foi de {menor}Kg. Peso de {nomes_magros}')