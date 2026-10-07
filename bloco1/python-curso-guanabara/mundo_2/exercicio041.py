try:
    nasc = int(input('Qual o seu ano de nascimento? '))
    idade = 2026 - nasc
except ValueError:
    print('Erro: voce nao digitou um numero.')
if idade <= 9:
    print('Você está na fase mirim.')
elif idade <= 13:
    print('Você está na fase infantil.')
elif idade <= 19:
    print('Você está na fase juvenil.')
elif idade <= 20:
    print('voces esta na fase senior')
else:
    print('voce esta na fase master')