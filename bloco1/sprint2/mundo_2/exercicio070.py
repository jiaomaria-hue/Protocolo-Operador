tot_18 = 0
tot_homens = 0
tot_mulheres_20 = 0

while True:
    print('-' * 20)
    print('CADASTRANDO UMA PESSOA')
    print('-' * 20)
    
    # --- BLINDAGEM DA IDADE ---
    while True:
        try:
            idade = int(input('Idade: '))
            if idade >= 0: # Garante que não digitem idades negativas
                break
            else:
                print("Erro! A idade não pode ser negativa.")
        except ValueError:
            print("Erro! Digite apenas números inteiros válidos.")
    
    
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
        
    print('-' * 20)
    
    # --- ANÁLISE DOS DADOS ---
    if idade > 18:
        tot_18 += 1
        
    if sex == 'M':
        tot_homens += 1
        
    if sex == 'F' and idade < 20:
        tot_mulheres_20 += 1
    
    # --- BLINDAGEM DA PARADA ---
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if cont == 'N':
        break

print('=' * 20)
print(f'Total de pessoas com mais de 18 anos: {tot_18}')
print(f'Ao todo temos {tot_homens} homens cadastrados.')
print(f'E temos {tot_mulheres_20} mulheres com menos de 20 anos.')