import socket
alvo = 'scanme.nmap.org'
portas = [80, 443, 22]
for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    resultado = s.connect_ex((alvo, porta))
    if resultado == 0:
        print(f'Porta {porta} foi conectada')
    else:
        print(f'Porta {porta} nao foi conectada')
    s.close() 