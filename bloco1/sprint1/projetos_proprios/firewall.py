class Firewall:
    def __init__(self, porta, protocolo):
        self.porta = porta
        self.protocolo = protocolo
    
    def analisar(self):
        print(f'\n\033[33m🔍 Analisando porta {self.porta} via {self.protocolo}...\033[0m')
        print('-' * 40)
        
        if self.porta == 80 and self.protocolo == 'TCP':
            print('\033[32m✅ ALLOW — HTTP permitido\033[0m')
        elif self.porta == 443 and self.protocolo == 'TCP':
            print('\033[32m✅ ALLOW — HTTPS permitido\033[0m')
        elif self.porta == 22 and self.protocolo == 'TCP':
            print('\033[31m🚫 BLOCK — SSH bloqueado\033[0m')
        else:
            print('\033[31m❌ DROP — Porta desconhecida\033[0m')
        print('-' * 40)