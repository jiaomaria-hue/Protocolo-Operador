import socket
ips = set()
resultados = socket.getaddrinfo('google.com', 80)
for item in resultados:
    sockaddr = item[4]
    ip = sockaddr[0]
    ips.add(ip)

print('IPs do Google encontrados:')
for ip in ips:
    print(F' - {ip}')
