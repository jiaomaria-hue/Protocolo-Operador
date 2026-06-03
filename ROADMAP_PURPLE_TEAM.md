# 🗺️ MAPA DE ELITE — PROTOCOLO DE 18 MESES v4
### Purple Team / Security Engineering · João · Palmas, TO
> "A perfeição na segurança cibernética não é um desenho bonitinho. É um ciclo de guerra infinito."

---

## ⚡ MISSÃO DE ATIVAÇÃO — CONCLUÍDA (28/05/2026)

- [x] Abrir o terminal e criar olamundo.py
- [x] Criar LOG_DE_GUERRA.md com entrada: 28/05/2026 — Iniciado Protocolo de Elite
- [x] Criar repositório Protocolo-Operador no GitHub e fazer primeiro commit
- [x] Assistir Aula 1 da SecDay Academy no YouTube

---

## 🖥️ HOME LAB — MONTAR ANTES DE COMEÇAR

> Sem isso o roadmap inteiro é teoria. Monte antes de entrar na Fase 1.

**Configuração mínima no VirtualBox — rede interna isolada**

| VM | Sistema | Função |
|---|---|---|
| VM 1 | Kali Linux | Máquina de ataque |
| VM 2 | Windows 10 | Endpoint alvo |
| VM 3 | Windows Server 2019 | Domain Controller (AD) |

**Como configurar**
- Todas as VMs na mesma rede interna (`intnet`) no VirtualBox — elas se enxergam, sem acesso à internet da máquina alvo
- Windows Server 2019: promover a Domain Controller, criar domínio (ex: `lab.local`)
- Windows 10: ingressar no domínio
- Kali: deixar na rede interna + NAT para ter internet quando precisar

> Este lab é o campo de batalha de todas as fases. Você vai atacar, defender e monitorar nele.

---

## 📚 FONTES DE ESTUDO

| Fonte | Como usar | Fase |
|---|---|---|
| SecDay Academy — 16 aulas (YouTube) | Fundação Linux e Redes | Fase 1–2 |
| Cisco Networking Academy | Redes + Intro Cibersegurança (certificado gratuito) | Fase 1–2 |
| Microsoft Learn | Active Directory, GPO, PowerShell | Fase 1+ |
| TCM Security — Practical Ethical Hacking | AD attacks, metodologia pentest completa | Fase 3–4 |
| TCM Security — Practical Active Directory (gratuito YouTube) | AD básico antes do curso pago | Fase 1–2 |
| TryHackMe — Jr Pentester | Campo de batalha prático | Fase 3+ |
| HackTheBox | Prática avançada, ambientes reais | Final Fase 3+ |

> TikTok (studywithme cibersegurança): radar de conceitos e motivação. Não é fonte técnica.

---

## 💻 PROGRESSÃO DE LINGUAGENS

```
Fase 1      →  Python           (automação, scripts, lógica de segurança)
Fase 1–2    →  Bash             (terminal Linux — começa aqui, não depois)
Fase 3      →  PowerShell ofensivo   (AD attacks, living off the land)
Fase 3      →  SQL              (entra como tópico de OWASP — 3 dias de prática, não uma fase)
Fase 4      →  C básico         (leitura de exploits, ponteiros, memória — não desenvolvimento)
Fase 5+     →  Assembly x86/x64 (só se especializar em Reverse Engineering)
```

> PowerShell básico começa na Fase 1 como ferramenta de administração Windows.
> PowerShell ofensivo entra na Fase 3 — são coisas diferentes e o roadmap trata assim.
> Ruby foi removido. Você usa Metasploit, não reescreve ele.

---

## FASE 1 — DOMÍNIO DA MÁQUINA

> Onde você sai de usuário para Operador. Linux E Windows — os dois ambientes de guerra.
> Esta fase tem dois blocos internos. Complete o Bloco A antes de começar o Bloco B.

---

### BLOCO A — Linux e Python `Checkpoint: semanas 1–4`

**O que aprender**
- Terminal completo: permissões (chmod/chown), usuários, processos, systemd, cron
- Vim básico — servidores sem GUI não têm VS Code
- Bash scripting: loops, condicionais, pipes, redirecionamento
- Git + GitHub: commits descritivos desde o primeiro dia
- Python puro: lógica, funções, arquivos, tratamento de erros, controle de fluxo

**O que entregar**
- Scripts de gestão de sistema sem interface gráfica
- Projeto `firewall_logic.py` rodando no terminal
- Repositório Protocolo-Operador no GitHub com commits regulares

**Checkpoint A — você passa quando:**
> Consegue navegar o sistema de arquivos, criar usuários, editar permissões, escrever um script Bash que automatiza uma tarefa real e versionar tudo no GitHub sem consultar tutorial.

---

### BLOCO B — Windows, AD e Monitoramento `Checkpoint: semanas 5–10`

**O que aprender**

*Windows e Active Directory*
- Navegação CLI: cmd e PowerShell básico (administração, não ofensiva)
- Active Directory: estrutura, objetos, autenticação NTLM e Kerberos — no lab real
- Group Policy (GPO): criar e aplicar políticas no Domain Controller do lab
- Ingressar a VM Windows 10 no domínio e validar

*Monitoramento e logs*
- Windows Event Logs: Event IDs críticos — 4624, 4625, 4688, 4720, 7045
- Sysmon: instalar na VM Windows 10, configurar com SwiftOnSecurity config, entender o que cada regra captura

*Fundamentos de segurança*
- Tríade CIA — Confidencialidade, Integridade, Disponibilidade
- Criptografia básica — SHA, AES, RSA: o que são, como funcionam, onde falham

**Fontes do Bloco B**
- Microsoft Learn — Active Directory e Windows Server fundamentals
- TCM Security — Practical Active Directory (YouTube gratuito)
- SwiftOnSecurity/sysmon-config (GitHub) — config de Sysmon de referência

**O que entregar**
- Domain Controller funcional no VirtualBox com domínio `lab.local`
- Windows 10 ingressado no domínio
- Sysmon instalado e gerando logs na VM Windows
- Abrir o Event Viewer e identificar: login bem-sucedido, login falho, processo criado

**Checkpoint B — você passa quando:**
> Consegue abrir o Event Viewer, filtrar por Event ID 4625 e identificar uma tentativa de login falha no seu lab. Consegue explicar a diferença entre autenticação NTLM e Kerberos sem consultar anotação.

**📅 Rotina Semanal — Fase 1**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Linux / Bloco A | SecDay Academy + praticar comandos no terminal |
| Terça + Quinta | Windows / Bloco B | Microsoft Learn + configurar lab AD + Sysmon |
| Sexta | Python | Escrever scripts + push no GitHub + LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Revisar Event IDs e anotações ou descansar |

> TryHackMe ainda não. Sem AD funcional e Sysmon configurado, você vai travar em 60% das máquinas.

---

## FASE 2 — VIGILÂNCIA DA REDE `Marco: competência, não calendário`

> Entender como os dados se movem é entender o campo de batalha.

**O que aprender**
- Modelo OSI — 7 camadas com exemplo de ataque em cada camada
- TCP/IP, DNS, DHCP, HTTP/S, ARP, ICMP
- TCP Handshake vs UDP — diferença e implicações de segurança
- Subnetting e CIDR — MAC vs IP, endereçamento de redes
- VLANs e Tabelas de Roteamento básicas
- Ataques wireless: WPA2 handshake capture, deauth, evil twin — conceito e lab
- NIST CSF e ISO 27001 — linguagem corporativa que aparece em toda entrevista
- IAM, MFA, SSO — fundamentos de identidade e acesso

**Ferramentas**
- Wireshark — captura e análise de tráfego real no lab
- Nmap — reconhecimento de redes, OS fingerprinting, scripts NSE
- Netcat — shells, transferência de arquivos, banner grabbing
- Scapy — manipulação de pacotes via Python
- Aircrack-ng — ataques wireless no lab (adaptador wireless necessário)

> Se não tiver adaptador wireless compatível: estude o conceito via teoria e volte ao lab quando tiver o hardware. Chipsets Alfa AWUS036ACH funcionam no Kali sem configuração extra.

**Fontes desta fase**
- Cisco Networking Academy — cursos de redes
- SecDay Academy — automação com Python

**O que entregar**
- Port Scanner em Python com detecção de serviços rodando em portas
- Capturas de tráfego reais documentadas no LOG_DE_GUERRA.md
- Identificar no Wireshark: ARP poisoning, port scan, TCP handshake anômalo

**Marco de validação**
> Você mapeia o lab inteiro com Nmap, identifica todos os serviços em cada VM e consegue explicar cada pacote capturado no Wireshark. Se o Kali fizer um scan na rede, você vê no tráfego.

**📅 Rotina Semanal — Fase 2**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Cisco (redes) + anotar no VS Code |
| Terça + Quinta | Prática | Wireshark + Nmap no lab + scripts de rede em Python |
| Sexta | Consolidação | Push no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Revisar capturas de tráfego e anotações |

> Cada anomalia capturada no Wireshark vai pro LOG com explicação do que é e por que importa.

---

## FASE 3 — ARTE DA OFENSIVA — RED `Marco: competência, não calendário`

> Mentalidade de invasor. Se a máquina não cair, você não para.

**O que aprender**
- OWASP Top 10 — lab prático para cada vulnerabilidade (SQLi entra aqui, 3 dias de prática)
- Metodologia completa: Reconhecimento → Enumeração → Exploração → Pós-exploração → Relatório
- OSINT e Engenharia Social — coleta passiva e ativa
- C básico — leitura de código, ponteiros, gerenciamento de memória (não desenvolvimento)
- PowerShell ofensivo — living off the land, execução de payloads, bypass de políticas
- Como escrever Relatórios de Pentest profissionais

**Por que C entra aqui**
> Quando você analisar exploits e entender por que um payload funcionou, vai precisar ler o que acontece em baixo nível. Sem isso você usa ferramentas sem entender — e trava quando sair do script.

**Por que PowerShell ofensivo entra aqui**
> Você já tem o lab AD montado. Ataques reais em ambientes Windows usam PowerShell nativamente — é living off the land. Aprender isso junto com o Red Team é o momento certo.

**Ferramentas**
- Burp Suite — interceptação, repetição e fuzzing de requisições web
- Metasploit — framework de exploração (você usa, não lê o fonte)
- PowerView, BloodHound — enumeração de AD
- OSINT Framework, Maltego (básico)

**Plataformas**
- TryHackMe — caminho Jr Penetration Tester (do início ao fim)
- HackTheBox — pelo menos 5 máquinas Easy/Medium documentadas
- TCM Security — Practical Ethical Hacking (cobre AD attacks em profundidade)
- C básico: CS50x (Harvard, gratuito) — semanas 1 a 4. Alternativa: "The C Programming Language" — Kernighan e Ritchie, capítulos 1 a 5
- Quando travar: pesquise o write-up. É assim que profissionais aprendem.

**O que entregar**
- Caminho Jr Pentester do TryHackMe completo
- Write-ups com metodologia completa no GitHub
- Pelo menos 1 relatório de pentest formatado profissionalmente
- Ataque completo no lab AD: comprometer o Domain Controller a partir do Kali
- LOG_DE_GUERRA com raciocínio de cada invasão — não só o que funcionou

**Marco de validação**
> Você compromete uma máquina Easy do HackTheBox sem write-up e documenta metodicamente. Consegue comprometer o Domain Controller do seu lab e explicar cada passo — do reconhecimento ao DCSync.

**📅 Rotina Semanal — Fase 3**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | OWASP, exploits, CVEs, C básico, PowerShell ofensivo |
| Terça + Quinta | Prática | TryHackMe / HackTheBox + ataques no lab AD |
| Sexta | Consolidação | Push write-up no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Máquinas que não caíram + write-ups de referência |

> Se a máquina não cair na Terça, você volta pra ela na Quinta. Sem pular.
> **Ao final desta fase: fazer o eJPT.**

---

## FASE 4 — ARTE DA DEFESA — BLUE `Marco: competência, não calendário`

> Você só defende bem o que aprendeu a atacar.

**O que aprender**
- Hardening Linux e Windows com checklist documentado
- Windows Event Logs avançado + Sysmon — análise de tráfego anômalo real
- Wazuh: SIEM open source configurado para detectar os ataques da Fase 3
- Splunk: queries SPL básicas, dashboards, alertas
- UFW e Iptables — regras reais, não só conceito
- Resposta a Incidentes: playbooks, contenção, erradicação, recuperação
- Forense Digital básico: memória (Volatility), disco, artefatos
- Cloud Security (AWS/Azure): IAM, políticas, misconfigurações comuns
- Docker security básico

**Por que Wazuh + Sysmon juntos**
> O SIEM ingere o que o Sysmon captura. Se você não sabe o que o Sysmon registra, o SIEM é ruído. Configure os dois juntos — um sem o outro é metade do trabalho.

**Ferramentas**
- Wazuh — SIEM open source, detecção de intrusão
- Splunk — análise de logs em escala (free tier suficiente para labs)
- UFW / Iptables
- Volatility — análise de memória forense
- AWS Free Tier / Azure Student — primeiros labs em cloud

**O que entregar**
- Hardening completo de cada VM do lab atacada na Fase 3
- Wazuh detectando exatamente os ataques que você executou — Pass-the-Hash, Kerberoasting, DCSync
- Documentação de defesa como contrapartida de cada write-up de ataque
- Pelo menos 1 playbook de resposta a incidente escrito por você
- Relatório Purple Team de um ciclo completo no lab AD

**Marco de validação**
> Para cada ataque executado na Fase 3 contra o lab AD: você fecha a brecha, configura o Wazuh para alertar no mesmo vetor e escreve o playbook de resposta. Se o SIEM não alerta antes de você terminar o ataque, a defesa não está pronta.

**📅 Rotina Semanal — Fase 4**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Hardening, Sysmon avançado, Wazuh, cloud + anotar |
| Terça + Quinta | Prática | Configurar SIEM + hardening nas VMs + labs AWS |
| Sexta | Consolidação | Push documentação de defesa no GitHub + LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Testar se o SIEM detecta os ataques. Se não detecta, corrige. |

> Pega cada ataque da Fase 3 e fecha a brecha. Sem exceção.
> **Ao final desta fase: fazer o BTL1.**

---

## FASE 5 — OPERADOR DE ELITE `Marco: competência, não calendário`

> Purple Team completo: você ataca, detecta, responde e endurece. Em AD e em cloud.

**O que aprender**
- Active Directory avançado — Pass-the-Hash, Kerberoasting, DCSync, Golden Ticket: ataque E defesa
- MITRE ATT&CK Navigator — mapear seus próprios ataques contra a matrix
- Threat Intelligence — IOCs, TTPs, threat hunting básico
- Engenharia Reversa — Ghidra, análise estática de binários simples
- Assembly x86 básico — leitura, não escrita
- Cloud Security avançado — IAM profundo, políticas, arquitetura segura

**O que entregar**
- Portfólio público no GitHub com projetos de Purple Team organizados e documentados
- Write-ups completos com ciclo fechado: ataque → detecção → resposta → hardening → relatório
- LinkedIn técnico ativo — posts técnicos sobre o que você está aprendendo
- Pelo menos 3 ciclos Purple Team completos documentados publicamente

**Certificações — em ordem de prioridade**

| Cert | Por quê | Quando fazer |
|---|---|---|
| eJPT | Valida lado ofensivo, acessível, boa para portfólio | Final da Fase 3 |
| BTL1 | Valida lado defensivo, reconhecida BR + internacional | Final da Fase 4 |
| CompTIA Security+ | Reconhecimento corporativo, abre portas em empresas grandes | Durante a Fase 5 |
| OSCP | Meta pós-protocolo — o ouro do Red Team | Pós-18 meses |

**Marco de validação**
> Você executa um ciclo Purple Team completo em ambiente AD — compromete o DC, detecta no SIEM, responde com playbook, endurece e entrega um relatório que um SOC Manager lê e entende sem te perguntar nada.

**📅 Rotina Semanal — Fase 5**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | AD avançado, MITRE ATT&CK, Engenharia Reversa + anotações |
| Terça + Quinta | Prática | Simulações Purple Team no lab + automação + portfólio |
| Sexta | Consolidação | Push portfólio no GitHub + LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Certificações (eJPT / BTL1 / Security+) + LinkedIn |

> Ciclo completo todo projeto: ataque → detecção → resposta → hardening → relatório.

---

## 🛡️ CÓDIGO DE CONDUTA DO OPERADOR

1. **Regra dos 15 min** — Travou? Pesquise por 15 minutos. Não resolveu? Pergunta imediatamente.
2. **LOG_DE_GUERRA.md** — Todo erro resolvido entra no log: data, problema, tentativas, solução.
3. **Ambiente impecável** — Scripts limpos, comentados e funcionais. Código sujo é vetor de falha.
4. **Automação sempre** — Fez manualmente duas vezes? Na terceira, cria o script Python.
5. **Git é sagrado** — Todo script vai pro GitHub com commit descritivo. Sem versionamento = código perdido.
6. **Marco antes de avançar** — Não passa de fase por calendário. Passa quando executa o marco de validação. Data não valida conhecimento.
7. **Lab antes de teoria** — Se um conceito pode ser testado no lab, testa antes de anotar. Entendimento sem execução é ilusão.

---

## 📈 VISÃO DE LONGO PRAZO

```
Fases 1–5   →  Operador júnior com base técnica sólida, portfólio real e 2 certificações
Ano 2–3     →  Especialização: Cloud Sec, Malware Analysis ou Red Team puro
Ano 3–5     →  Referência técnica na área escolhida
Ano 5+      →  Você define o próximo mapa
```

> Este roadmap tem prazo de validade. O Código de Conduta, não.
> As ferramentas mudam. A disciplina é permanente.