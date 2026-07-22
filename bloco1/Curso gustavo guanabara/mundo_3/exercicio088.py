matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_te_con = 0
maior_seg_linha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-' * 20)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()

print('-' * 20)

for l in range(0, 3):
    soma_te_con += matriz[l][2] 
maior_seg_linha = matriz[1][0]  
for c in range(1, 3):           
    if matriz[1][c] > maior_seg_linha:
        maior_seg_linha = matriz[1][c]

print(f'A soma de todos os valores pares digitados é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_te_con}')
print(f'O maior valor da segunda linha é: {maior_seg_linha}')