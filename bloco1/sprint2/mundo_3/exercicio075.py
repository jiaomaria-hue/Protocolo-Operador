import random

numeros = tuple(random.choices(range(10), k=5))

print(f'Números gerados: {numeros}')
print(f'O menor número é {min(numeros)}')
print(f'O maior número é {max(numeros)}')