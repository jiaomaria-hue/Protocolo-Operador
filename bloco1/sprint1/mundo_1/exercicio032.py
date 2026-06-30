bisexto = int(input('excreva um ano qualuqer: '))
bix = (bisexto % 4 == 0 and bisexto % 100 != 0) or (bisexto % 400 == 0)
if bix:
    print('o ano e bisexto.')
else:
    print('o ano nao e bisexto.')