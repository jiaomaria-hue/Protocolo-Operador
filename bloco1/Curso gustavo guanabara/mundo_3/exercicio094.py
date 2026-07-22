jogador = {}
gols = []
total = 0


jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(partidas):
    gol = int(input(f'Quantos gols na partida {c}? '))
    gols.append(gol)
    total += gol  

jogador['gols'] = gols
jogador['total'] = total

print('=' * 80)
print(jogador)
print('=' * 80)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('=' * 80)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i, g in enumerate(gols):
    print(f'    => Na partida {i}, fez {g} gols.')

print(f'Foi um total de {total} gols.')   