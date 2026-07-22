while True:
    t = int(input('Vocẽ quer ver a tabuada de que valor? '))
    if t < 0:
        print('Tabuada encerrada')
        break
    print('-' * 50)
    for c in range(1, 11):
        print(f'{t} x {c:2} = {t * c}')
    print('-' * 50)