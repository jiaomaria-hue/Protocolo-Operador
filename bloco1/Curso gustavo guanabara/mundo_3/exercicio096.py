time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    gols.clear()  
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    for c in range(partidas):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
        
    jogador['gols'] = gols[:]  
    jogador['total'] = sum(gols)  
    time.append(jogador.copy())  
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=' * 60)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3} {v["nome"]:<15} {str(v["gols"]):<15} {v["total"]:<5}')
print('=' * 60)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 60)

print('<< VOLTE SEMPRE >>')