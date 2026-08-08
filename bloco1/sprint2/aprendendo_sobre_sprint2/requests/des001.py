import requests
from rich import print
from rich.panel import Panel

resposta = requests.get('https://ipinfo.io/8.8.8.8/json')
dados = resposta.json()

conteudo = f"""[cyan]IP:[/] {dados.get('ip')}
[cyan]Cidade:[/] {dados.get('city')}, {dados.get('region')}
[cyan]País:[/] {dados.get('country')}
[cyan]ISP:[/] {dados.get('org')}
[cyan]Timezone:[/] {dados.get('timezone')}"""

c = Panel(conteudo, title="[red]OSINT — IP Info[/]", border_style="cyan", width=35)
print(c)