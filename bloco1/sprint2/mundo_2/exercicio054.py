frase = input('digite uma palavra: ').strip().upper()

palavra = frase.split()
junto = ''.join(palavra)

inverso = junto[::-1]

print(f'voce digitou {junto} e o inverso é {inverso}')
if junto == inverso:
    print('é um polimedro')
else:
    print('nao é um polimedro.')