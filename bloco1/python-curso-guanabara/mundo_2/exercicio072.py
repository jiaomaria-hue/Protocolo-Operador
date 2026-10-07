montante = int(input('Digite o valor a ser sacado: '))
atual = 50
total_notas = 0
while True:
    if montante >= atual:
        total_notas += 1
        montante -= atual
    else:
        if total_notas > 0:
            print(f'O total de {total_notas} cedulas de R$ {atual}')
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 1
        total_notas = 0
        if montante == 0:
            break