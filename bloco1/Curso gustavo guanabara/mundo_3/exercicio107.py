c = ('\033[m',         
     '\033[0;30;41m',   
     '\033[0;30;42m',   
     '\033[0;30;44m'    
     )

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='') 

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=2) # Usando verde (índice 2)
    comando = str(input('Função ou Biblioteca > ')).strip()
    
    if comando.upper() == 'FIM':
        break
    else:
        # Opcional: Mostrar título da ajuda com outra cor
        titulo(f'Acessando o manual de "{comando}"', cor=3)
        ajuda(comando)

titulo('ATÉ LOGO!', cor=1)   