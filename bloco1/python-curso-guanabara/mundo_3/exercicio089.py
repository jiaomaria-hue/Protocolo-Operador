
from random import randint
from time import sleep
jogos = []
temp = []
print('-' * 30)
print('       JOGA NA MEGA SENA')
print('-' * 30)
numS = int(input('Quantos jogos vocẽ quer que eu sorteie? '))
tot = 1
while tot <= numS:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    tot += 1
print('-' * 3, f' Sorteando {numS} JOGOS ', '-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-' * 5, '< BOA SORTE! >', '-' * 5)