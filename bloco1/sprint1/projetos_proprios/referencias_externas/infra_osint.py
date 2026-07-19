import socket
import sys
import subprocess
import dns.resolver
import requests

def banner():
    print("=" * 60)
    print("        Abaetê OSINT - Reconhecimento de Infraestrutura     ")
    print("=" * 60)

def coletar_ip(alvo):
    """Descobre o endereço IP principal do domínio."""
    print(f"\n[*] Coletando IP de: {alvo}")
    try:
        ip = socket.gethostbyname(alvo)
        print(f"[+] IP Encontrado: {ip}")
        return ip
    except socket.gaierror:
        print("[-] Erro: Não foi possível resolver o domínio.")
        return None

def consultar_dns(alvo):
    """Consulta registros DNS essenciais para mapeamento."""
    print(f"\n[*] Consultando Registros DNS para: {alvo}")
    tipos_registro = ['NS', 'MX', 'TXT']
    
    for tipo in tipos_registro:
        try:
            respostas = dns.resolver.resolve(alvo, tipo)
            print(f"\n--- Registros {tipo} ---")
            for rdata in respostas:
                print(f" [->] {rdata.to_text()}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"[-] Nenhum registro {tipo} encontrado.")
        except Exception as e:
            print(f"[-] Erro ao consultar {tipo}: {str(e)}")

def analisar_cabecalhos_http(alvo):
    """Analisa os cabeçalhos HTTP para identificar o servidor web."""
    print(f"\n[*] Analisando Cabeçalhos HTTP de: {alvo}")
    url = f"http://{alvo}"
    try:
        resposta = requests.get(url, timeout=5)
        cabecalhos = resposta.headers
        
        print("\n--- Informações do Servidor Web ---")
        if 'Server' in cabecalhos:
            print(f"[+] Servidor: {cabecalhos['Server']}")
        else:
            print("[-] Cabeçalho 'Server' ocultado (Boa prática de segurança).")
            
        if 'X-Powered-By' in cabecalhos:
            print(f"[+] Tecnologia: {cabecalhos['X-Powered-By']}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Falha ao conectar via HTTP: {str(e)}")

def rodar_nmap(ip_alvo):
    """Executa o Nmap no IP encontrado."""
    if not ip_alvo:
        print("[-] Nmap cancelado: IP inválido ou não encontrado.")
        return

    print(f"\n[*] Iniciando varredura rápida com Nmap no IP: {ip_alvo}")
    # -F varre rapidamente as 100 portas mais comuns
    comando = ["nmap", "-F", ip_alvo]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("\n--- Resultado do Nmap ---")
        print(resultado.stdout)
    except FileNotFoundError:
        print("[-] Erro: Nmap não encontrado no sistema. Instale via 'sudo apt install nmap'.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Erro ao executar o Nmap: {e.stderr}")

def rodar_gobuster(alvo):
    """Executa o Gobuster para encontrar diretórios comuns ocultos."""
    print(f"\n[*] Iniciando brute-force de diretórios com Gobuster em: {alvo}")
    
    url_alvo = f"http://{alvo}"
    # Caminho padrão da wordlist que o APT instala junto com ferramentas de brute force
    wordlist = "/usr/share/dirb/wordlists/common.txt"
    
    # Executa o gobuster ocultando o banner inicial (-q) para deixar o terminal limpo
    comando = ["gobuster", "dir", "-u", url_alvo, "-w", wordlist, "-q"]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("\n--- Diretórios Encontrados pelo Gobuster ---")
        if resultado.stdout.strip():
            print(resultado.stdout)
        else:
            print("[+] Nenhum diretório comum exposto publicamente.")
    except FileNotFoundError:
        print("[-] Erro: Gobuster não encontrado no sistema. Instale via 'sudo apt install gobuster'.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Erro ao executar o Gobuster: {e.stderr}")

def main():
    banner()
    if len(sys.argv) < 2:
        print("Uso correto: python infra_osint.py <dominio_alvo>")
        print("Exemplo: python infra_osint.py exemplo.com")
        sys.exit(1)
        
    alvo = sys.argv[1]
    
    ip = coletar_ip(alvo)
    consultar_dns(alvo)
    analisar_cabecalhos_http(alvo)
    
    # Executa as ferramentas externas integradas
    rodar_nmap(ip)
    rodar_gobuster(alvo)
    
    print("\n" + "=" * 60)
    print("[*] Coleta de inteligência concluída de forma legítima.")
    print("=" * 60)

if __name__ == "__main__":
    main()