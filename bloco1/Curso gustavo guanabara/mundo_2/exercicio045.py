import random # Essa biblioteca gera o comportamento "imprevisível"

# 1. Defina as opções
itens = ('Pedra', 'Papel', 'Tesoura')

# 2. Computador escolhe (Atacante)
computador = random.randint(0, 2) 

# 3. Você escolhe (Defensor)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

# 4. Lógica de comparação (O núcleo do sistema)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

if computador == jogador:
    print('EMPATE')
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU')