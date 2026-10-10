# Hardening Log - SSH

## Item 1: PermitRootLogin
- Antes: comentado (default prohibit-password)
- Depois: PermitRootLogin no (explícito, bloqueio total de root via SSH)
- Comando: sed + systemctl restart sshd

## Item 2: PasswordAuthentication
- Antes: comentado (default yes)
- Depois: PasswordAuthentication no (só chave SSH, sem senha)
- Comando: sed + systemctl restart ssh

## Item 3: MaxAuthTries
- Antes: comentado (default 6)
- Depois: MaxAuthTries 3 (mitigação básica de brute-force)
- Comando: sed + systemctl restart ssh

## Item 4: UFW Firewall
- Antes: UFW inativo (sem filtro de rede)
- Depois: UFW ativo, política deny incoming / allow outgoing, exceção SSH liberada
- Comando: ufw default deny incoming / allow outgoing / allow ssh / enable

## Item 5: Docker - Portas Expostas Esquecidas
- Achado: nmap localhost revelou portas 5432 e 8000 abertas via docker-proxy
- Investigacao: docker ps revelou 3 containers antigos (projeto casino com amigos, 3 semanas rodando) + 1 container extra (teste-deface, nginx, 5 semanas parado)
- Risco: Docker contorna regras do UFW diretamente no iptables, exposicao real mesmo com firewall ativo
- Acao: todos os containers parados e removidos (docker stop + docker rm)
- Licao: UFW sozinho NAO protege contra servicos Docker expostos - preciso auditar containers regularmente, nao so configs de SSH
