def ficha(jg='<desconhecido>', gol=0):
    print(f'o jogador {jg} fez {gol} gol(s) no campeonato.')
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)