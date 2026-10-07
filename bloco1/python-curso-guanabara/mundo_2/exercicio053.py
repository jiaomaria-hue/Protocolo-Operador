num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='') # Cor amarela para divisor
        tot += 1
    else:
        print('\033[31m', end='') # Cor vermelha para não divisor
    print(f'{c} ', end='')

print('\n\033[m', end='') # Reseta a cor
print(f'O número {num} foi divisível {tot} vezes.')

if tot == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NÃO é primo.')