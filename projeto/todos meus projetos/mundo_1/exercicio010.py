n1 = float(input('quantos reais voce tem? '))
cotacao = float(input('qual é a contaçao do real pro dola? '))

tl = n1 / cotacao

print(f'voce consegue comprar {tl :.2f} dolares, com {n1} reais')