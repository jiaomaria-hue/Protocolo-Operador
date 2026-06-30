from datetime import date
atual = date.today().year
totmaior = 0
totmenos = 0
for c in range(1, 6 + 1):
    nasc = int(input(f'Em que ano a {c}¹ pessoa nasceu? '))
    idade = nasc - atual
    if idade >= 18:
        totmaior += 1
    else:
        totmenos += 1
print(f'ao todo tivemos {totmaior} pessoas de maior')
print(f'ao todo tivemos {totmenos} pessoas de menor')
    
    