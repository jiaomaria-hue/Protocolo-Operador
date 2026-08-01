from recon import Recon
from firewall import Firewall
import socket
from time import sleep

while True:
    sleep(2)
    print(f"""
    \033[36m████████╗███████╗███████╗████████╗███████╗\033[0m
    \033[36m╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝\033[0m
    \033[36m   ██║   █████╗  ███████╗   ██║   █████╗  \033[0m
    \033[36m   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  \033[0m
    \033[36m   ██║   ███████╗███████║   ██║   ███████╗\033[0m
    \033[36m   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝\033[0m
                        \033[1mProtocolo Teste — Sprint 1\033[0m
    """)

    print('\033[36m' + '=' * 50 + '\033[0m')
    print('   \033[33m1\033[0m - Reconhecimento (RECON)')
    print('   \033[33m2\033[0m - Firewall Logic')
    print('   \033[33m3\033[0m - Port Scanner')
    print('   \033[33m4\033[0m - Sair')
    print('\033[36m' + '=' * 50 + '\033[0m')

    opcao = input(f'\n\033[1mEscolha uma opção: \033[0m').strip()

    if opcao == '1':
        alvo = input('\033[36mDigite o domínio ou IP do alvo: \033[0m').strip()
        if alvo:
            r = Recon(alvo)
            r.resolver_ip()
        else:
            print('\033[31m❌ Alvo não pode ser vazio.\033[0m')

    elif opcao == '2':
        try:
            porta = int(input('\033[36mDigite a porta: \033[0m'))
            protocolo = input('\033[36mDigite o protocolo (TCP/UDP): \033[0m').strip().upper()
            f = Firewall(porta, protocolo)
            f.analisar()
        except ValueError:
            print('\033[31m❌ Erro: Digite um número válido para a porta.\033[0m')

    elif opcao == '3':
        alvo = input('\033[36mDigite o alvo: \033[0m').strip()
        if not alvo:
            print('\033[31m❌ Erro: Por favor insira um Alvo válido.\033[0m')
            continue

        print(f'\n\033[33m🔍 Escaneando {alvo}...\033[0m')
        print('-' * 40)
        
        abertas = 0
        try:
            for porta in range(1, 1025):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    resultado = s.connect_ex((alvo, porta))
                    if resultado == 0:
                        print(f'\033[32m✅ Porta {porta} aberta\033[0m')
                        abertas += 1
        except socket.gaierror:
            print('\033[31m❌ Erro: Não foi possível resolver o hostname/IP informado.\033[0m')
        except KeyboardInterrupt:
            print('\n\033[33m⚠️ Scan interrompido pelo usuário.\033[0m')
        except Exception as e:
            print(f'\033[31m❌ Erro inesperado no escaneamento: {e}\033[0m')
        
        print('-' * 40)
        print(f'\033[1mScan completo. {abertas} porta(s) aberta(s) encontrada(s).\033[0m')

    elif opcao == '4':
        print('\033[33mSaindo do Protocolo Teste...\033[0m')
        break

    else:
        print('\033[31m❌ Opção inválida.\033[0m')