valores = []
for cont in range(0, 5):
    valores.append(int(input(f'DIgite um valor na posiçao {cont}: '))) 
print('-=' * 20)
print(f'Voce digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'o maior valor foi o {maior} na posiçao {valores.index(maior)}')
print(f'o menor valor foi o {menor} na posiçao {valores.index(menor)}')