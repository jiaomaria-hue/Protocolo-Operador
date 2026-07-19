import socket
class Recon:
    def __init__(self, alvo):
        self.alvo = alvo
    def resolver_ip(self):
        try:
            ip = socket.gethostbyname(self.alvo)
            print(f'✅ IP encontrado: {ip}')
        except:
            print('❌ Não foi possível resolver o domínio')
r = Recon('google.com')
r.resolver_ip()