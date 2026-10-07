try:
    nasc = int(input('Qual o seu ano de nascimento? '))
    idade = 2026 - nasc
    serv_militar = 18
except ValueError:
    print('Erro: voce nao digitou um numero.')
else:
    if idade > serv_militar:
        anos_passados = idade - serv_militar
        print(f'Voce já passou da idade de se alistar. Voce tem {idade} anos e já se passaram {anos_passados} anos do prazo.')
    elif idade < serv_militar:
        anos_faltantes = serv_militar - idade
        print(f'Voce ainda vai se alistar. Voce tem {idade} anos e faltam {anos_faltantes} anos para o alistamento.')
    else:
        print('Está na hora de se alistar. O mais rápido possível!')