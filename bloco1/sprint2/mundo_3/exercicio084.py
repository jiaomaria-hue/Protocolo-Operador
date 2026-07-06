contador  = 0
esta_Correta = True
expressao = input('Digite uma expressao: ')
for caractere in expressao:
    if caractere == '(':
        contador += 1
    elif caractere == ')':
        contador -= 1
        if contador < 0:
            esta_Correta = False
if esta_Correta and contador == 0:
    print('expressao correta')
else:
    print('expressao errada')