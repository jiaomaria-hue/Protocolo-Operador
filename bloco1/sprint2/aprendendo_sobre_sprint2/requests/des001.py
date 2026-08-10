import requests
from rich import print
from rich.panel import Panel
try:
    ip = input('Digite um ip: ')
    resposta = requests.get(f'https://ipinfo.io/{ip}/json')
    dados = resposta.json()
    if dados.get('ip') is None:
        print('[red]❌ IP inválido ou não encontrado.[/]')
    else:
        conteudo = (
    f"[cyan]IP:[/] {dados.get('ip')}\n"
    f"[cyan]Cidade:[/] {dados.get('city')}, {dados.get('region')}\n"
    f"[cyan]País:[/] {dados.get('country')}\n"
    f"[cyan]ISP:[/] {dados.get('org')}\n"
    f"[cyan]Timezone:[/] {dados.get('timezone')}"
)

        c = Panel(conteudo, title="[red]OSINT — IP Info[/]", border_style="cyan", width=35)
        print(c)
except KeyboardInterrupt:
    print('Vocẽ intenrrompeu a ferramenta.')
except requests.exceptions.JSONDecodeError:
    print('[red]❌ IP inválido ou sem dados.[/]')
except requests.exceptions.ConnectionError:
    print('[red]❌ Sem conexão com a internet.[/]')