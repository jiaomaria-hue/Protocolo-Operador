soma = 0
for c in range(1, 7):
    num = int(input(f'digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
print(f'a soma é {soma}')