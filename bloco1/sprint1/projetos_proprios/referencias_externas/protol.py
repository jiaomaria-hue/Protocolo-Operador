import os
import sys
import time
import socket
import subprocess
import shutil
import requests
from typing import Dict, Optional

# ==============================================================================
# CONFIGURAÇÕES (PREENCHA AQUI A SUA CHAVE HIBP)
# ==============================================================================
# Para obter sua chave: https://haveibeenpwned.com/API/Key
HIBP_API_KEY = "INSIRA_SUA_CHAVE_AQUI" 
GEO_URL = "https://ipinfo.io/{ip}/json"
HACKERTARGET_URL = "https://api.hackertarget.com/reverseiplookup/?q={ip}"
WORDLIST = "/usr/share/dirb/wordlists/common.txt"
REQUEST_TIMEOUT = 5

# ==============================================================================
# INFRAESTRUTURA E VALIDAÇÃO
# ==============================================================================
def checar_dependencias():
    """Verifica se as ferramentas de sistema estão presentes."""
    for tool in ["nmap", "gobuster"]:
        if shutil.which(tool) is None:
            print(f"[!] ERRO CRÍTICO: {tool} não encontrado no sistema.")
            return False
    if not os.path.exists(WORDLIST):
        print(f"[!] ERRO: Wordlist não encontrada em {WORDLIST}.")
        return False
    return True

def delay(segundos=1.0):
    time.sleep(segundos)

# ==============================================================================
# MÓDULOS DE INTELIGÊNCIA
# ==============================================================================
def consultar_geo(ip: str):
    print(f"[*] Consultando Geo para {ip}...")
    try:
        resp = requests.get(GEO_URL.format(ip=ip), timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        print(f"    [+] Local: {data.get('city')}, {data.get('country')}")
        print(f"    [+] ISP: {data.get('org')}")
    except Exception as e:
        print(f"    [!] Erro na API Geo: {e}")

def executar_nmap(alvo: str):
    print(f"[*] Executando Nmap em {alvo}...")
    delay(1)
    try:
        # Nmap geralmente requer sudo para scan de versão (-sV)
        resultado = subprocess.run(["nmap", "-sV", "-F", alvo], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"    [!] Erro Nmap: {e.stderr}")

def executar_gobuster(alvo: str):
    print(f"[*] Executando Gobuster em {alvo}...")
    delay(1)
    try:
        resultado = subprocess.run(["gobuster", "dir", "-u", f"https://{alvo}", "-w", WORDLIST, "-q"], capture_output=True, text=True, check=True)
        print(resultado.stdout if resultado.stdout else "[+] Scan concluído. Nada encontrado.")
    except subprocess.CalledProcessError as e:
        print(f"    [!] Erro Gobuster: {e.stderr}")

def executar_people_osint(email: str):
    if HIBP_API_KEY == "INSIRA_SUA_CHAVE_AQUI" or not HIBP_API_KEY:
        print("[!] ERRO: Você não configurou sua HIBP_API_KEY no código.")
        return

    print(f"[*] Consultando vazamentos para: {email}")
    delay(1)
    try:
        resp = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", 
                            headers={"hibp-api-key": HIBP_API_KEY, "User-Agent": "Operador-Bot"}, timeout=5)
        if resp.status_code == 200:
            vazamentos = resp.json()
            print(f"    [!] ALERTA: Exposto em {len(vazamentos)} vazamentos!")
            for v in vazamentos[:5]:
                print(f"        - {v.get('Name')}")
        elif resp.status_code == 404:
            print("    [+] E-mail limpo nas bases conhecidas.")
        else:
            print(f"    [!] Erro API (Status {resp.status_code}): Verifique sua chave.")
    except Exception as e:
        print(f"    [!] Falha de rede: {e}")

# ==============================================================================
# MENU E EXECUÇÃO
# ==============================================================================
def main():
    if not checar_dependencias():
        print("\n[!] Ajuste o ambiente acima e rode o script novamente.")
        sys.exit(1)

    while True:
        print("""
  ██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗ ██████╗ ██████╗ 
 ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
 ██║   ██║██████╔╝█████╗  ██████╔╝███████║██║  ██║██║  ██║██████╔╝
 ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██║  ██║██║  ██║██╔══██║
 ╚██████╔╝██║     ███████╗██║  ██║██║  ██║██████╔╝██████╔╝██║  ██║
  ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝
             PROTOCOLO OPERADOR v2.0
""")
        print("1. GeoIP | 2. Nmap | 3. Gobuster | 4. OSINT | 5. Sair")
        op = input("\n>>> Opção: ").strip()

        if op == '5': break
        
        alvo = input("Alvo ou Email: ").strip()
        
        if op == '1': consultar_geo(alvo)
        elif op == '2': executar_nmap(alvo)
        elif op == '3': executar_gobuster(alvo)
        elif op == '4': executar_people_osint(alvo)
        
        delay(1.5)

if __name__ == "__main__":
    main()