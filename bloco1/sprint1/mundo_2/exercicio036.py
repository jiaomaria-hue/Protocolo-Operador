valor = float(input('digite o valor da casa: '))
salar = float(input('digite o seu salario: '))
anos = int(input('quantos anos voce vai pagar a casa? '))
meses = anos * 12
prestaçao = valor / meses
limite = salar * 0.30
if prestaçao <= limite:
    print('emprestimo aprovado')
else:
    print('emprestimo nao aprovado')