import math
catop = float(input('qual e o valor da cateto oposto? '))
catadj = float(input('qual e o valor do cateto adjacente? '))

h1 = math.hypot(catop, catadj)

print(f' a hipotenusa vai medir {h1:.2f}')