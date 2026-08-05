import socket
from rich import print
from rich.panel import Panel
class Recon:
    def __init__(self, alvo):
        self.alvo = alvo
    def resolver_ip(self):
        try:
            
            ip = socket.gethostbyname(self.alvo)
            conteudo = f'''[green]✅ IP encontrado:[/] [red]{ip}[/]'''
            print(Panel(conteudo, title='[red]IP HOST[/]', width=32))
        except socket.gaierror:
            print('[red]❌ Não foi possível resolver o domínio[/]')