from recon import Recon
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
            
            print(f'\n\033[33m🔍 Analisando porta {porta} via {protocolo}...\033[0m')
            print('-' * 40)
            
            if porta == 80 and protocolo == 'TCP':
                print('\033[32m✅ ALLOW — HTTP permitido\033[0m')
            elif porta == 443 and protocolo == 'TCP':
                print('\033[32m✅ ALLOW — HTTPS permitido\033[0m')
            elif porta == 22 and protocolo == 'TCP':
                print('\033[31m🚫 BLOCK — SSH bloqueado\033[0m')
            else:
                print('\033[31m❌ DROP — Porta desconhecida\033[0m')
            print('-' * 40)
        except ValueError:
            print('\033[31m❌ Erro: Por favor, digite um número válido para a porta.\033[0m')

    elif opcao == '3':
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
        
        print('-' * 40)
        print(f'\033[1mScan completo. {abertas} porta(s) aberta(s) encontrada(s).\033[0m')

    else:
        print('\033[31m❌ Opção inválida.\033[0m')   