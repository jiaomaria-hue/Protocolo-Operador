import socket
import time
from rich import print

alvo = 'google.com'
porta = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

inicio = time.time()

resultado = s.connect_ex((alvo, porta))

fim = time.time()

latencia = (fim - inicio) * 1000

if resultado == 0:
    print(f'[green]✅ Conectado a {alvo}:{porta}[/]')
    print(f'[bold yellow]⏱️ Latência (Ping TCP):[/] {latencia:.2f} ms')
else:
    print('[red]❌ Falha ao conectar ao alvo.[/]')

s.close()