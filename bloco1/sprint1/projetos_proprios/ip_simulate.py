P = input('DIGITE O IP DO SEU ALVO: ')
p1 = '192.0556'

print(f'o ip do seu alvo foi cadastrado. iniciando analise, OPERADOR...')

if P == '192.046':
    print('IP errado.')
elif P == '192.0556':
    print(f'IP encontrado: {p1[:8]}')
else:
    print('IP não reconhecido.')