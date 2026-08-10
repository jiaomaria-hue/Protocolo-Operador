import re

texto = "O IP 192.168.1.1 tentou acessar a porta 22"

# encontra o IP
ip = re.search(r'\d+\.\d+\.\d+\.\d+', texto)
print(ip.group())  # 192.168.1.1