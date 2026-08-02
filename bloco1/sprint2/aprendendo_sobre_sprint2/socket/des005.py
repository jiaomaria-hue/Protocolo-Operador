import socket
from rich import print
alvo = input('\033[1;31;40mDigite o alvo: \033[m')
try:
    ip = socket.gethostbyname(alvo)
    print(f'[green]✅ IP encontrado:[/] {ip}')
except socket.gaierror:
    print('[red]❌ Não foi possível resolver o domínio pois e inexsistente[/]')
