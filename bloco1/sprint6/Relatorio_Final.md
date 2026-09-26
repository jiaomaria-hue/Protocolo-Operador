
# RELATÓRIO DE TESTE DE PENETRAÇÃO AUTORIZADO

**Cliente:** Hack The Box

**Alvo:** Aplicação Web "Cap" (`10.129.143.250`)

**Data:** 26 de Setembro de 2026

**Elaborado por:** Kryzen Team

**Classificação:** ESTRITAMENTE CONFIDENCIAL

---

## 1. SUMÁRIO EXECUTIVO

### 1.1 Visão Geral

A equipa **Kryzen Team** foi contratada pela **Hack The Box** para realizar um teste de penetração autorizado (*Black-Box*) na infraestrutura da aplicação web **Cap** (IP: `10.129.143.250`). O objetivo principal desta avaliação foi identificar vulnerabilidades de segurança que pudessem ser exploradas por atores maliciosos para comprometer a confidencialidade, integridade e disponibilidade do sistema.

### 1.2 Resumo de Risco

O risco global da aplicação e do servidor foi classificado como **CRÍTICO**.

Foram identificadas falhas graves de controlo de acesso no sistema web e configurações inadequadas de permissões no sistema operativo Linux. A exploração encadeada destas falhas permitiu a um atacante não autenticado obter acesso inicial ao servidor e, em seguida, elevar privilégios para acesso total de superutilizador (`root`).

| Nível de Risco | Quantidade |
| --- | --- |
| **Crítico** | 1 |
| **Alto** | 1 |
| **Médio** | 0 |
| **Baixo** | 0 |

---

## 2. ESCOPO E METODOLOGIA

### 2.1 Escopo dos Testes

* **Endereço IP Alvo:** `10.129.143.250`
* **Serviços Avaliados:**
* Servidor Web HTTP (Porta `80`)
* Servidor FTP (Porta `21`)
* Servidor SSH (Porta `22`)



### 2.2 Metodologia

A avaliação seguiu padrões internacionais de testes de penetração, incluindo:

* **OWASP Top 10** (para análise de vulnerabilidades na aplicação web)
* **PTES** (*Penetration Testing Execution Standard*)

---

## 3. RELATÓRIO TÉCNICO DE VULNERABILIDADES

### [VULN-01] Insecure Direct Object Reference (IDOR) no Download de Capturas de Rede

* **Severidade:** Alta (CVSS v3.1: 7.5 — `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N`)
* **URL Afetada:** `[http://10.129.143.250/data/](http://10.129.143.250/data/){id}`
* **CWE Relacionado:** CWE-639 (Insecure Direct Object Reference)

#### Descrição

A aplicação web permite a visualização e download de ficheiros de captura de tráfego de rede (`.pcap`) através de um parâmetro numérico sequencial na URL. O backend falha ao não validar se a requisição pertence ao utilizador autenticado na sessão, permitindo a enumeração e extração ilícita de ficheiros de terceiros.

#### Prova de Conceito (PoC)

1. Navegou-se até ao recurso de captura gerado pela aplicação na URL: `[http://10.129.143.250/data/1](http://10.129.143.250/data/1)`.
2. Alterou-se manualmente o parâmetro numérico para `0` na barra de endereços: `[http://10.129.143.250/data/0](http://10.129.143.250/data/0)`.
3. O servidor respondeu com os dados da captura de rede referente ao ID `0`.
4. Ao analisar o ficheiro `.pcap` descarregado, identificou-se o tráfego do serviço FTP contendo credenciais em texto claro do utilizador `nathan`:
* **Utilizador:** `nathan`
* **Serviço:** FTP / SSH



#### Impacto

Exposição de informações confidenciais de tráfego de rede e vazamento de credenciais de acesso do sistema, permitindo que um atacante obtenha acesso inicial remoto via SSH.

#### Remediação Recomendada

1. **Controlo de Acesso Baseado em Sessão:** Validar no backend se o ID solicitado pertence estritamente ao utilizador autenticado.
2. **Uso de UUIDs:** Substituir IDs numéricos sequenciais por identificadores únicos não previsíveis (ex.: UUIDv4).

---

### [VULN-02] Elevação de Privilégios via Linux Capabilities Inseguras (`cap_setuid`)

* **Severidade:** Crítica (CVSS v3.1: 9.8 — `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`)
* **Ficheiro Afetado:** `/usr/bin/python3.8`
* **CWE Relacionado:** CWE-250 (Execution with Unnecessary Privileges)

#### Descrição

O binário executável do Python 3.8 possui a *capability* especial `cap_setuid` atribuída. Esta permissão permite que qualquer utilizador comum invoque a chamada de sistema `setuid(0)` para alterar o ID do seu processo para `root` sem a necessidade de autenticação via `sudo`.

#### Prova de Conceito (PoC)

1. Após obter acesso via SSH com a conta do utilizador `nathan` (obtida na **VULN-01**), executou-se a enumeração de capacidades do sistema:
```bash
getcap -r / 2>/dev/null

```


**Saída do comando:**
```text
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip

```


2. Executou-se o seguinte comando para alterar o UID do processo para `0` e invocar uma nova shell:
```bash
python3.8 -c 'import os; os.setuid(0); os.system("/bin/bash")'

```


3. O comando concedeu com sucesso um terminal interativo com privilégios de superutilizador (`root`).

#### Impacto

Comprometimento total do sistema operativo. Um atacante obtém controlo irrestrito sobre o servidor, podendo alterar configurações, instalar malwares, apagar registos de auditoria e aceder a todos os dados armazenados.

#### Remediação Recomendada

Remover a capacidade `cap_setuid` do binário do Python executando o comando:

```bash
sudo setcap -r /usr/bin/python3.8

```

---

## 4. PLANO DE AÇÃO E REMEDIAÇÃO PRIORIZADA

1. **Imediato (Nas primeiras 24 horas):** Remover a *capability* `cap_setuid` do binário `/usr/bin/python3.8` para fechar o vetor de elevação de privilégios local.
2. **Curto Prazo (Até 7 dias):** Corrigir a lógica de autorização no endpoint `/data/{id}` da aplicação web e alterar a palavra-passe do utilizador `nathan`.
