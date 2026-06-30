import random

lista = [0, 1, 2, 3, 4, 5]

numero = random.randint(0, 5)

palpite = int(input("Adivinhe o número de 0 a 5: "))

if palpite == numero:
    print("O número está correto!")
else:
    print("O número está errado.")
    print("O número era:", numero)