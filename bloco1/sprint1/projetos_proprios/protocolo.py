from recon import Recon
from firewall import Firewall
from ip_osint import Ip
from time import sleep
from rich import print
from scanner import PortScanner
from config import *
print("""
[red]  _________             _________        .__          __  .__                [/]
[red] /   _____/   /\\|\/\\    \\_   ___ \\  ____ |  |   _____/  |_|__|__  _______  [/]
[red] \\_____  \\   _)    (__  /    \\  \\/ /  _ \\|  | _/ __ \\   __\\  \\  \\/ /\\__  \\ [/]
[red] /        \\  \\_     _/  \\     \\___(  <_> )  |_\\  ___/|  | |  |\\   /  / __ \\[/]
[red]/_______  /    )    \\    \\______  /\\____/|____/\\___  >__| |__| \\_/  (____  /[/]
[red]        \\/     \\/\\|\\/           \\/                 \\/                    \\/ [/]
                [bold]Protocolo Operador — Sprint 2[/]
""")
while True:
    sleep(2)
    print("[cyan]" + "=" * 50 + "[/]")
    print("   [yellow]1[/] - Reconhecimento (RECON)")
    print("   [yellow]2[/] - Firewall Logic")
    print("   [yellow]3[/] - Port Scanner")
    print("   [yellow]4[/] - Consulta de IP (OSINT)")
    print("   [yellow]5[/] - Scan UDP")
    print("   [yellow]6[/] - Sair")
    print("[cyan]" + "=" * 50 + "[/]")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == '1':
        alvo = input("Digite o domínio ou IP do alvo: ").strip()
        if alvo:
            r = Recon(alvo)
            r.resolver_ip()
        else:
            print("[red]❌ Alvo não pode ser vazio.[/]")

    elif opcao == '2':
        try:
            porta = int(input("Digite a porta: "))
            protocolo = input("Digite o protocolo (TCP/UDP): ").strip().upper()
            f = Firewall(porta, protocolo)
            f.analisar()
        except ValueError:
            print("[red]❌ Erro: Digite um número válido para a porta.[/]")

    elif opcao == "3":
        alvo = input("Digite o alvo: ").strip()

        if not alvo:
            print("[red]❌ Alvo inválido.[/]")
            continue

        scanner = PortScanner(alvo)
        scanner.scan()

    elif opcao == '4':
        ip = input("Digite o IP: ").strip()
        i = Ip(ip)
        i.osint_basico_ip()

    elif opcao == '5':
        alvo = input('Digite um alvo: ').strip()
        if not alvo:
            print('[red]❌ Alvo inválido.[/]')
            continue
        scanner = PortScanner(alvo)
        scanner.scan_udp()


    else:
        print("[red]❌ Opção inválida.[/]")