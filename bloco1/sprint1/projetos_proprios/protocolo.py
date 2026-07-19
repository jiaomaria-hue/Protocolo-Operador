from recon import Recon
from firewall import Firewall
import socket
from time import sleep
while True:
    sleep(2)
    print(f"""
    \033[36m██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗ ██████╗ ██████╗ \033[0m
    \033[36m██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗\033[0m
    \033[36m██║   ██║██████╔╝█████╗  ██████╔╝███████║██║  ██║██║  ██║██████╔╝\033[0m
    \033[36m██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██║  ██║██║  ██║██╔══██╗\033[0m
    \033[36m╚██████╔╝██║     ███████╗██║  ██║██║  ██║██████╔╝██████╔╝██║  ██║\033[0m
    \033[36m ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝\033[0m
                        \033[1mProtocolo Operador — Sprint 1\033[0m
    """)

    print('\033[36m' + '=' * 50 + '\033[0m')
    print('   \033[33m1\033[0m - reconhecimento (RECON)')
    print('   \033[33m2\033[0m - firewall logic')
    print('   \033[33m3\033[0m - Port Scanner')
    print('\033[36m' + '=' * 50 + '\033[0m')

    opcao = input(f'\n\033[1mEscolha uma opção: \033[0m')

    if opcao == '1':
        alvo = input('\033[36mDigite o dominio ou Ip do alvo: \033[0m')
        r = Recon(alvo)
        r.resolver_ip()

    elif opcao == '2':
        try:
            porta = int(input('\033[36mDigite a porta: \033[0m'))
            protocolo = input('\033[36mDigite o protocolo (TCP/UDP): \033[0m').upper()
            f = Firewall(porta, protocolo)
            f.analisar()
        except ValueError:
            print('\033[31m❌ Erro: Digite um número válido para a porta.\033[0m')

    elif opcao == '3':
        try:
            alvo = input('\033[36mDigite o alvo: \033[0m')
            print(f'\n\033[33m🔍 Escaneando {alvo}...\033[0m')
            print('-' * 40)
            
            abertas = 0
            for porta in range(1, 1025):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                resultado = s.connect_ex((alvo, porta))
                if resultado == 0:
                    print(f'\033[32m✅ Porta {porta} aberta\033[0m')
                    abertas += 1
                s.close()
        except:
            print('Erro! Porfavor digite um Alvo correto.')
        
        print('-' * 40)
        print(f'\033[1mScan completo. {abertas} porta(s) aberta(s) encontrada(s).\033[0m')

    else:
        print('\033[31m❌ Opção inválida.\033[0m')   