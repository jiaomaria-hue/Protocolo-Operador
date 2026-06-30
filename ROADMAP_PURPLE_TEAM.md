# 🏆 ROADMAP PURPLE TEAM — DEFINITIVO.
### Fusão Profissional · ~19 Meses · Joao · Palmas, TO
> "Operar a detecção que alguém te deu é Tier 1. Projetar a detecção que ninguém te deu, em qualquer stack, contra um padrão mínimo conhecido, é Purple Team."

---

## ⚠️ AVISOS FIXOS — LÊ ANTES DE COMEÇAR

### 🔴 Aviso de Inglês
Este roadmap usa fontes majoritariamente em inglês. Os pontos críticos estão marcados com **[🇺🇸 INGLÊS NECESSÁRIO]**. Solução: Anki com 15 palavras técnicas por dia desde agora. Quando travar numa fonte, resolve o vocabulário daquele conteúdo específico e continua — não pula.

### 🔴 Aviso de Execução
Você está na v8. O risco real não é técnico — é ficar refinando plano em vez de executar. A partir de agora: **nenhuma edição no roadmap enquanto estiver dentro de um bloco.** Edições só acontecem na semana de descanso entre blocos, com base no que você viveu, não no que imaginou.

### 🔴 Aviso de Atraso
Se um sprint atrasar mais de 2 semanas: **não compensa o atraso**. Entrega o que tem, documenta o que ficou faltando no LOG_DE_GUERRA, e avança. Atraso acumulado mata roadmap.

### 🔴 Aviso de Visibilidade
Você não existe para o mercado enquanto não aparecer. Postar 1 vez por mês no LinkedIn a partir do Bloco 2 não é opcional — é parte do protocolo. Presença pública construída ao longo do tempo vale mais do que 2 semanas de post no final.

---

## 📐 ESTRUTURA GERAL

```
BLOCO 1  →  Semanas 1–24    (~6 meses)     FUNDAÇÃO + RED TEAM
BLOCO 2  →  Semanas 25–61   (~9 meses)     BLUE TEAM
BLOCO 3  →  Semanas 62–85   (~6 meses)     ELITE / PURPLE TEAM

TOTAL: ~85 semanas ≈ 19,5 meses
```

---

## 🗓️ GRADE DIÁRIA — REGRAS FIXAS

> Válidas para todos os blocos. O conteúdo muda sprint a sprint — as regras não.

| Regra | Detalhe |
|---|---|
| **Anki todo dia** | 15 palavras, últimos 15 min. O algoritmo de repetição espaçada quebra se pular. |
| **Commit obrigatório** | Seg, ter, qua, qui, sex e sáb. Se não commitou, o dia não existiu. |
| **Domingo é OFF** | Sem leitura. Sem lab. Sem "opcional". Sem exceção nas primeiras 4 semanas. |
| **LOG_DE_GUERRA toda sexta** | Erros da semana entram antes de fechar o dia. |
| **Sinal de colapso** | Semana inteira sem commit = grade quebrou. Para, identifica o dia que falhou, corrige. |

**Horário de férias:** 14:30–18:50 (4h20/dia) · 40 dias · 23 jun → 2 ago
**Cobertura das férias:** Sprint 1 + Sprint 2 completos + ~8 dias do Sprint 3
**Horário escolar:** 14:30–16:50 semana, 14:30–17:50 fim de semana — grade revisada no fim das férias.

### ⚠️ Exceções Semanais Fixas

**Terça — Curso 16:00–18:30 + Krav Maga 19:30–21:00**
| Horário | O que fazer |
|---|---|
| 14:30–15:45 | Conteúdo do sprint |
| 15:45–16:00 | Commita + Anki 15 palavras |
| 16:00–18:30 | Curso |
| 18:30–19:30 | Se arrumar + deslocamento |
| 19:30–21:00 | Krav Maga |

> 1h30 de estudo. Dia curto — aceita e segue.

**Quarta — Curso 14:00–16:30/17:30**
| Horário | O que fazer |
|---|---|
| 14:00–16:30 | Curso |
| 16:30–18:35 | Conteúdo do sprint |
| 18:35–18:50 | Commita + Anki 15 palavras |

> 2h05 de estudo. Dia curto — aceita e segue.

**Quinta — Krav Maga 19:30–21:00**
| Horário | O que fazer |
|---|---|
| 14:30–19:00 | Grade normal do sprint |
| 19:00–19:30 | Commita + Anki + fecha LOG |
| 19:30–21:00 | Krav Maga |

> 4h30 de estudo. Dia quase completo.

---

## 🌍 CAMADAS TRANSVERSAIS

### Inglês Técnico
| Período | O que praticar |
|---|---|
| Semanas 1–8 | docs.python.org — lê a documentação das funções que usa |
| Semanas 9–24 | Man pages do Nmap, docs do Wireshark |
| Semanas 25–61 | Documentação Wazuh, KQL docs, MITRE ATT&CK |
| Semanas 62–85 | White papers de Purple Team, Detection Engineering papers |

**Método:** Anki, 15 palavras técnicas/dia. Quando travar numa fonte, resolve aquele vocabulário específico e continua.

### Presença Pública — A partir do Bloco 2
A partir do Sprint 1 do Bloco 2: **1 post técnico por mês no LinkedIn**, sem exceção. Não precisa ser artigo profundo. "Hoje configurei Sysmon e descobri que o Windows nativo não loga process injection sem ele" já é conteúdo válido.

### Dia de Quebra — 1x por mês
Quebre o ambiente de propósito (VM, venv, dependência) e restaure sem ajuda.

### Código de Conduta do Operador
1. **Regra dos 15 min** — travou? Pesquisa 15 min. Não resolveu? Pergunta.
2. **LOG_DE_GUERRA.md** — todo erro resolvido vira entrada: data, problema, tentativas, solução.
3. **Ambiente impecável** — código limpo, comentado, funcional.
4. **Automação sempre** — fez manual 2x? Na 3ª, vira script.
5. **Git é sagrado** — todo arquivo vai pro GitHub no mesmo dia.

### Progressão de Linguagens
```
Semana 1        →  Python
Semanas 9–24    →  Bash + SQL
Semanas 25–61   →  PowerShell + KQL + SPL (Splunk)
Semanas 70–71   →  C básico (pré-requisito para RE)
Semanas 72–73   →  Assembly x86/x64 + Ghidra
```

### Regra de Produção Contínua
A partir do Bloco 2 Sprint 5, para cada técnica ATT&CK estudada:
> **1 regra própria (Sigma, KQL, SPL ou EQL) + 1 entrada no LOG_DE_DETECCAO.md explicando a lógica.**

### Regra de Produção de Código
A partir do Bloco 2 Sprint 1, para cada sprint:
> **Mínimo 1 script próprio entregue e commitado no GitHub.**

Exemplos:
- Parser de log que destaca linhas suspeitas
- Script que verifica se regras Sigma estão ativas no SIEM
- Coletor de evidências de artefatos de comprometimento
- Gerador de relatório forense em Markdown
- Automação de IOC contra VirusTotal API

### Regra de Qualidade de Detecção
Toda entrada no LOG_DE_DETECCAO.md precisa de 2 números:
> **Taxa de detecção em teste (mínimo 80%) + nota de falso positivo observado.**

Regra sem esses dois números não conta para o gate final.

### Catálogo de Técnicas Obrigatórias
**Mínimo obrigatório: 11 técnicas.** Meta recomendada: 20+ técnicas.

**11 técnicas obrigatórias:**

| Tática | Técnica | ID |
|---|---|---|
| Execução | PowerShell | T1059.001 |
| Execução | WMI | T1047 |
| Persistência | Registry Run Keys | T1547.001 |
| Persistência | Scheduled Task | T1053.005 |
| Acesso a Credenciais | LSASS Dump | T1003.001 |
| Acesso a Credenciais | Kerberoasting | T1558.003 |
| Movimentação Lateral | SMB/Admin Shares | T1021.002 |
| C2 | Web Protocols | T1071.001 |
| C2 | Ingress Tool Transfer | T1105 |
| Identidade | Valid Accounts | T1078 |
| Exfiltração | Exfiltration Over C2 | T1041 |

**9 técnicas recomendadas (meta 20+):**

| Tática | Técnica | ID |
|---|---|---|
| Acesso a Credenciais | DCSync | T1003.006 |
| Acesso a Credenciais | Pass-the-Hash | T1550.002 |
| Acesso a Credenciais | Golden Ticket | T1558.001 |
| Acesso a Credenciais | Silver Ticket | T1558.002 |
| Movimentação Lateral | RDP | T1021.001 |
| Execução | PsExec (via SMB) | T1569.002 |
| Execução | PowerShell Empire/C2 framework | T1059.001 |
| Evasão | DLL Search Order Hijacking | T1574.001 |
| Persistência | Service Creation | T1543.003 |

### Aviso de Ritmo
Após cada bloco: **1 semana de descanso ativo** antes do próximo. Descanso ativo = revisar LOG_DE_GUERRA, organizar GitHub, planejar próximo bloco.

---

# 🧱 BLOCO 1 — FUNDAÇÃO + RED TEAM (Semanas 1–24)

---

## Sprint 1 (Semanas 1–4) — Linux + Python Básico

**Objetivo:** Terminal sem mouse, Python com lógica real.
**Teoria:** Comandos essenciais Linux, estruturas Python (variáveis, condicionais, loops, funções).
**Lab:** Zorin OS como ambiente principal — sem GUI quando possível.
**Projeto:** `firewall_logic.py` funcionando ✅ *(commita no GitHub se ainda não fez)*
**Checkpoint:** [ ] Navega no terminal sem consultar nada. [ ] Escreve uma função Python do zero sem copiar.

### 🗓️ Grade Diária — Sprint 1 (Férias · 14:30–18:50)

**Segunda — Python / Código**
| Horário | O que fazer |
|---|---|
| 14:30–14:45 | Revisão do dia anterior — LOG ou GitHub |
| 14:45–16:30 | Conteúdo do sprint — escreve código novo |
| 16:30–17:30 | Exercício prático do que estudou |
| 17:30–18:30 | Resolve bug / aprofunda conceito que travou |
| 18:30–18:35 | Commita no GitHub + 1 linha no LOG_DE_GUERRA |
| 18:35–18:50 | Anki — 15 palavras técnicas em inglês |

**Terça — EXCEÇÃO: Curso 16:00–18:30 + Krav Maga 19:30–21:00**
| Horário | O que fazer |
|---|---|
| 14:30–15:45 | Linux / Terminal — pratica comandos do sprint |
| 15:45–16:00 | Commita + Anki 15 palavras |
| 16:00–18:30 | Curso |
| 18:30–19:30 | Se arrumar + deslocamento |
| 19:30–21:00 | Krav Maga |

> 1h30 de estudo. Dia curto — aceita e segue.

**Quarta — EXCEÇÃO: Curso 14:00–16:30**
| Horário | O que fazer |
|---|---|
| 14:00–16:30 | Curso |
| 16:30–18:35 | Python / Conceito difícil da semana |
| 18:35–18:50 | Commita + Anki 15 palavras |

> 2h05 de estudo. Dia curto — aceita e segue.

> ⚠️ Quarta vira Redes/Cisco a partir do Sprint 3 (semana 9). Até lá, é Python.

**Quinta — EXCEÇÃO: Krav Maga 19:30–21:00**
| Horário | O que fazer |
|---|---|
| 14:30–17:00 | TryHackMe — sem interrupção |
| 17:00–18:20 | Documenta o que travou e o que resolveu |
| 18:20–18:30 | Atualiza LOG_DE_GUERRA |
| 18:30–18:35 | Commita |
| 18:35–18:50 | Anki — 15 palavras |
| 19:30–21:00 | Krav Maga |

> 4h30 de estudo. Dia quase completo.

**Sexta — Revisão Semanal**
| Horário | O que fazer |
|---|---|
| 14:30–15:30 | Revisão da semana — relê LOG, testa conceitos de cabeça sem consultar |
| 15:30–17:30 | Refaz exercício que travou durante a semana |
| 17:30–18:30 | Fecha o LOG_DE_GUERRA da semana — erros resolvidos documentados |
| 18:30–18:35 | Commita |
| 18:35–18:50 | Anki — 15 palavras |

**Sábado — Projeto / Portfólio**
| Horário | O que fazer |
|---|---|
| 14:30–17:00 | Trabalha no projeto do sprint — entregável pro GitHub |
| 17:00–18:30 | Documenta, refina, commita |
| 18:30–18:35 | Commita final da semana |
| 18:35–18:50 | Anki + planeja o que vai fazer na segunda |

**Domingo — OFF TOTAL**
> Sem leitura. Sem lab. Sem "opcional". Cérebro precisa consolidar o que absorveu.

---

## Sprint 2 (Semanas 5–8) — Python Aplicado + Git

**Objetivo:** Primeiro projeto real no portfólio.
**Teoria:** Módulos Python (socket, os, subprocess), Git workflow.
**Lab:** Construir ferramentas que resolvem problemas reais.
**Projeto:** Port scanner funcional no GitHub ✅ *(garante que está documentado com README)*
**Checkpoint:** [ ] Repositório GitHub organizado com README, commits diários. [ ] Explica cada linha do port scanner.

> **[🇺🇸 INGLÊS NECESSÁRIO]** A partir daqui, docs.python.org vai ser sua referência principal.

### 🗓️ Grade Diária — Sprint 2 (Férias · 14:30–18:50)

**Segunda — Python / Módulos**
| Horário | O que fazer |
|---|---|
| 14:30–14:45 | Revisão do dia anterior |
| 14:45–16:30 | Módulos Python — socket, os, subprocess |
| 16:30–17:30 | Exercício prático com o módulo estudado |
| 17:30–18:30 | Trabalha no port scanner — resolve o que travar |
| 18:30–18:35 | Commita |
| 18:35–18:50 | Anki — 15 palavras |

**Terça — EXCEÇÃO: Curso 16:00–18:30 + Krav Maga 19:30–21:00**
| Horário | O que fazer |
|---|---|
| 14:30–15:45 | Git workflow — branches, commits semânticos, README |
| 15:45–16:00 | Commita + Anki 15 palavras |
| 16:00–18:30 | Curso |
| 18:30–19:30 | Se arrumar + deslocamento |
| 19:30–21:00 | Krav Maga |

> 1h30 de estudo. Dia curto — aceita e segue.

**Quarta — EXCEÇÃO: Curso 14:00–16:30**
| Horário | O que fazer |
|---|---|
| 14:00–16:30 | Curso |
| 16:30–18:35 | Python / lógica de rede, tratamento de erros |
| 18:35–18:50 | Commita + Anki 15 palavras |

> 2h05 de estudo. Dia curto — aceita e segue.

**Quinta — EXCEÇÃO: Krav Maga 19:30–21:00**
| Horário | O que fazer |
|---|---|
| 14:30–17:00 | TryHackMe ou exercício de Python aplicado a segurança |
| 17:00–18:20 | Documenta |
| 18:20–18:30 | Atualiza LOG_DE_GUERRA |
| 18:30–18:35 | Commita |
| 18:35–18:50 | Anki — 15 palavras |
| 19:30–21:00 | Krav Maga |

> 4h30 de estudo. Dia quase completo.

**Sexta — Revisão Semanal**
| Horário | O que fazer |
|---|---|
| 14:30–15:30 | Revisão — relê LOG, testa de cabeça |
| 15:30–17:30 | Refaz o que travou |
| 17:30–18:30 | Fecha LOG_DE_GUERRA da semana |
| 18:30–18:35 | Commita |
| 18:35–18:50 | Anki — 15 palavras |

**Sábado — Projeto / Portfólio**
| Horário | O que fazer |
|---|---|
| 14:30–17:00 | Port scanner — finaliza, testa, documenta |
| 17:00–18:30 | README completo + commita no GitHub |
| 18:30–18:35 | Commita final |
| 18:35–18:50 | Anki + planeja segunda |

**Domingo — OFF TOTAL**

---

## Sprint 3 (Semanas 9–14) — Redes Completas

**Objetivo:** OSI na veia, Nmap e Wireshark como extensão da mão.
**Teoria:** Modelo OSI/TCP-IP, protocolos (TCP, UDP, DNS, HTTP, ARP), subnetting.
**Lab:** Nmap contra VMs próprias, Wireshark capturando tráfego real.
**Projeto:** Calculadora de subnet em Python + documentação de 5 scans Nmap com análise.

> **[🇺🇸 INGLÊS NECESSÁRIO]** Man pages do Nmap e docs do Wireshark estão em inglês.

**Checkpoint:** [ ] OSI de cabeça, camada por camada. [ ] Identifica um protocolo num pcap do Wireshark sem ajuda.

### 🗓️ Grade Diária — Sprint 3 em diante (estrutura semanal fixa)

> A partir daqui a escola retorna. Grade escolar será definida ao fim das férias com os horários reais. A estrutura temática dos dias permanece:

| Dia | Foco |
|---|---|
| Segunda | Código / Script do sprint |
| Terça | Terminal / Automação |
| **Quarta** | **Redes / Cisco / Nmap / Wireshark** ← muda aqui |
| Quinta | Lab Prático — TryHackMe / PortSwigger / HackTheBox |
| Sexta | Revisão + LOG_DE_GUERRA + Anki |
| Sábado | Projeto / Portfólio / Entregável |
| Domingo | OFF TOTAL |

---

## Sprint 4 (Semanas 15–18) — Fundamentos Web

**Objetivo:** OWASP Top 10 entendido na prática, não só decorado.
**Teoria:** HTTP/HTTPS, cookies, sessões, OWASP Top 10.
**Lab:** PortSwigger Academy — módulos de SQLi, XSS, IDOR.

> **[🇺🇸 INGLÊS NECESSÁRIO]** PortSwigger Academy está 100% em inglês. Primeiro ponto onde o inglês vai te custar tempo real.

**Projeto:** Relatório documentando 3 vulnerabilidades exploradas no PortSwigger, com causa raiz e mitigação.
**Checkpoint:** [ ] OWASP Top 10 de cabeça. [ ] Burp Suite funcional, intercepta e modifica uma requisição.

---

## Sprint 5 (Semanas 19–22) — Reconhecimento Ofensivo

**Objetivo:** Metodologia de ataque documentada, não só ferramentas.
**Teoria:** Fases de pentest (PTES), reconhecimento passivo e ativo.
**Lab:** TryHackMe — 2 máquinas completas (1 Linux, 1 Windows).
**Projeto:** 2 write-ups completos no GitHub com metodologia, ferramentas e lições aprendidas.
**Checkpoint:** [ ] Explica a diferença entre reconhecimento passivo e ativo. [ ] Write-up estruturado publicado.

---

## Sprint 6 (Semanas 23–24) — Primeiro Pentest Real

**Objetivo:** Relatório profissional — o produto que um cliente receberia.

> **⚠️ GATE CONSTRUÍDO:** Este sprint transforma o que você aprendeu nos Sprints 3–5 num entregável profissional. Se os write-ups dos Sprints 5 não estiverem sólidos, fica mais uma semana neles antes de avançar.

**Teoria:** Estrutura de relatório de pentest (Executive Summary, Findings, Recomendações).
**Lab:** HackTheBox — 1 máquina introdutória completa.
**Projeto:** Relatório de Pentest em PDF, estrutura profissional.
**Checkpoint:** [ ] Relatório com pelo menos 3 findings documentados, cada um com evidência, impacto e recomendação.

**Gate de saída do Bloco 1:**
- [ ] 24 entradas no LOG_DE_GUERRA (mínimo)
- [ ] Relatório de Pentest formal no portfólio
- [ ] Repositório GitHub organizado: scripts, write-ups, relatório, README
- [ ] Explica toda a metodologia de ataque sem consultar nada
- [ ] Port scanner e firewall_logic.py documentados e commitados

---

# 🛡️ BLOCO 2 — BLUE TEAM (Semanas 25–61)

> **A partir daqui: 1 post técnico por mês no LinkedIn. Sem exceção.**

---

## Sprint 1 (Semanas 25–26) — Hardening Linux

**Objetivo:** Fechar as portas que você abriu como atacante.
**Teoria:** CIS Benchmarks básico, princípio do menor privilégio, hardening de SSH.
**Lab:** Aplicar hardening na própria VM atacada no Bloco 1.
**Projeto:** Checklist de hardening + script de auditoria em Python.
**Checkpoint:** [ ] VM atacada agora resiste aos mesmos exploits usados antes.

### 🗓️ Grade Diária — Bloco 2 (estrutura semanal fixa)

| Dia | Foco |
|---|---|
| Segunda | SIEM / Detecção — escreve ou ajusta 1 regra com taxa e FP |
| Terça | Script do sprint — commita no GitHub |
| Quarta | KQL / SPL / EQL — 1 query nova escrita do zero |
| Quinta | Lab Ativo — TryHackMe IR, forense, cloud |
| Sexta | Revisão + LOG_DE_DETECCAO + Anki 15 palavras |
| Sábado | Projeto do sprint — entregável commitado |
| Domingo | OFF TOTAL |

---

## Sprint 2 (Semanas 27–28) — Hardening Windows

**Objetivo:** Mesma lógica, ambiente Windows.
**Teoria:** Group Policy básico, desativação de serviços desnecessários.
**Lab:** Hardening da VM Windows atacada no Bloco 1.
**Projeto:** Documentação comparando antes/depois do hardening.
**Checkpoint:** [ ] Explica 3 mudanças de configuração que fecharam vetores de ataque.

---

## Sprint 3 (Semanas 29–30) — Análise de Logs

**Objetivo:** Diferenciar tráfego normal de ataque, na prática.
**Teoria:** Logs do /var/log, Windows Event Viewer, estrutura de log.
**Lab:** TryHackMe — sala "Intro to Logs".
**Projeto:** Analisar um log de ataque simulado e identificar a intrusão.
**Checkpoint:** [ ] Identifica um ataque dentro de um log sem dica.

---

## Sprint 4 (Semanas 31–34) — SIEM com Wazuh

**Objetivo:** Implantar detecção real.
**Teoria:** Arquitetura de SIEM, regras de detecção, alertas.
**Lab:** Instalar Wazuh numa VM e conectar como agente na máquina atacada do Bloco 1.
**Projeto:** SIEM detectando, ao vivo, os ataques documentados no Bloco 1.

> **[🇺🇸 INGLÊS NECESSÁRIO]** Documentação do Wazuh está em inglês.

> **⚠️ REGRA DO WAZUH:** Se após 2 semanas o Wazuh não estiver gerando alertas funcionais, para. Documenta o problema no LOG_DE_GUERRA, troca para **Security Onion** temporariamente e continua. O objetivo é aprender detecção, não virar administrador de SIEM.

**Checkpoint:** [ ] SIEM (Wazuh ou Security Onion) gera alerta real para um ataque replicado.

---

## ⭐ Sprint 4.5 (Semana 35) — Sysmon: Telemetria que Alimenta Tudo

**Objetivo:** Sem Sysmon, suas regras Windows detectam com os olhos fechados.
**Teoria:** O que o Sysmon é e por que existe. Event IDs principais:
- **Event ID 1** — Process Creation (base de T1059.001, T1047, T1569.002)
- **Event ID 3** — Network Connection (base de T1071.001, T1105)
- **Event ID 7** — Image Loaded / DLL Load (base de T1574.001)
- **Event ID 10** — Process Access (base de T1003.001 — LSASS dump)
- **Event ID 11** — File Create (base de T1547.001, T1053.005)
- **Event ID 13** — Registry Value Set (base de T1547.001)

**Lab:** Instalar Sysmon na VM Windows com config SwiftOnSecurity. Replicar 2 ataques do Bloco 1 e comparar: Windows Event Viewer nativo vs Sysmon.

> **[🇺🇸 INGLÊS NECESSÁRIO]** Config SwiftOnSecurity e documentação do Sysmon estão em inglês.

**Projeto:** Documento comparativo: "Log nativo vs Sysmon para os mesmos 2 ataques."
**Checkpoint:** [ ] Sysmon instalado e gerando logs. [ ] Consegue filtrar Event ID 1 e 10 no Wazuh e identificar processo suspeito por nome e linha de comando.

---

## ⭐ Sprint 5 (Semanas 36–37) — Detection Engineering às Escuras

**Objetivo:** A diferença entre operar detecção e projetar detecção.
**Teoria:** Estrutura de uma regra Sigma, como ler um TTP do MITRE ATT&CK e traduzir em lógica de detecção sem ter executado o ataque antes.
**Lab:** Escolher 3 técnicas do MITRE ATT&CK que você **nunca simulou**. Sem atacar primeiro, escrever a regra. Depois, simular e testar.
**Projeto:** Documento com as 3 regras escritas antes do ataque + resultado + o que foi ajustado. Abre o LOG_DE_DETECCAO.md aqui.
**Checkpoint:** [ ] Pelo menos 1 das 3 regras detectou o ataque sem ajuste. [ ] As 3 têm taxa de detecção e nota de FP registradas.

> A Regra de Produção Contínua e a Regra de Qualidade entram em vigor a partir deste sprint.

---

## ⭐ Sprint 5.5 (Semana 38) — Telemetria → Hipótese → Detecção

**Objetivo:** O salto que separa quem opera detecção de quem projeta.
**Teoria:** Como um Detection Engineer sênior raciocina a partir de anomalia, não de TTP conhecido.
**Lab:** Pegar os logs do Sysmon e dos ataques do Bloco 1 e fazer o exercício sem consultar write-up:
1. Olhar os logs sem saber qual ataque foi executado
2. Identificar anomalias pelo padrão
3. Formular hipótese
4. Confirmar ou descartar consultando ATT&CK depois

**Projeto:** Documento com raciocínio completo: anomalia → hipótese → TTP confirmado → regra criada. Pelo menos 2 ciclos. Entra no LOG_DE_DETECCAO.md.
**Checkpoint:** [ ] Identifica pelo menos 1 técnica ATT&CK partindo de anomalia nos logs, sem saber de antemão. [ ] Documenta o raciocínio, não só a conclusão.

---

## ⭐ Sprint 6 (Semanas 39–41) — KQL e Threat Hunting com Sentinel/Defender

**Objetivo:** Segunda linguagem de detecção — obrigatória para stack Microsoft.
**Teoria:** Sintaxe básica de KQL, tabelas no Log Analytics, diferença entre regra de detecção e query de hunting.
**Lab:** Conta trial do Microsoft Sentinel ou Defender. Reescrever em KQL 2 das regras Sigma do Sprint 5. Rodar 1 hunting query contra logs de exemplo.

> **[🇺🇸 INGLÊS NECESSÁRIO]** KQL docs e repositórios públicos de hunting queries estão em inglês.

**Projeto:** Documento comparativo Sigma vs KQL para a mesma detecção.
**Checkpoint:** [ ] Escreve uma query KQL de hunting do zero para uma técnica ATT&CK simples, sem copiar de exemplo.

---

## ⭐ Sprint 6.5 (Semana 42) — Splunk: Exposição à Stack Dominante

**Objetivo:** Remover o "nunca vi Splunk" — eliminador de vagas que o restante do roadmap te qualificaria a disputar.

> **Por que Splunk entra aqui:** O mercado BR e remoto de Purple Team/Detection Engineering usa Splunk como stack primária em empresas de médio/grande porte. Chegar numa entrevista com Sigma, KQL e EQL sem nunca ter visto SPL é gap eliminatório.

**Teoria:** Arquitetura básica do Splunk (indexer, search head, forwarder), SPL básico — comparação direta com KQL.
**Lab:** Splunk Free Trial. Ingerir logs que você já tem (Sysmon, Wazuh) e reescrever 1 das regras KQL do Sprint 6 em SPL.

> **[🇺🇸 INGLÊS NECESSÁRIO]** Documentação do Splunk está em inglês.

**Projeto:** Adicionar ao documento do Sprint 6 uma terceira coluna: mesma detecção em Sigma, KQL e SPL lado a lado.
**Checkpoint:** [ ] 1 regra funcional em SPL, validada contra os mesmos logs.

---

## ⭐ Sprint 7 (Semana 43) — Elastic Security: Terceira Stack

**Objetivo:** Remover o "nunca vi isso" para o caso de a vaga pedir Elastic.
**Teoria:** Detection rule no Elastic Security, diferença entre EQL e KQL/SPL/Sigma.
**Lab:** Trial do Elastic Security. Traduzir 1 regra para EQL e validar.
**Projeto:** Documento comparativo final: Sigma | KQL | SPL | EQL — quatro stacks, mesma detecção.
**Checkpoint:** [ ] 1 regra funcional em EQL, validada.

---

## Sprint 8 (Semanas 44–45) — Firewalls na Prática

**Objetivo:** UFW e Iptables aplicados.
**Teoria:** Regras de entrada/saída, NAT sob ótica defensiva.
**Lab:** Configurar regras que bloqueiam o scan do Bloco 1.
**Projeto:** Script que audita regras de firewall ativas.
**Checkpoint:** [ ] Nmap scan contra a VM retorna portas filtradas, não abertas.

---

## Sprint 9 (Semanas 46–48) — Resposta a Incidentes

**Objetivo:** Saber agir quando o ataque já aconteceu.
**Teoria:** Ciclo de IR (Preparação → Identificação → Contenção → Erradicação → Recuperação → Lições Aprendidas).
**Lab:** TryHackMe — sala de Incident Response introdutória.

> **⚠️ PONTO DE ATENÇÃO:** IR é onde Purple Team júnior mais perde em entrevistas. O projeto precisa simular um incidente real do início ao fim.

**Projeto:** Plano de resposta a incidente escrito + simulação documentada de um incidente completo.
**Checkpoint:** [ ] Cita as 6 fases do IR com exemplo prático de cada uma, sem consultar.

---

## Sprint 10 (Semanas 49–50) — Forense Digital Básico

**Objetivo:** Investigar depois do ataque.
**Teoria:** Artefatos de memória e disco, cadeia de custódia.
**Lab:** TryHackMe — sala de forense introdutória.
**Projeto:** Relatório forense básico de uma máquina comprometida (lab controlado).
**Checkpoint:** [ ] Identifica 2 artefatos de comprometimento numa imagem de disco/memória.

---

## Sprint 11 (Semanas 51–52) — IAM, MFA, SSO

**Objetivo:** Entender gestão de identidade.
**Teoria:** Autenticação vs autorização, MFA (TOTP, FIDO2), SSO.
**Lab:** Configurar MFA num serviço próprio (GitHub, e-mail).
**Projeto:** Documento explicando por que MFA sozinho não impede todos os ataques (ex: MFA fatigue).
**Checkpoint:** [ ] Explica autenticação vs autorização sem hesitar.

---

## ⭐ Sprint 12 (Semanas 53–57) — Cloud Security: Proteção + Detecção

**Objetivo:** Purple Team em cloud significa detectar e caçar ameaças — não só proteger.
**Teoria:**
- Semanas 53–54: IAM em nuvem, políticas, misconfigurações comuns (buckets/blobs públicos), AWS e Azure.
- Semanas 55–57: CloudTrail (AWS) e Azure Activity Logs, GuardDuty, Microsoft Defender for Cloud, hunting query KQL para Azure Activity Logs.

**Lab parte 1:** AWS Free Tier + Azure Student — criar e auditar ambiente com permissões corretas.
**Lab parte 2:** Gerar evento suspeito controlado e encontrá-lo via CloudTrail/GuardDuty e Activity Logs/Defender for Cloud.

> **[🇺🇸 INGLÊS NECESSÁRIO]** Documentação AWS e Azure está majoritariamente em inglês.

**Projeto:** Comparativo documentado de detecção cloud: como AWS e Azure sinalizam o mesmo evento suspeito.
**Checkpoint:** [ ] Identifica misconfiguration clássica em S3 e Blob Storage. [ ] Encontra evento suspeito simulado usando ferramentas nativas de ambas as clouds.

---

## Sprint 13 (Semanas 58–59) — Contêineres e DevSecOps

**Objetivo:** Segurança em Docker e pipelines.
**Teoria:** Superfície de ataque de containers, scanning de imagem, CI/CD seguro.
**Lab:** Rodar container vulnerável conhecido e identificar a falha.
**Projeto:** Dockerfile hardenizado + documentação do que foi corrigido.
**Checkpoint:** [ ] Explica por que rodar container como root é perigoso.

---

## Sprint 14 (Semanas 60–61) — NIST CSF — Estudo de Caso Real

**Objetivo:** Falar a língua de governança do mercado corporativo, com prática real.
**Teoria:** As 6 funções do NIST CSF 2.0 (Governar, Identificar, Proteger, Detectar, Responder, Recuperar).
**Lab:** Escolher um vazamento/incidente público documentado e mapear o que a empresa fez certo/errado em cada função.
**Projeto:** Relatório: "Onde o NIST CSF teria evitado este incidente" + mapear os próprios projetos do Bloco 2 contra o framework.
**Checkpoint:** [ ] Cita as 6 funções do NIST CSF de cabeça e aplica num caso real.

**Gate de saída do Bloco 2:**
- [ ] SIEM detectando ao vivo ataques do Bloco 1 (Wazuh)
- [ ] 3 regras escritas "no escuro" com resultado, taxa de detecção e nota de FP documentadas
- [ ] Pelo menos 2 regras traduzidas entre Sigma, KQL, SPL e EQL — documento comparativo com as 4 stacks
- [ ] LOG_DE_DETECCAO.md ativo com 1 regra por técnica ATT&CK estudada desde o Sprint 5, cada uma com taxa e nota de FP
- [ ] Hardening documentado (Linux + Windows) com antes/depois
- [ ] Simulação completa de IR (não só teoria) + relatório forense no portfólio
- [ ] Lab de Cloud documentado em AWS e Azure, cobrindo proteção e detecção
- [ ] Estudo de caso NIST CSF com incidente real
- [ ] Explica IAM, MFA, NIST CSF, KQL básico, SPL básico, EQL básico sem consultar nada
- [ ] Pelo menos 14 scripts próprios commitados no GitHub (1 por sprint do Bloco 2)
- [ ] Pelo menos 6 posts técnicos no LinkedIn publicados

---

# 🎯 BLOCO 3 — ELITE / PURPLE TEAM REAL (Semanas 62–85)

---

## Sprint 1 (Semanas 62–64) — Active Directory: Fundamentos e Ataque

**Objetivo:** Entender e atacar AD pela primeira vez.
**Teoria:** Estrutura de domínio, Trusts, Forests, autenticação Kerberos em detalhe — AS-REQ, AS-REP, TGS-REQ, TGS-REP.
**Lab:** TryHackMe — AD Basics + HackTheBox — máquina AD introdutória. Não avança para BloodHound até conseguir explicar Kerberos de cabeça.

> **[🇺🇸 INGLÊS NECESSÁRIO]** HackTheBox e recursos sérios de AD estão em inglês.

**Projeto:** Write-up do primeiro comprometimento de domínio com diagrama do fluxo Kerberos anotado.
**Checkpoint:** [ ] Explica o fluxo de autenticação Kerberos de cabeça, etapa por etapa, sem consultar.

### 🗓️ Grade Diária — Bloco 3 (estrutura semanal fixa)

| Dia | Foco |
|---|---|
| Segunda | Ataque (Red) — executa TTP, documenta evidências, previsão de detecção primeiro |
| Terça | Defesa (Blue) — escreve/ajusta regra para o ataque de segunda, valida no SIEM |
| Quarta | Conteúdo denso do sprint — Kerberos, BloodHound, Assembly, conforme sprint |
| Quinta | HackTheBox / CTF — sem write-up de apoio, tenta sozinho primeiro |
| Sexta | Revisão + ATT&CK Navigator — mapeia o que atacou/detectou, confere catálogo |
| Sábado | Portfólio / Presença Pública — write-up, post técnico, projeto final |
| Domingo | OFF TOTAL |

---

## Sprint 2 (Semanas 65–67) — Active Directory: BloodHound, Mimikatz, Impacket e Ataques de Credencial

**Objetivo:** Mapear e explorar caminhos de ataque em AD.
**Teoria:** Movimentação lateral, delegação, persistência em domínio, Pass-the-Hash (T1550.002), DCSync (T1003.006), Golden Ticket (T1558.001).
**Ferramentas:**
- **BloodHound** — mapeamento de caminhos de ataque em AD
- **Mimikatz** — extração de credenciais e hashes do Windows
- **Impacket** — manipulação de protocolos de rede (SMB, Kerberos, DCSync)

**Lab:** Lab de AD com BloodHound mapeando caminho de ataque completo. Executar pelo menos 2 ataques de credencial usando Mimikatz e Impacket.
**Projeto:** Grafo de ataque do BloodHound documentado + write-up de pelo menos 1 ataque de credencial com evidência capturada.
**Checkpoint:** [ ] Identifica caminho de privesc usando BloodHound sem ajuda. [ ] Executa DCSync ou Pass-the-Hash em lab controlado e documenta.

---

## Sprint 3 (Semanas 68–69) — Active Directory: Defesa

**Objetivo:** Fechar o que você acabou de abrir — com detecções para múltiplos ataques.
**Teoria:** Detecção de Kerberoasting, DCSync, Pass-the-Hash, hardening de GPO, Tiering Model, Protected Users group.
**Lab:** Para cada ataque executado no Sprint 2, escrever a regra de detecção **antes** de executar de novo. Validar no SIEM.
**Projeto:** Documentação Purple Team completa para pelo menos 2 ataques de AD: previsão → ataque → detecção → resposta → hardening. Entra no LOG_DE_DETECCAO.md.
**Checkpoint:** [ ] SIEM detecta ataque de AD replicado ao vivo, com regra escrita antes do teste. [ ] Pelo menos 2 técnicas de AD têm regra própria no LOG.

---

## Sprint 4 (Semanas 70–73) — Engenharia Reversa: da Base ao Binário

**Objetivo:** Primeiro contato real com análise de binários.
**Teoria:**
- Semanas 70–71: C básico — variáveis, ponteiros, como função vira instruções de máquina.
- Semanas 72–73: Assembly x86/x64 básico, registradores, como Ghidra desmonta um binário.

**Lab:** Ghidra analisando um binário simples (crackme introdutório) — só depois de ter compilado pelo menos 3 programas em C.
**Projeto:** Relatório de RE de um crackme nível iniciante, explicando relação entre C equivalente e assembly do Ghidra.
**Checkpoint:** [ ] Identifica função principal de binário simples no Ghidra e explica o bloco de assembly correspondente.

> **Decisão ao final deste sprint:** Decida e documente — continua RE pós-protocolo ou foi suficiente. Não existe meio-termo.

---

## ⭐ Sprint 5 (Semanas 74–78) — Pós-Exploração, Persistência e Fechamento do Catálogo

**Objetivo:** O que acontece depois que a porta é arrombada — e cobertura das técnicas do Catálogo que faltarem.
**Teoria:** Mecanismos de persistência, exfiltração de dados, C2 básico — T1003.001, T1547.001, T1053.005, T1071.001, T1105, T1041.
**Ferramentas:**
- **Atomic Red Team** — biblioteca de testes atômicos por TTP do MITRE ATT&CK. Executa uma técnica específica e verifica imediatamente se o SIEM alertou.
- **CALDERA** — emulação adversarial automatizada desenvolvida pela MITRE. Permite planejar e executar cenários de ataque completos baseados em TTPs reais.
- **Velociraptor** — threat hunting em endpoints e resposta a incidentes. Usado para verificar se o ataque deixou artefatos detectáveis no endpoint.

**Lab:** Lab controlado simulando persistência + detecção — regra escrita antes de executar. Usa Atomic Red Team para validar cada TTP.
**Projeto:** Documentação do mecanismo de persistência + regra de detecção criada previamente. Entra no LOG_DE_DETECCAO.md.
**Checkpoint:** [ ] Cria regra antes de ver o ataque rodar. [ ] Pelo menos 8 das 11 técnicas têm regra própria no LOG.

---

## Sprint 6 (Semanas 79–80) — Evasão de Defesas

**Objetivo:** Entender bypass de WAF/AV/EDR para saber detectar isso depois.
**Teoria:** Técnicas de ofuscação, bypass básico de assinatura.
**Lab:** Tentar contornar uma regra de WAF/SIEM que você mesmo configurou.
**Projeto:** Relatório: "Como eu burlei minha própria defesa, e como vou corrigir."
**Checkpoint:** [ ] Ajusta a própria regra de detecção depois de burlá-la.

---

## Sprint 7 (Semanas 81–82) — Threat Intelligence e MITRE ATT&CK

**Objetivo:** Falar a língua universal de Threat Intel.
**Teoria:** TTPs, IOCs, diferença entre inteligência estratégica e operacional.
**Lab:** Mapear todos os ataques dos Blocos 1–3 no MITRE ATT&CK Navigator. Cruzar com o LOG_DE_DETECCAO.md.
**Projeto:** Heatmap do ATT&CK Navigator cobrindo a jornada completa.
**Checkpoint:** [ ] Mapeia ataque novo no Navigator sem consultar exemplo. [ ] Lista exatamente quais técnicas do catálogo ainda faltam.

---

## ⭐ Sprint 8 (Semanas 83–84) — Presença Pública, CTF Cronometrado e Simulação de Entrevista

**Objetivo:** Sair do anonimato técnico, treinar pressão de tempo real, e não travar em entrevista.

**Lab — CTF:** 1 CTF cronometrado real (HackTheBox temporada ou competição aberta).

**Lab — Entrevista:** Escrever respostas completas para estas 10 perguntas e revisar em voz alta:
1. Me explica o que é Purple Team e como funciona na prática
2. Como você escreveria uma regra de detecção para Kerberoasting?
3. Qual a diferença entre Sigma, KQL, SPL e EQL?
4. Me descreve um incidente que você investigou do início ao fim
5. O que é um Golden Ticket e como você detectaria?
6. Como você priorizaria alertas num SOC com alto volume de ruído?
7. O que é DCSync e por que é perigoso?
8. Como você diferencia um falso positivo de um verdadeiro positivo?
9. Me explica o fluxo Kerberos em detalhes
10. O que você faria nas primeiras 2 horas de um incidente confirmado?

**Projeto:**
- 1 post técnico público (LinkedIn ou blog)
- Resultado documentado do CTF
- Documento com as 10 respostas + auto-avaliação do que não conseguiu responder com clareza

**Checkpoint:** [ ] Post técnico publicado. [ ] 1 CTF com tempo limite real completado. [ ] Responde as 10 perguntas sem consultar nada.

---

## ⭐ Sprint 9 (Semanas 85) — Simulação Purple Team Completa [PROJETO FINAL]

**Objetivo:** O projeto mestre do protocolo inteiro.
**Lab:** HackTheBox laboratório avançado (Zephyr recomendado) ou ambiente próprio com AD completo.
**Projeto:** Ciclo Purple Team completo: **previsão de detecção → Red ataca → Blue detecta → IR responde → hardening aplicado → relatório final.**
**Checkpoint:** [ ] Projeto completo, sozinho, do início ao fim, sem write-up de apoio. [ ] LOG_DE_DETECCAO.md cobre as 11 técnicas, todas com taxa e nota de FP.

**Gate de saída do Bloco 3 — GATE FINAL:**
- [ ] Simulação Purple Team completa documentada
- [ ] 11 técnicas do Catálogo cobertas no LOG_DE_DETECCAO.md, taxa mínimo 80% e nota de FP
- [ ] Pelo menos 4 regras traduzidas entre Sigma, KQL, SPL e EQL
- [ ] Portfólio público no GitHub com toda a jornada
- [ ] Pelo menos 1 certificação tirada (eJPT ou BTL1)
- [ ] Heatmap do ATT&CK Navigator completo
- [ ] 1 post técnico público + 1 CTF cronometrado completados
- [ ] 10 perguntas de entrevista respondidas com clareza, documentadas
- [ ] Decisão documentada sobre RE
- [ ] Explica qualquer parte do protocolo sem consultar nada

---

## 🎓 CERTIFICAÇÕES

| Certificação | Quando tirar | Custo aprox. |
|---|---|---|
| eJPT | Final do Bloco 1 | ~$200 |
| BTL1 | Final do Bloco 2 | ~$400 |
| CompTIA Security+ | Durante o Bloco 3 | ~$400 |
| SC-200 | Após Sprint KQL/SPL (Bloco 2), se trilha Microsoft fez sentido | ~$165 |
| **CPTS (HackTheBox)** | Pós-protocolo — alternativa ao OSCP se orçamento for limitado | ~$490 |
| OSCP | Pós-protocolo — meta de longo prazo | ~$1.600+ |

> CEH e CISSP fora: CISSP exige experiência que você ainda não tem; CEH tem reputação fraca frente ao eJPT/OSCP no mercado prático.

---

## 📚 FONTES POR BLOCO

| Fonte | Bloco | Tipo |
|---|---|---|
| Curso em Vídeo / Hashtag Programação | 1 | Gratuito, PT |
| SecDay Academy | 1 | Gratuito, PT |
| Cisco Networking Academy | 1–2 | Gratuito |
| TryHackMe | 1–3 | Gratuito (parcial) / Pago |
| PortSwigger Academy | 1 | Gratuito 🇺🇸 |
| HackTheBox | 1, 3 | Gratuito (parcial) / Pago 🇺🇸 |
| Documentação Wazuh | 2 | Gratuito 🇺🇸 |
| Sigma Rules (repositório público) | 2–3 | Gratuito 🇺🇸 |
| Microsoft Sentinel/Defender Trial + KQL docs | 2–3 | Gratuito (trial) 🇺🇸 |
| Splunk Free Trial + docs.splunk.com | 2–3 | Gratuito (trial) 🇺🇸 |
| Repositórios públicos KQL/SPL hunting queries | 2–3 | Gratuito 🇺🇸 |
| Elastic Security Trial | 2–3 | Gratuito (trial) 🇺🇸 |
| AWS Free Tier / Azure Student | 2 | Gratuito (com limites) 🇺🇸 |
| MITRE ATT&CK | 2–3 | Gratuito 🇺🇸 |
| LinkedIn / blog pessoal | 2–3 | Gratuito |

*🇺🇸 = conteúdo majoritariamente em inglês*

---

## 📈 VISÃO PÓS-PROTOCOLO

```
Fim do protocolo (~19 meses)  →  Purple Team júnior com portfólio de detecção
                                   projetada em Sigma, KQL, SPL e EQL, cloud
                                   detection documentado, 1+ certificação,
                                   presença pública ativa, entrevista preparada

Ano 2–3                        →  Especialização: Detection Engineering, Cloud
                                   Security, Threat Hunting, ou Red Team puro

Ano 3–5                        →  Referência técnica na área escolhida

Ano 5+                         →  Você define o próximo mapa
```

---

## 📋 O QUE MUDOU DA v7 PARA A v8

| O que mudou | Detalhe |
|---|---|
| Grade diária integrada ao roadmap | Cada sprint agora tem sua grade diária embutida logo abaixo do conteúdo |
| Regras fixas da grade no topo | Seção dedicada antes dos blocos para não repetir em todo sprint |
| Blocos 2 e 3 com grade temática | Estrutura de dias por bloco — conteúdo detalhado por sprint quando necessário |
| Horário de férias explícito | 14:30–18:50 indicado na grade dos Sprints 1 e 2 |
| **[CORREÇÃO]** Inglês Técnico Bloco 2 corrigido | Semanas 25–58 → 25–61 (alinhado com fim real do Bloco 2) |
| **[CORREÇÃO]** Inglês Técnico Bloco 3 corrigido | Semanas 59–82 → 62–85 (alinhado com início e fim real do Bloco 3) |
| **[CORREÇÃO]** Progressão de linguagens C corrigida | Semanas 59–63 → 70–71 (alinhado com Sprint 4 do Bloco 3) |
| **[CORREÇÃO]** Progressão de linguagens Assembly corrigida | Semanas 64–67 → 72–73 (alinhado com Sprint 4 do Bloco 3) |