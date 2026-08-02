import socket
alvo = 'scanme.nmap.org'
porta = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
resultado = s.connect((alvo, porta))
requisicao = "GET / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n"
r = s.send(requisicao.encode())
re = s.recv(1024)
print(re.decode())
s.close()