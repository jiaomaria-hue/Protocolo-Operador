import socket
from rich import print
from config import TIMEOUT, PORTA_FIM, PORTA_INICIO
from concurrent.futures import ThreadPoolExecutor


class PortScanner:
    def __init__(self, alvo):
        self.alvo = alvo
        self.portas_abertas = []

    def testar_porta(self, porta):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(TIMEOUT)
                if s.connect_ex((self.alvo, porta)) == 0:
                    print(f"[green]✅ Porta {porta} aberta[/]")
                    self.portas_abertas.append(porta)
        except:
            pass

    def scan(self):
        print(f"\n[yellow]🔍 Escaneando {self.alvo}...[/]")
        print("-" * 40)
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(self.testar_porta, range(PORTA_INICIO, PORTA_FIM))
        return self.portas_abertas