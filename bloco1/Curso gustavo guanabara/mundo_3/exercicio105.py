def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! digite um numero inteiro valido')
        if ok:
            break
    return valor
# programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar um numero {n}')