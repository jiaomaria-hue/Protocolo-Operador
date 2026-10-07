from random import randint
from time import sleep

lista = []

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(0, 5)
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.3) 
    print('PRONTO!')

def somapar():
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
sorteia()
somapar()