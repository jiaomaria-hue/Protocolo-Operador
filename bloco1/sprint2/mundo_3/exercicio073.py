numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
    'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:
    try:
        numero = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= numero <= 20:
            print(f'O numero que voce digitou é {numeros_extenso[numero]}')
            break
        else:
            print('Numero fora do intervalo, tenta de novo.')
    except ValueError:
        print('Digite um numero válido.')