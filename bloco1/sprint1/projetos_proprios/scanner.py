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

    def scan_udp(self):
        portas_udp = {
            53: 'DNS',
            67: 'DHCP',
            68: 'DHCP',
            123: 'NTP',
            161: 'SNMP'
        }

        print(f"\n[yellow]🔍 Scan UDP em {self.alvo}...[/]")
        print('-' * 40)

        for porta, servico in portas_udp.items():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.settimeout(TIMEOUT)
                    s.sendto(b'', (self.alvo, porta))
                    s.recvfrom(1024)
                    print(f"[green]✅ Porta UDP {porta} ({servico}) respondeu[/]")
            except socket.timeout:
                print(f"[yellow]⚠️ Porta UDP {porta} ({servico}) sem resposta[/]")
            except Exception as e:
                print(f"[red]❌ Porta UDP {porta} ({servico}) — {e}[/]")