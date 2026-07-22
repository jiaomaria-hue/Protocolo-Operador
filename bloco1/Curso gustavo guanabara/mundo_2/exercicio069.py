from random import randint

vitorias = 0

while True:
    jogador_num=int(input('Diga um valor: '))
    computador_num = randint(0, 10)
    total = jogador_num + computador_num
    
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Impar? [P/I]: ').strip().upper()[0]
    print('-' * 40)
    print(f'Vocẽ jogou {jogador_num} e o computador {computador_num}. total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-' * 40)

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!!')
            vitorias += 1
        else:
            print("VOCE PERDEU")
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('VOCE VENCEU!!')
            vitorias += 1
        else:
            print('VOCE PERDEU!!!')
            break
    print('Vamos jogar novamente...')
    print('=' * 40)

print(f'GAME OVER! Vocẽ venceu {vitorias} vezes')