import socket
alvo = input('Digite o alvo: ')
print(f'Escaneando {alvo}...')
print('-' * 30)

for porta in range(1, 1025):
    s = socket.socket()
    s.settimeout(1)
    resultado = s.connect_ex((alvo, porta))
    if resultado == 0:
        print(f'Porta {porta} aberta')
    s.close()

print('Scan completo.')