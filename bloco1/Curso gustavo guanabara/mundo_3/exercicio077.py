listagem = ('Shampoo', 12, 'Escova de dente', 4, 'Refrigerante', 9, 'Pasta de dente', 5)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]}........................: R$ {listagem[i + 1]}')