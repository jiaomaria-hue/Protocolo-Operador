# 1. Leitura das três retas
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# 2. Aplicação da condição de existência
# Todas as três condições precisam ser verdadeiras ao mesmo tempo
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')