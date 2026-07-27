def passo(i, f, p):
    for c in range(i, f+1, p):
            print(c, end='')
passo(i=int(input('inicio: ')), f=int(input('Fim: ')), p=int(input('Passo:')))