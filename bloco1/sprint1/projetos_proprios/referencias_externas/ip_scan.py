# ORIGEM: código de [Sawyerk], Blue/Red Team júnior
# USO: referência de estudo, NÃO é trabalho próprio
# Reescrever do zero quando chegar em Sprint de módulos externos/API
import argparse
import ipaddress
import json
import re
import shutil
import subprocess
import sys
from typing import Any, Dict, Optional

import requests

RIPE_URL = "https://stat.ripe.net/data/prefix-overview/data.json"
# CORREÇÃO: Alterado para HTTPS para evitar rejeição da API
IPAPI_URL = "https://ip-api.com/json/{ip}"
REQUEST_TIMEOUT = 10


def validar_ip(ip: str) -> str:
    try:
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        raise argparse.ArgumentTypeError(f"IP inválido: {ip}")


def rodar_whois(ip: str) -> Dict[str, Optional[str]]:
    whois_bin = shutil.which("whois") or shutil.which("whois.exe")
    if not whois_bin:
        return {
            "raw": None,
            "bloco": None,
            "titular": None,
            "erro": "Comando 'whois' não instalado no sistema operando. Execute: sudo apt install whois"
        }

    try:
        # Consulta genérica para o WHOIS descobrir o servidor correto automaticamente
        resultado = subprocess.run(
            [whois_bin, ip],
            capture_output=True,
            text=True,
            timeout=15,
            check=False
        )

        texto = (resultado.stdout or "") + "\n" + (resultado.stderr or "")
        texto = texto.strip()

        if not texto:
            return {
                "raw": None,
                "bloco": None,
                "titular": None,
                "erro": "WHOIS retornou vazio."
            }

        bloco = None
        titular = None

        padroes_bloco = [
            r"inetnum:\s*([0-9./ -]+)",
            r"NetRange:\s*([0-9.\- ]+)",
            r"CIDR:\s*([0-9./, ]+)",
            r"route:\s*([0-9./]+)",
        ]

        padroes_titular = [
            r"owner:\s*(.+)",
            r"org-name:\s*(.+)",
            r"OrgName:\s*(.+)",
            r"netname:\s*(.+)",
            r"descr:\s*(.+)",
        ]

        for padrao in padroes_bloco:
            match = re.search(padrao, texto, re.IGNORECASE)
            if match:
                bloco = match.group(1).strip()
                break

        for padrao in padroes_titular:
            match = re.search(padrao, texto, re.IGNORECASE)
            if match:
                titular = match.group(1).strip()
                break

        return {
            "raw": texto,
            "bloco": bloco,
            "titular": titular,
            "erro": None
        }

    except subprocess.TimeoutExpired:
        return {
            "raw": None,
            "bloco": None,
            "titular": None,
            "erro": "WHOIS expirou por timeout."
        }
    except Exception as e:
        return {
            "raw": None,
            "bloco": None,
            "titular": None,
            "erro": f"Erro ao executar WHOIS: {e}"
        }


def consultar_ripe(ip: str) -> Dict[str, Any]:
    try:
        resp = requests.get(
            RIPE_URL,
            params={"resource": ip},
            timeout=REQUEST_TIMEOUT
        )
        resp.raise_for_status()
        data = resp.json()

        asns = data.get("data", {}).get("asns", [])
        prefix = data.get("data", {}).get("resource")

        asn = asns[0].get("asn") if asns else None
        holder = asns[0].get("holder") if asns else None

        return {
            "asn": asn,
            "asn_holder": holder,
            "prefix": prefix,
            "erro": None
        }
    except requests.RequestException as e:
        return {
            "asn": None,
            "asn_holder": None,
            "prefix": None,
            "erro": f"Erro na consulta RIPE: {e}"
        }
    except (ValueError, KeyError, IndexError, TypeError) as e:
        return {
            "asn": None,
            "asn_holder": None,
            "prefix": None,
            "erro": f"Resposta inesperada da RIPE: {e}"
        }


def consultar_geo(ip: str) -> Dict[str, Any]:
    try:
        # CORREÇÃO: Headers adicionados para simular navegador real e evitar bloqueios automáticos
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        resp = requests.get(
            IPAPI_URL.format(ip=ip),
            params={"fields": "status,message,country,regionName,city,zip,lat,lon,isp,org,query"},
            headers=headers,
            timeout=REQUEST_TIMEOUT
        )
        resp.raise_for_status()
        data = resp.json()

        if data.get("status") != "success":
            return {
                "pais": None, "regiao": None, "cidade": None, "cep": None,
                "lat": None, "lon": None, "isp": None, "org": None,
                "erro": f"GeoIP falhou: {data.get('message', 'erro desconhecido')}"
            }

        return {
            "pais": data.get("country"),
            "regiao": data.get("regionName"),
            "cidade": data.get("city"),
            "cep": data.get("zip"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "isp": data.get("isp"),
            "org": data.get("org"),
            "erro": None
        }

    except requests.RequestException as e:
        return {
            "pais": None, "regiao": None, "cidade": None, "cep": None,
            "lat": None, "lon": None, "isp": None, "org": None,
            "erro": f"Erro na consulta GeoIP: {e}"
        }
    except (ValueError, TypeError) as e:
        return {
            "pais": None, "regiao": None, "cidade": None, "cep": None,
            "lat": None, "lon": None, "isp": None, "org": None,
            "erro": f"Resposta inesperada do GeoIP: {e}"
        }


def imprimir_relatorio(ip: str, whois_data: Dict[str, Any], ripe_data: Dict[str, Any], geo_data: Dict[str, Any]) -> None:
    print(f"\n[+] Consulta para IP: {ip}\n")

    print("=== WHOIS ===")
    print("Bloco:      ", whois_data.get("bloco") or "Não encontrado")
    print("Titular:    ", whois_data.get("titular") or "Não encontrado")
    if whois_data.get("erro"):
        print("Erro WHOIS: ", whois_data["erro"])

    print("\n=== BGP / ASN ===")
    print("Prefixo:    ", ripe_data.get("prefix") or "Não encontrado")
    print("ASN:        ", f"AS{ripe_data.get('asn')}" if ripe_data.get('asn') else "Não encontrado")
    print("Holder ASN: ", ripe_data.get("asn_holder") or "Não encontrado")
    if ripe_data.get("erro"):
        print("Erro RIPE:  ", ripe_data["erro"])

    print("\n=== GEOIP ===")
    print("País:       ", geo_data.get("pais") or "Não encontrado")
    print("Região:     ", geo_data.get("regiao") or "Não encontrado")
    print("Cidade:     ", geo_data.get("cidade") or "Não encontrado")
    print("CEP:        ", geo_data.get("cep") or "Não encontrado")
    print("ISP:        ", geo_data.get("isp") or "Não encontrado")
    print("Org:        ", geo_data.get("org") or "Não encontrado")
    print("Lat/Lon:    ", f"{geo_data.get('lat')} / {geo_data.get('lon')}" if geo_data.get('lat') else "Não encontrado")
    if geo_data.get("erro"):
        print("Erro GEOIP: ", geo_data["erro"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Consulta WHOIS + ASN + GEOIP de um IP")
    parser.add_argument("ip", type=validar_ip, help="Endereço IP para consulta")
    parser.add_argument("--json", action="store_true", help="Saída em JSON")
    args = parser.parse_args()

    ip = args.ip

    whois_data = rodar_whois(ip)
    ripe_data = consultar_ripe(ip)
    geo_data = consultar_geo(ip)

    if args.json:
        saida = {
            "ip": ip,
            "whois": whois_data,
            "ripe": ripe_data,
            "geo": geo_data,
        }
        print(json.dumps(saida, indent=2, ensure_ascii=False))
        return

    imprimir_relatorio(ip, whois_data, ripe_data, geo_data)


if __name__ == "__main__":
    main()