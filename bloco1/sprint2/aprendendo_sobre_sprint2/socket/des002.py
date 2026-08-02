import socket

# 1. Cria um socket UDP (SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # 2. Aponta para um IP externo (não precisa enviar dados de fato)
    s.connect(('8.8.8.8', 80))
    
    # 3. Pega o IP local da placa que se conectou
    ip_real = s.getsockname()[0]
    print(f'Seu IP real na rede local é: {ip_real}')

except Exception as e:
    print(f'Erro ao obter IP: {e}')

finally:
    s.close()