def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
def leiaFloat(msg=0):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return f

# Programa Principal
n = leiaInt('Digite um número: ')
f = leiaFloat('Digite um numero real: ')
print(f'Você acabou de digitar o número {n}, e o numero real é {f}')   