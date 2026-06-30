n1 = int(input('Digite um numero: '))
con = int(input('qual base de conversao voce quer? 1 = binario 2 = octual e 3 = hexadecimal:  '))
binario = bin(n1)
octual = oct(n1)
hexadecimal = hex(n1)
if con == 1:
    print(f'o seu numero vai ser binario que e igual a {binario[2:]}')
elif con == 2:
    print(f'o seu numero vai ser octual {octual}')
elif con == 3:
    print(f'seu numero vai ser hexadecimal {hexadecimal[2:]}')
else:
    print(f'Opçao invalida, digite 1, 2, 3.')