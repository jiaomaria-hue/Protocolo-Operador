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
