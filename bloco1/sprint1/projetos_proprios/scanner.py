import socket
from rich import print

TIMEOUT = 0.5

class PortScanner:
    def __init__(self, alvo):
        self.alvo = alvo
        self.portas_abertas = []

    def scan(self):
        print(f"\n[yellow]🔍 Escaneando {self.alvo}...[/]")
        print("-" * 40)

        try:
            for porta in range(1, 1025):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(TIMEOUT)

                    if s.connect_ex((self.alvo, porta)) == 0:
                        print(f"[green]✅ Porta {porta} aberta[/]")
                        self.portas_abertas.append(porta)

        except socket.gaierror:
            print("[red]Hostname inválido.[/]")

        return self.portas_abertas