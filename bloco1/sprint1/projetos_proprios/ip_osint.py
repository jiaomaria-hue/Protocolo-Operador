import requests
from rich import print
from rich.panel import Panel
from config import URL_IPINFO

class Ip:
    def __init__(self, ip):
        self.ip = ip

    def osint_basico_ip(self):
        try:
            resposta = requests.get(URL_IPINFO.format(ip=self.ip), timeout=5)
            dados = resposta.json()
            
            conteudo = f"""[cyan]IP:[/] {dados.get('ip')}
[cyan]Cidade:[/] {dados.get('city')}, {dados.get('region')}
[cyan]País:[/] {dados.get('country')}
[cyan]ISP:[/] {dados.get('org')}
[cyan]Timezone:[/] {dados.get('timezone')}"""
            
            print(Panel(conteudo, title="[red]OSINT — IP Info[/]", border_style="cyan", width=35))
        except requests.exceptions.RequestException as e:
            print(f"[red]❌ Erro na requisição: {e}[/]")