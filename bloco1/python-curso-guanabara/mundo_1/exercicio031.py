viagem = int(input('qual a distancia em km a viagem? '))
valor_por_200 = 0.50
valor_mais_longo = 0.45
n1_200 = viagem * valor_por_200
n2_longo = valor_mais_longo * viagem
if viagem <= 200:
    print(f'vai dar {n1_200} o total de km')
else:
    print(f'vai dar {n2_longo} o valor total, de km.')