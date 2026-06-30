try:
    # Tudo o que está aqui dentro deve ter um recuo de 4 espaços
    nasc = int(input('Qual o seu ano de nascimento? '))
    idade = 2026 - nasc
    # ... resto do seu código com recuo ...
except ValueError:
    # Este print também precisa de recuo de 4 espaços
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