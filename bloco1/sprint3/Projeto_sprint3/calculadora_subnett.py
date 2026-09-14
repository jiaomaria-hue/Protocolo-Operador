import ipaddress

def calcular_subnet(ip_cidr):
    try:
        rede = ipaddress.ip_network(ip_cidr, strict=False)

        resultados = {
            "Endereco de rede": str(rede.network_address),
            "Máscara de Sub-rede": str(rede.netmask),
            "Wildcard Mask": str(rede.hostmask),
            "Endereço de Broadcast": str(rede.broadcast_address),
            "Total de Endereços IP": rede.num_addresses,
            "Prefixo CIDR": f"/{rede.prefixlen}"
        }

        hosts = list(rede.hosts())
        if hosts:
            resultados["Primeiro Host utilizavel"] = str(hosts[0])
            resultados["Ultimo Host utilizavel"] = str(hosts[-1])
            resultados["Total de Host uteis"] = str(len(hosts))
        else:
            resultados["Host utilizaveis"] = "Nenhum (Rede /31 ou /32)"

        for chave, valor in resultados.items():
            print(f"{chave}: {valor}")

    except ValueError as e:
        print(f"Erro ao processar o IP/CIDR: {e}")

if __name__ == "__main__":
    entrada = input("Digite o IP com a máscara CIDR (ex: 192.168.1.0/24): ")
    calcular_subnet(entrada)