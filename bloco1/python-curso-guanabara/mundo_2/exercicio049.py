n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for i in range(1, 11):
    print(f'{n} x {i:2} = {n*i}')
print('-' * 12)