n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))

m = (n1 + n2) / 2
print(m)
print('-' * 20)
if m < 5.0:
    print('Você foi reprovado.')
elif 5.0 <= m <= 6.9:
    print('Você está de recuperação.')
else:
    print('Você foi aprovado.')
print('-' * 20)