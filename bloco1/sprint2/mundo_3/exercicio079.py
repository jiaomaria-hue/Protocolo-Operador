valores = []
for cont in range(0, 5):
    valores.append(int(input(f'DIgite um valor na posiçao {cont}: '))) 
print('-=' * 20)
print(f'Voce digitou os valores {valores}')
print(f'o maior valor foi o {max(valores)} na posiçao {valores.index(max(valores))}')
print(f'o menor valor foi o {min(valores)} na posiçao{valores.index(min(valores))}')