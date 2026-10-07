tot_gasto = 0  
tot_1000 = 0
barato_nome = ''
menor_preço = 0  


primeiro = True 

while True:
    nom_pro = str(input('Digite o nome do produto: ')).strip()
    preço = int(input('Digite o preço do produto: '))
    
    
    tot_gasto += preço
    
    
    if preço > 1000:
        tot_1000 += 1
        
    
    if primeiro or preço < menor_preço:
        menor_preço = preço
        barato_nome = nom_pro
        primeiro = False 
        
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if cont == 'N':
        break

print(f'Total gasto: R$ {tot_gasto}')
print(f'Produtos mais caros que R$1000: {tot_1000}')
print(f'O produto mais barato foi {barato_nome} por R$ {menor_preço}')