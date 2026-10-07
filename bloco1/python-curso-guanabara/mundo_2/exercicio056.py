totmaior = 0
totmenor = 0
for c in range(1, 5 + 1):
    peso = int(input(f'pessoa {c} qual é seu peso em kg? '))
    if peso > 60:
        totmaior += peso
    else:
        totmenor += peso
print(f'peso maior total foi {totmaior}')
print(f'peso menor total foi {totmenor}')
