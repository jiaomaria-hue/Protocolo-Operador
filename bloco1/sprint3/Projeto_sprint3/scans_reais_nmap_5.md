
## Scan 1
Comando: nmap -A scanme.nmap.org
IP: 45.33.32.156
Portas Abertas:
- 22/tcp SSH (OpenSSH 6.6.1p1)
- 80/tcp HTTP (Apache 2.4.7)
- 9929/tcp nping-echo
- 31337/tcp tcpwrapped

Protocolos Identificados: SSH, HTTP, ICMP echo alternative

Análise:
- Porta 22 aberta = servidor SSH disponível (login remoto seguro)
- Porta 80 aberta = servidor web HTTP ativo
- nping-echo = serviço de teste (Nmap echo service)
- tcpwrapped = porta ativa mas não consegue identificar serviço
- SO: Linux 5.0-5.14 (99% confiança) — identificado corretamente
- Distância: 21 hops (servidor em São Francisco, você no Brasil)


## Scan 2
Comando: nmap -A google.com
IP: 172.217.28.206
Portas Abertas:
- 80/tcp HTTP (gws - Google Web Server)
- 443/tcp HTTPS (gws + SSL/TLS)

Protocolos Identificados: HTTP, HTTPS, TLS 1.2+

Análise:
- Porta 80: Redireciona para https://www.google.com/ (força HTTPS)
- Porta 443: Certificado wildcard *.google.com (válido até 2026-11-02)
- Certificado contém múltiplos domínios (youtube.com, google.com.br, etc)
- SO: Apple macOS (ERRADO — Google roda Linux, mas Nmap chutou porque só achou portas abertas, sem portas fechadas pra comparar)
- Distância: 14 hops
- TLS protocols: grpc-exp, h2 (HTTP/2), http/1.1, http/1.0

## Scan 3
Comando: nmap -sV bancocn.com
IP: 104.21.52.8 (resolvido também como 172.67.192.199)
Portas Abertas:
- 80/tcp, 443/tcp, 8080/tcp, 8443/tcp
- Todas identificadas como "Cloudflare http proxy" / "cloudflare"

Análise:
- Servidor ESTÁ ATRÁS DE CLOUDFLARE (WAF/CDN)
- Você não tá vendo o servidor real, tá vendo o proxy
- Portas 8080/8443 = HTTP alternativo (muitas vezes usado internamente)
- SO detection falhou (Apple/FreeBSD com 89%) — porque Cloudflare esconde a verdade

## Scan 4
Comando: nmap -O scanme.nmap.org
IP: 45.33.32.156
Portas (sem service detection):
- 22/tcp ssh
- 80/tcp http
- 9929/tcp nping-echo
- 31337/tcp Elite

Análise OS Detection:
- Linux 5.0-5.14 (98% confiança)
- Diferença vs Scan 1: -O usa only OS guessing, sem -sV (service detection)
- Resultado: mesmo SO, menos informação sobre versões de serviços

Por que -O importa?
- Permite identificar SO sem expor serviços (mais stealth)
- Útil em reconhecimento passivo onde você quer só o SO

## Scan 5
Comando: nmap -sU google.com
IP: 172.217.28.206
Portas UDP:
- 33459/udp closed (unknown)
- 999 portas open|filtered (sem resposta)

Protocolos UDP Identificados: Nenhum específico respondeu

Análise:
- UDP é stateless — não usa handshake like TCP
- "open|filtered" = Nmap enviou pacote UDP mas não recebeu resposta
  - Pode ser: porta aberta, firewall bloqueando, ou host não responde UDP
- Google bloqueia a maioria das portas UDP (proteção)
- Porta 33459 retornou ICMP "port unreachable" = confirmadamente fechada
- Diferença UDP vs TCP: TCP você sabe se tá aberto/fechado. UDP é incerteza.

Por que UDP importa?
- Serviços críticos rodam em UDP: DNS (53), NTP (123), SNMP (161), DHCP (67/68)
- Se você quer fazer pentest completo, precisa testar TCP E UDP
- Google restringe UDP porque ataques DDoS usam UDP amplification