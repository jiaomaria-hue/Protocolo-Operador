largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem {area:.2f}m² e você precisará de {tinta:.2f} litros de tinta.')