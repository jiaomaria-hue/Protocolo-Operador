def metade(valor = 0,format=False):
    calculo = valor / 2
    return calculo if format is False else moeda(calculo)

def dobro(valor = 0, format=False):
    calculo = valor * 2
    return calculo if format is False else moeda(calculo)

def aumentar(valor = 0, taxa=0, format = False):
    calculo = valor + (valor * taxa / 100)
    return calculo if format is False else moeda(calculo)

def diminuir(valor = 0, taxa=0, format = False):
    calculo = valor - (valor * taxa / 100)
    return calculo if format is False else moeda(calculo)

def moeda(preço=0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(valor, taxa_aum=10, taxa_red=5):
    print('-' * 30)
    print('     RESUMO DO VALOR     '.center(30))
    print('-' * 30)
    
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(valor, taxa_aum, True)}')
    print(f'{taxa_red}% de redução: \t{diminuir(valor, taxa_red, True)}')