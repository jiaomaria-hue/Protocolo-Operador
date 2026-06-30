import socket

print("""
  ██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗ ██████╗ ██████╗ 
 ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
 ██║   ██║██████╔╝█████╗  ██████╔╝███████║██║  ██║██║  ██║██████╔╝
 ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██║  ██║██║  ██║██╔══██╗
 ╚██████╔╝██║     ███████╗██║  ██║██║  ██║██████╔╝██████╔╝██║  ██║
  ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝
                    Protocolo Operador — Sprint 1
""")

print('=' * 50)
print('   1 - reconhecimento (RECON)')
print('   2 - firewall logic')
print('   3 - Port Scanner')
print('=' * 50)

opcao = input('\nEscolha uma opção: ')

#opção 1 - Recon
if opcao == '1':
    alvo = input('Digite o dominio ou Ip do alvo: ')
    print(f'\n🔍 Iniciando reconhecimento em: {alvo}')
    print('-' * 40)
    try:
        ip = socket.gethostbyname(alvo)
        print(f'✅ IP encontrado: {ip}')
    except:
        print('❌ Não foi possível resolver o domínio')
    print('-' * 40)

# OPÇÃO 2 - FIREWALLS
elif opcao == '2':
    porta = int(input('Digite a porta: '))
    protocolo = input('Digite o protocolo (TCP/UDP): ').upper()
    print(f'\n🔍 Analisando porta {porta} via {protocolo}...')
    print('-' * 40)
    if porta == 80 and protocolo == 'TCP':
        print('✅ ALLOW — HTTP permitido')
    elif porta == 443 and protocolo == 'TCP':
        print('✅ ALLOW — HTTPS permitido')
    elif porta == 22 and protocolo == 'TCP':
        print('🚫 BLOCK — SSH bloqueado')
    else:
        print('❌ DROP — Porta desconhecida')
    print('-' * 40)

# opçao 3 - port scanner:
elif opcao == '3':
    alvo = input('Digite o alvo: ')
    print(f'\n🔍 Escaneando {alvo}...')
    print('-' * 40)
    for porta in range(1,1025):
        s = socket.socket()
        s.settimeout(1)
        resultado = s.connect_ex((alvo, porta))
        if resultado == 0:
            print(f'✅ Porta {porta} aberta')
        s.close()
    print('-' * 40)
    print('Scan completo.')


else:
    print('❌ Opção inválida.')