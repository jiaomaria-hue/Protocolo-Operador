from rich import print, inspect
import subprocess
import os
import socket
from datetime import datetime

class Autenticacao:
    def autenticar(self):
        senha = 'operador2026'
        tent = 0
        try:
            while tent != 3:
                tent += 1
                se = input('Digite uma senha obs:(voce tem 3 tentativas): ')
                if se == senha:
                    print('[green]Acesso liberado.[/]')
                    return True
                elif tent == 3:
                    print('[green]Acabou suas tentativas. volte mais tarde, ou[/]... [red]VOCE VAI SOFRER![/]')
                    while True:
                        print('[red]DIGITE CONTROL C AGORA[/]')
        except KeyboardInterrupt:
            print('\nErro, voce interrompeu o processo')
            
class Reconhecimento:
    def __init__(self, ip=None):
        self.ip = ip
    def recon(self):
        try:
            print('[red]Me de um dominio.[/]')
            dom = input('Digite um dominio ou um ip de uma.. pessoa.. real.: ')

            self.ip = socket.gethostbyname(dom)
            print(f'[green]O ip de seu alvo é {self.ip}, agora vamos[/].... [red]ATACAR[/]')

            process = subprocess.run(
            ['curl', '-s', f'https://ipinfo.io/{self.ip}/json'],
            capture_output=True,
            text=True

            )
            print(f'[red]Dados sobre seu ip[/]: \n{process.stdout}')
        except socket.gaierror:
            print('Invalido, ip invalido.')


class Varredura:
    def __init__(self, ip=None):
        self.ip = ip

    def scan(self):
        portas = []
        for porta in range(20, 101):
            s = socket.socket()
            s.settimeout(0.5)
            resultado = s.connect_ex((self.ip, porta))
            if resultado == 0:
                try:
                    servico = socket.getservbyport(porta)
                except:
                    servico = 'desconhecido'
                print(f'[green]Porta {porta} — {servico}[/]')
                portas.append(porta)
            s.close()
        return portas

p1 = Autenticacao()
acesso = p1.autenticar()
if acesso:
    r = Reconhecimento()
    r.recon()
    v = Varredura(r.ip)
    portas = v.scan()
    
    data = datetime.now().strftime('%d/%m/%Y %H:%M')
    with open('relatorio.txt', 'w') as f:
        f.write('RELATÓRIO DE MISSÃO\n')
        f.write(f'Data: {data}\n')
        f.write(f'Alvo: {r.ip}\n')
        f.write(f'Portas abertas: {portas}\n')
    
    print('[green]Relatório salvo em relatorio.txt[/]')