from rich import print
from rich.panel import Panel

class Firewall:
    def __init__(self, porta, protocolo):
        self.porta = porta
        self.protocolo = protocolo
    
    def analisar(self):
        if self.porta == 80 and self.protocolo == 'TCP':
            conteudo = '[green]✅ ALLOW — HTTP permitido[/]'
        elif self.porta == 443 and self.protocolo == 'TCP':
            conteudo = '[green]✅ ALLOW — HTTPS permitido[/]'
        elif self.porta == 22 and self.protocolo == 'TCP':
            conteudo = '[red]🚫 BLOCK — SSH bloqueado[/]'
        else:
            conteudo = '[red]❌ DROP — Porta desconhecida[/]'
        
        print(Panel(conteudo, title=f'[cyan]Firewall — Porta {self.porta} {self.protocolo}[/]', width=50))