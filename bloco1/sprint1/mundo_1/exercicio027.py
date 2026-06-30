nome_completo = input('Digite seu nome completo: ').strip()
lista_nome = nome_completo.split()

print(f'Primeiro nome: {lista_nome[0]}')
print(f'Último nome: {lista_nome[-1]}')