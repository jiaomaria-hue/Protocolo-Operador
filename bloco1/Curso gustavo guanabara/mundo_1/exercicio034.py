entrada = input('Digite seu salário (use apenas ponto para centavos, ex: 1250.00): ')
slr = float(entrada)
aumento = slr * 1.10
menor = slr * 1.15
if slr < aumento:
    print(f'voce recebeu {slr}, mas com o aumento voce recebeu {aumento}')
else:
    print(f'voce recebeu {slr}, mas com o aumento voce recebeu {menor}')

