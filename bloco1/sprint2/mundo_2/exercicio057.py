soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher_menos_20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_idade += idade

    # Lógica para o homem mais velho
    # Se for o primeiro homem ou se a idade for maior que a registrada
    if sexo in 'Mm':
        if p == 1 or idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_mais_velho = nome

    # Lógica para mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        total_mulher_menos_20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {total_mulher_menos_20} mulheres com menos de 20 anos.')