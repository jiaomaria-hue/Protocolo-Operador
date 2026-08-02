import socket

alvo = input('\n\033[1mDigite o alvo: \033[0m')

try:
    socket.gethostbyname(alvo)
    print(f'Escaneando {alvo}...')
    print('-' * 30)

    for porta in range(1, 1025):
        s = socket.socket()
        s.settimeout(0.5)
        resultado = s.connect_ex((alvo, porta))
        if resultado == 0:
            print(f'Porta {porta} aberta')
        s.close()

except socket.gaierror:
    print('Alvo não encontrado. Digite um alvo válido.')

print('Scan completo.')