comp = float(input('qual e o comprimento da parede? '))
larg = float(input('qual e a largura da parede? '))
area = comp * larg
tinta = area / 2
print(f'precisa de {tinta:.2f} baldes de tinta, para pintar {area:.2f} da area de metrosquadrados.')