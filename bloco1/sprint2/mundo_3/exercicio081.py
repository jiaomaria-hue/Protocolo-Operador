lista = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(F'Adicionado na posiçao {pos} da lista')
                break 
            pos += 1
print(f'os valores digidatos em ordem foram {lista}')