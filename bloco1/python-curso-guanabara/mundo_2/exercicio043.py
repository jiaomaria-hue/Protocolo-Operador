peso = float(input('Qual o peso (kg): '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

print(f'o imc é {imc:.1f}')

if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')