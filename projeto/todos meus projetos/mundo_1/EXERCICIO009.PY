n1 = int(input('digite um numero: '))

m1 = n1 * 1
m2 = n1 * 2
m3 = n1 * 3
m4 = n1 * 4
m5 = n1 * 5
m6 = n1 * 6
m7 = n1 * 7
m8 = n1 * 8
m9 = n1 * 9
m10 = n1 * 10

print (f'a multiplicaçao de {n1} vezes 1: {m1}, vezes 2: {m2}, vezes 3: {m3}, 4: {m4}, 5: {m5}, 6: {m6}, 7: {m7}, 8: {m8}, 9: {m9}, 10: {m10}')

# ou 

# Em vez de criar m1, m2, m3...
# Use um loop para fazer o trabalho para você:
n1 = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{n1} x {i} = {n1 * i}")