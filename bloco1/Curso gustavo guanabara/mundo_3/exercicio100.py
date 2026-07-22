from time import sleep
def maior(* num):
    print('-' * 20)
    print('Analisando os valores passados.')
    sleep(1)
    for valor in num:
        print(f'{valor} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        maior_valor = max(num)
    else:
        maior_valor = 0
        
    print(f'O maior valor informado foi {maior_valor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('-=' * 30)