dicio = {}
dicio['nome'] = str(input('Nome: '))
dicio['media'] = float(input(f'Media da {dicio["nome"]}: '))
print('-' * 20)
print(f'Nome é igual a {dicio['nome']}')
print(f'Media é igual a {dicio["media"]}')
if dicio['media'] >= 7:
    print('Esta aprovada de ano')
else:
    print('Esta reprovada de ano')
print('-' * 20)