
tot = []
for i in range(4):
    n = int(input(f'Digite o {i+1} valor:  '))
    tot.append(n)
tot = tuple(tot)
print('-' * 20)
print(f'Voce digitou os numeros {tot}')
print(f'o valor 9 apareceu {tot.count(9)} vezes')
if 3 in tot:
    print(f'o valor 3 foi digitado pela primeira vez na posicao {tot.index(3) + 1}')
else:
    print('o valor 3 nao foi digitado')

for numero in tot:
    if numero % 2 == 0:
        print(f'numero par encontrado: {numero}')