# 🏆 ROADMAP PURPLE TEAM — v8
### Fusão Profissional · ~19 Meses · Joao · Palmas, TO
> "Operar a detecção que alguém te deu é Tier 1. Projetar a detecção que ninguém te deu, em qualquer stack, contra um padrão mínimo conhecido, é Purple Team."

---

## ⚠️ AVISOS FIXOS — LÊ ANTES DE COMEÇAR

### 🔴 Aviso de Inglês
Fontes majoritariamente em inglês. Pontos críticos marcados com **[🇺🇸 INGLÊS NECESSÁRIO]**. Anki com 15 palavras técnicas por dia desde agora.

### 🔴 Aviso de Execução
Nenhuma edição no roadmap enquanto estiver dentro de um bloco. Edições só na semana de descanso entre blocos.

### 🔴 Aviso de Atraso
Se um sprint atrasar mais de 2 semanas: não compensa. Entrega o que tem, documenta no LOG_DE_GUERRA, avança.

### 🔴 Aviso de Visibilidade
1 post técnico por mês no LinkedIn a partir do Bloco 2. Não é opcional.

---

## 📐 ESTRUTURA GERAL

```
BLOCO 1  →  Semanas 1–24    (~6 meses)     FUNDAÇÃO + RED TEAM
BLOCO 2  →  Semanas 25–61   (~9 meses)     BLUE TEAM
BLOCO 3  →  Semanas 62–85   (~6 meses)     ELITE / PURPLE TEAM

TOTAL: ~85 semanas ≈ 19,5 meses
```

> **A grade de horários (quando estudar cada dia) não fica mais neste documento.** Ela vive em `ROTINA.md`, separada, editável a qualquer momento sem mexer aqui.

---

## 🌍 CAMADAS TRANSVERSAIS

### Inglês Técnico
| Período | O que praticar |
|---|---|
| Semanas 1–8 | docs.python.org |
| Semanas 9–24 | Man pages do Nmap, docs do Wireshark |
| Semanas 25–61 | Documentação Wazuh, KQL docs, MITRE ATT&CK |
| Semanas 62–85 | White papers de Purple Team, Detection Engineering |

### Presença Pública — a partir do Bloco 2
1 post técnico por mês no LinkedIn, sem exceção.

### Dia de Quebra — 1x por mês
Quebre o ambiente de propósito (VM, venv, dependência) e restaure sem ajuda.

### Código de Conduta do Operador
1. Regra dos 15 min — travou? Pesquisa 15 min. Não resolveu? Pergunta.
2. LOG_DE_GUERRA.md — todo erro resolvido vira entrada.
3. Ambiente impecável — código limpo, comentado, funcional.
4. Automação sempre — fez manual 2x? Na 3ª, vira script.
5. Git é sagrado — todo arquivo vai pro GitHub no mesmo dia.

### Progressão de Linguagens
```
Semana 1        →  Python
Semanas 9–24    →  Bash + SQL
Semanas 25–61   →  PowerShell + KQL + SPL (Splunk)
Semanas 70–71   →  C básico
Semanas 72–73   →  Assembly x86/x64 + Ghidra
```

### Regra de Produção Contínua (a partir do Bloco 2 Sprint 5)
1 regra própria (Sigma, KQL, SPL ou EQL) + 1 entrada no LOG_DE_DETECCAO.md por técnica ATT&CK estudada.

### Regra de Produção de Código (a partir do Bloco 2 Sprint 1)
Mínimo 1 script próprio entregue e commitado por sprint.

### Regra de Qualidade de Detecção
Toda entrada no LOG_DE_DETECCAO.md precisa de: taxa de detecção em teste (mínimo 80%) + nota de falso positivo.

### Catálogo de Técnicas Obrigatórias
Mínimo: 11 técnicas. Meta recomendada: 20+.

**11 obrigatórias:** T1059.001, T1047, T1547.001, T1053.005, T1003.001, T1558.003, T1021.002, T1071.001, T1105, T1078, T1041

**9 recomendadas:** T1003.006, T1550.002, T1558.001, T1558.002, T1021.001, T1569.002, T1059.001 (Empire), T1574.001, T1543.003

### Aviso de Ritmo
Após cada bloco: 1 semana de descanso ativo (revisar LOG, organizar GitHub, planejar próximo bloco).

---

# 🧱 BLOCO 1 — FUNDAÇÃO + RED TEAM (Semanas 1–24)

## Sprint 1 (Semanas 1–4) — Linux + Python Básico
**Objetivos:** Terminal sem mouse. Python com lógica real (variáveis, condicionais, loops, funções).
**Cursos:** Curso em Vídeo / Hashtag Programação, SecDay Academy.
**Labs:** Zorin OS como ambiente principal, sem GUI quando possível.
**Projeto:** `firewall_logic.py`.
**Entrega:** GitHub commitado. Checkpoint: navega no terminal sem consultar nada; escreve função Python do zero.

## Sprint 2 (Semanas 5–8) — Python Aplicado + Git
**Objetivos:** Módulos Python (socket, os, subprocess), Git workflow.
**Cursos:** docs.python.org como referência principal a partir daqui. [🇺🇸]
**Projeto:** Port scanner funcional.
**Entrega:** Repositório organizado, README, commits diários. Checkpoint: explica cada linha do port scanner.

## Sprint 3 (Semanas 9–14) — Redes Completas
**Objetivos:** OSI/TCP-IP, protocolos (TCP, UDP, DNS, HTTP, ARP), subnetting.
**Cursos:** Cisco Networking Academy, Bóson Treinamentos.
**Labs:** Nmap contra VMs próprias, Wireshark capturando tráfego real. [🇺🇸]
**Projeto:** Calculadora de subnet em Python + documentação de 5 scans Nmap analisados.
**Entrega:** Checkpoint: OSI de cabeça; identifica protocolo num pcap sem ajuda.

## Sprint 4 (Semanas 15–18) — Fundamentos Web
**Objetivos:** HTTP/HTTPS, cookies, sessões, OWASP Top 10.
**Labs:** PortSwigger Academy — SQLi, XSS, IDOR. [🇺🇸]
**Projeto:** Relatório de 3 vulnerabilidades exploradas, causa raiz e mitigação.
**Entrega:** Checkpoint: OWASP Top 10 de cabeça; Burp Suite intercepta e modifica requisição.

## Sprint 5 (Semanas 19–22) — Reconhecimento Ofensivo
**Objetivos:** PTES, reconhecimento passivo e ativo, OSINT básico.
**Cursos:** Solyd – Introdução ao Pentest.
**Ferramentas:** Shodan, theHarvester, crt.sh.
**Labs:** TryHackMe — 2 máquinas completas (1 Linux, 1 Windows).
**Projeto:** 2 write-ups completos com metodologia, ferramentas e lições.
**Entrega:** Checkpoint: diferencia recon passivo/ativo; write-up publicado.

## Sprint 6 (Semanas 23–24) — Primeiro Pentest Real
**Objetivos:** Estrutura de relatório de pentest profissional.
**Labs:** HackTheBox — 1 máquina introdutória completa.
**Projeto:** Relatório de Pentest em PDF, estrutura profissional.
**Entrega:** Checkpoint: relatório com 3+ findings (evidência, impacto, recomendação).

**Gate de saída do Bloco 1:**
- 24 entradas no LOG_DE_GUERRA (mínimo)
- Relatório de Pentest formal no portfólio
- GitHub organizado: scripts, write-ups, relatório, README
- Explica metodologia de ataque sem consultar nada
- Port scanner e firewall_logic.py documentados e commitados

---

# 🛡️ BLOCO 2 — BLUE TEAM (Semanas 25–61)

> A partir daqui: 1 post técnico por mês no LinkedIn.

## Sprint 1 (Semanas 25–26) — Hardening Linux
**Objetivos:** CIS Benchmarks básico, menor privilégio, hardening de SSH.
**Projeto:** Checklist de hardening + script de auditoria em Python.
**Entrega:** Checkpoint: VM resiste aos exploits usados antes.

## Sprint 2 (Semanas 27–28) — Hardening Windows
**Objetivos:** Group Policy básico, desativação de serviços desnecessários.
**Projeto:** Documentação antes/depois do hardening.
**Entrega:** Checkpoint: explica 3 mudanças que fecharam vetores de ataque.

## Sprint 3 (Semanas 29–30) — Análise de Logs
**Objetivos:** Logs do /var/log, Windows Event Viewer, estrutura de log.
**Labs:** TryHackMe — "Intro to Logs".
**Projeto:** Analisar log de ataque simulado e identificar a intrusão.
**Entrega:** Checkpoint: identifica ataque num log sem dica.

## Sprint 4 (Semanas 31–34) — SIEM com Wazuh
**Objetivos:** Arquitetura de SIEM, regras de detecção, alertas. [🇺🇸]
**Labs:** Instalar Wazuh, conectar como agente na VM atacada no Bloco 1.
> Regra: se após 2 semanas o Wazuh não gerar alertas funcionais, troca temporariamente pra Security Onion.
**Projeto:** SIEM detectando ao vivo os ataques do Bloco 1.
**Entrega:** Checkpoint: SIEM gera alerta real para ataque replicado.

## Sprint 4.5 (Semana 35) — Sysmon
**Objetivos:** Event IDs principais (1, 3, 7, 10, 11, 13). [🇺🇸]
**Labs:** Instalar Sysmon (config SwiftOnSecurity), replicar 2 ataques e comparar nativo vs Sysmon.
**Projeto:** Documento comparativo.
**Entrega:** Checkpoint: filtra Event ID 1/10 no Wazuh e identifica processo suspeito.

## Sprint 5 (Semanas 36–37) — Detection Engineering às Escuras
**Objetivos:** Estrutura de regra Sigma (sintaxe YAML antes do exercício), como traduzir TTP em detecção sem ter simulado antes.
**Labs:** Escolher 3 técnicas nunca simuladas, escrever regra antes de atacar, depois testar.
**Projeto:** 3 regras + resultado. Abre LOG_DE_DETECCAO.md.
**Entrega:** Checkpoint: 1 das 3 detecta sem ajuste; taxa e FP documentados.

## Sprint 5.5 (Semana 38) — Telemetria → Hipótese → Detecção
**Objetivos:** Raciocinar a partir de anomalia, não de TTP conhecido.
**Labs:** Logs do Sysmon/Bloco 1 sem saber qual ataque foi — anomalia → hipótese → confirmação.
**Projeto:** 2 ciclos documentados no LOG_DE_DETECCAO.md.
**Entrega:** Checkpoint: identifica 1 técnica partindo de anomalia, sem saber de antemão.

## Sprint 6 (Semanas 39–41) — KQL e Threat Hunting (Sentinel/Defender)
**Objetivos:** Sintaxe KQL, tabelas Log Analytics. [🇺🇸]
**Labs:** Trial Sentinel/Defender, reescrever 2 regras Sigma em KQL, 1 hunting query.
**Projeto:** Comparativo Sigma vs KQL.
**Entrega:** Checkpoint: query KQL de hunting do zero, sem copiar exemplo.

## Sprint 6.5 (Semana 42) — Splunk
**Objetivos:** Arquitetura básica, SPL básico. [🇺🇸]
**Labs:** Splunk Free Trial, ingerir logs próprios, reescrever 1 regra KQL em SPL.
**Projeto:** Terceira coluna no documento do Sprint 6 (Sigma | KQL | SPL).
**Entrega:** Checkpoint: 1 regra funcional em SPL.

## Sprint 7 (Semana 43) — Elastic Security
**Objetivos:** Detection rule, EQL.
**Labs:** Trial Elastic, traduzir 1 regra pra EQL.
**Projeto:** Comparativo final Sigma | KQL | SPL | EQL.
**Entrega:** Checkpoint: 1 regra funcional em EQL.

> **Prioridade se o tempo apertar: aprofunda Splunk e Elastic antes de Sentinel.**

## Sprint 8 (Semanas 44–45) — Firewalls na Prática
**Objetivos:** UFW e Iptables, regras de entrada/saída, NAT defensivo.
**Projeto:** Script que audita regras de firewall ativas.
**Entrega:** Checkpoint: Nmap retorna portas filtradas, não abertas.

## Sprint 9 (Semanas 46–48) — Resposta a Incidentes
**Objetivos:** Ciclo de IR completo (Preparação → Identificação → Contenção → Erradicação → Recuperação → Lições Aprendidas).
**Labs:** TryHackMe — IR introdutória.
**Projeto:** Plano de resposta escrito + simulação completa de incidente.
**Entrega:** Checkpoint: cita as 6 fases com exemplo prático de cada.

## Sprint 10 (Semanas 49–50) — Forense Digital Básico
**Objetivos:** Artefatos de memória e disco, cadeia de custódia.
**Labs:** TryHackMe — forense introdutória.
**Projeto:** Relatório forense de máquina comprometida (lab controlado).
**Entrega:** Checkpoint: identifica 2 artefatos de comprometimento.

## Sprint 11 (Semanas 51–52) — IAM, MFA, SSO
**Objetivos:** Autenticação vs autorização, MFA (TOTP, FIDO2), SSO, Microsoft Entra ID, Zero Trust.
**Projeto:** Documento sobre limites do MFA (ex: MFA fatigue).
**Entrega:** Checkpoint: explica autenticação vs autorização sem hesitar.

## Sprint 12 (Semanas 53–57) — Cloud Security: Proteção + Detecção
**Objetivos:** IAM em nuvem, misconfigurações comuns, CloudTrail, Azure Activity Logs, GuardDuty, Defender for Cloud. [🇺🇸]
**Ferramentas:** Prowler ou ScoutSuite.
**Labs:** AWS Free Tier + Azure Student, gerar evento suspeito e encontrá-lo via ferramentas nativas.
> Escolher 1 cloud principal (AWS ou Azure); a outra fica complementar.
**Projeto:** Comparativo de detecção cloud AWS vs Azure.
**Entrega:** Checkpoint: identifica misconfiguration clássica; encontra evento suspeito simulado.

## Sprint 13 (Semanas 58–59) — Contêineres e DevSecOps
**Objetivos:** Superfície de ataque de containers, scanning de imagem, CI/CD seguro.
**Ferramentas:** Trivy.
**Projeto:** Dockerfile hardenizado + documentação.
**Entrega:** Checkpoint: explica por que rodar container como root é perigoso.

## Sprint 14 (Semanas 60–61) — NIST CSF — Estudo de Caso Real
**Objetivos:** As 6 funções do NIST CSF 2.0.
**Labs:** Mapear incidente público documentado contra o framework.
**Projeto:** Relatório "onde o NIST CSF teria evitado este incidente" + mapear projetos próprios contra o framework.
**Entrega:** Checkpoint: cita as 6 funções de cabeça e aplica num caso real.

**Gate de saída do Bloco 2:**
- SIEM detectando ao vivo ataques do Bloco 1 (Wazuh)
- 3 regras "no escuro" com taxa e FP documentados
- 2+ regras traduzidas entre Sigma/KQL/SPL/EQL
- LOG_DE_DETECCAO.md ativo desde o Sprint 5, taxa e FP por técnica
- Hardening documentado (Linux + Windows) antes/depois
- Simulação completa de IR + relatório forense no portfólio
- Lab de Cloud documentado (AWS e Azure)
- Estudo de caso NIST CSF
- 14+ scripts próprios commitados
- 6+ posts técnicos no LinkedIn

---

# 🎯 BLOCO 3 — ELITE / PURPLE TEAM REAL (Semanas 62–85)

## Sprint 1 (Semanas 62–64) — Active Directory: Fundamentos e Ataque
**Objetivos:** Estrutura de domínio, Trusts, Forests, Kerberos em detalhe (AS-REQ, AS-REP, TGS-REQ, TGS-REP).
**Labs:** TryHackMe AD Basics + HackTheBox AD introdutória. Não avança pra BloodHound sem explicar Kerberos de cabeça. [🇺🇸]
**Projeto:** Write-up do primeiro comprometimento de domínio com diagrama Kerberos anotado.
**Entrega:** Checkpoint: explica o fluxo Kerberos de cabeça, sem consultar.

## Sprint 2 (Semanas 65–67) — AD: BloodHound, Mimikatz, Impacket
**Objetivos:** Movimentação lateral, delegação, persistência, Pass-the-Hash, DCSync, Golden Ticket.
**Ferramentas:** BloodHound, Mimikatz, Impacket.
**Labs:** Lab de AD com BloodHound mapeando caminho completo; 2 ataques de credencial.
**Projeto:** Grafo BloodHound documentado + write-up de ataque de credencial.
**Entrega:** Checkpoint: identifica caminho de privesc via BloodHound; executa DCSync ou PtH em lab.

## Sprint 3 (Semanas 68–69) — AD: Defesa
**Objetivos:** Detecção de Kerberoasting, DCSync, PtH; hardening de GPO; Tiering Model; Protected Users.
**Labs:** Escrever regra antes de reexecutar cada ataque do Sprint 2, validar no SIEM.
**Projeto:** Documentação Purple Team completa (previsão → ataque → detecção → resposta → hardening) pra 2+ ataques. Entra no LOG_DE_DETECCAO.md.
**Entrega:** Checkpoint: SIEM detecta ataque de AD replicado ao vivo.

## Sprint 4 (Semanas 70–73) — Engenharia Reversa: da Base ao Binário
**Objetivos:** C básico (semanas 70-71), Assembly x86/x64 básico (semanas 72-73).
**Cursos:** Mente Binária, LiveOverflow (apoio).
**Labs:** Ghidra num crackme introdutório — só depois de compilar 3+ programas em C.
**Projeto:** Relatório de RE de crackme iniciante.
**Entrega:** Checkpoint: identifica função principal no Ghidra e explica o assembly correspondente.
> ⚠️ **Sprint de maior risco de atraso do protocolo inteiro.** Decisão ao final: continuar RE pós-protocolo ou foi suficiente — documentar, sem meio-termo.

## Sprint 5 (Semanas 74–78) — Pós-Exploração, Persistência e Fechamento do Catálogo
**Objetivos:** Persistência, exfiltração, C2 básico.
**Ferramentas:** Atomic Red Team, CALDERA, Velociraptor.
**Labs:** Lab controlado simulando persistência + detecção, regra escrita antes de executar.
**Projeto:** Documentação do mecanismo de persistência + regra. Entra no LOG_DE_DETECCAO.md.
**Entrega:** Checkpoint: 8 das 11 técnicas obrigatórias com regra própria no LOG.

## Sprint 6 (Semanas 79–80) — Evasão de Defesas
**Objetivos:** Ofuscação, bypass básico de assinatura.
**Labs:** Tentar contornar regra própria de WAF/SIEM.
**Projeto:** Relatório "como eu burlei minha própria defesa, e como vou corrigir."
**Entrega:** Checkpoint: ajusta a própria regra depois de burlá-la.

## Sprint 7 (Semanas 81–82) — Threat Intelligence e MITRE ATT&CK
**Objetivos:** TTPs, IOCs, inteligência estratégica vs operacional, STIX/TAXII/MISP/OpenCTI (conceitual).
**Labs:** Mapear todos os ataques dos Blocos 1–3 no ATT&CK Navigator, cruzar com LOG_DE_DETECCAO.md.
**Projeto:** Heatmap do Navigator cobrindo a jornada completa.
**Entrega:** Checkpoint: mapeia ataque novo sem consultar exemplo.

## Sprint 8 (Semanas 83–84) — Presença Pública, CTF Cronometrado, Entrevista
**Labs:** 1 CTF cronometrado real. Responder por escrito as 10 perguntas de entrevista padrão da área.
**Projeto:** 1 post técnico público, resultado do CTF documentado, respostas + auto-avaliação.
**Entrega:** Checkpoint: post publicado; CTF completado; 10 perguntas respondidas sem consultar.

## Sprint 9 (Semana 85) — Simulação Purple Team Completa [PROJETO FINAL]
**Labs:** HackTheBox avançado (Zephyr recomendado) ou ambiente próprio com AD completo.
**Projeto:** Ciclo completo — previsão → Red ataca → Blue detecta → IR responde → hardening → relatório final.
**Entrega:** Checkpoint: projeto completo, sozinho, sem write-up de apoio. LOG_DE_DETECCAO.md cobre as 11 técnicas com taxa e FP.

**Gate de saída do Bloco 3 — GATE FINAL:**
- Simulação Purple Team completa documentada
- 11 técnicas cobertas no LOG, taxa mínimo 80% e nota de FP
- 4+ regras traduzidas entre Sigma/KQL/SPL/EQL
- Portfólio público no GitHub com toda a jornada
- 1+ certificação tirada (eJPT ou BTL1)
- Heatmap ATT&CK Navigator completo
- 1 post técnico + 1 CTF cronometrado completados
- 10 perguntas de entrevista documentadas
- Decisão documentada sobre RE
- Explica qualquer parte do protocolo sem consultar nada

---

## 🎓 CERTIFICAÇÕES

| Certificação | Quando tirar | Custo aprox. |
|---|---|---|
| eJPT | Final do Bloco 1 | ~$200 |
| BTL1 | Final do Bloco 2 | ~$400 |
| CPTA v2 (CyberWarFare Labs) | Alternativa entre BTL1 e OSCP | — |
| CompTIA Security+ | Durante o Bloco 3 | ~$400 |
| SC-200 | Após Sprint KQL/SPL, se trilha Microsoft fizer sentido | ~$165 |
| CPTS (HackTheBox) | Pós-protocolo | ~$490 |
| OSCP | Pós-protocolo, meta de longo prazo | ~$1.600+ |

> CEH e CISSP fora: CISSP exige experiência ainda não acumulada; CEH tem reputação fraca frente ao eJPT/OSCP.
> ⚠️ Resolver logística de conta AWS/Azure e inscrição de certificação com um responsável — algumas exigem maioridade ou consentimento.

---

## 📈 VISÃO PÓS-PROTOCOLO

```
Fim do protocolo (~19 meses)  →  Purple Team júnior com portfólio de detecção
                                   em Sigma, KQL, SPL e EQL, cloud detection
                                   documentado, 1+ certificação, presença
                                   pública ativa, entrevista preparada

Ano 2–3                        →  Especialização: Windows Internals aplicado
                                   a dev ofensivo, Exploit Development,
                                   Shellcode, Loaders, Win32 API avançada,
                                   pesquisa de vulnerabilidades, ou
                                   Detection Engineering / Cloud Security /
                                   Threat Hunting

Ano 3–5                        →  Referência técnica na área escolhida
```