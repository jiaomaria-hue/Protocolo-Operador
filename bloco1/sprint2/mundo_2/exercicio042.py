# 1. Leitura das três retas
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# 2. Aplicação da condição de existência
# Todas as três condições precisam ser verdadeiras ao mesmo tempo
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('PODEM formar um triângulo: ', end='')
    
    # Classificação aqui dentro
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('NÃO podem formar um triângulo.')