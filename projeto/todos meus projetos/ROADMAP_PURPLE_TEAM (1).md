# 🗺️ MAPA DE ELITE — PROTOCOLO DE 18 MESES
### Purple Team / Security Engineering · Joao · Palmas, TO
> "A perfeição na segurança cibernética não é um desenho bonitinho. É um ciclo de guerra infinito."

---

## ⚡ MISSÃO DE ATIVAÇÃO — HOJE (28/05/2026)

- [ ] Abrir o terminal e criar olamundo.py
- [ ] Criar LOG_DE_GUERRA.md com entrada: 28/05/2026 — Iniciado Protocolo de Elite
- [ ] Criar repositório Protocolo-Operador no GitHub e fazer primeiro commit
- [ ] Assistir Aula 1 da SecDay Academy no YouTube

---

## 📚 FONTES DE ESTUDO

| Fonte | Como usar | Fase |
|---|---|---|
| SecDay Academy — 16 aulas (YouTube) | Fundação Linux e Redes | Fase 1–2 |
| Cisco Networking Academy | Redes + Intro Cibersegurança (certificado gratuito) | Fase 1–2 |
| TryHackMe — Jr Pentester | Campo de batalha prático | Fase 3+ |
| HackTheBox | Prática avançada, ambientes reais | Final Fase 3+ |

> TikTok (studywithme cibersegurança): radar de conceitos e motivação. Não é fonte técnica.

---

## 💻 PROGRESSÃO DE LINGUAGENS

```
Fase 1      →  Python           (automação, scripts, exploits simples)
Fase 2–3    →  Bash             (terminal Linux, aprofundar)
Fase 2–3    →  SQL              (SQL Injection é OWASP Top 10 — obrigatório)
Fase 3      →  Ruby (leve)      (ler módulos do Metasploit)
Fase 4      →  PowerShell       (obrigatório para AD e ambientes Windows)
Fase 5      →  C / C++          (engenharia reversa, leitura de malware)
Fase 5+     →  Assembly x86/x64 (só se especializar em Reverse Engineering)
```

> Regra de ouro: você não aprende linguagem por curiosidade. Aprende quando um problema exige.

---

## FASE 1 — DOMÍNIO DA MÁQUINA `Meses 1–3`
> Onde você sai de usuário para Operador.

**O que aprender**
- Linux terminal — permissões (chmod/chown), usuários, processos. Nunca mais usar o mouse.
- Python puro — lógica, funções, arquivos, tratamento de erros, controle de fluxo
- Bash scripting básico
- Git + GitHub desde o Dia 1
- Tríade CIA — Confidencialidade, Integridade, Disponibilidade
- Criptografia básica — SHA, AES, RSA (o que são, como funcionam, onde aparecem)

**Fontes desta fase**
- SecDay Academy — trilha Bases Fundamentais (16 aulas)
- Cisco Networking Academy — Introdução à Cibersegurança

**O que entregar**
- Scripts de gestão de sistema. Zero interface gráfica.
- Projeto firewall_logic.py rodando no terminal
- Repositório Protocolo-Operador no GitHub com commits regulares
- VirtualBox instalado com primeira VM criada

**📅 Rotina Semanal — Fase 1**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Aula da SecDay ou Cisco + anotar conceitos no VS Code |
| Terça + Quinta | Prática | Escrever scripts Python + praticar comandos no terminal |
| Sexta | Consolidação | Push no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Revisar erros da semana ou descansar |

> Foco total: Python e terminal. TryHackMe ainda não — você não tem base suficiente pra aproveitar.

---

## FASE 2 — VIGILÂNCIA DA REDE `Meses 4–6`
> Entender como os dados se movem é entender o campo de batalha.

**O que aprender**
- Modelo OSI — 7 camadas na ponta da língua
- TCP/IP, DNS, DHCP, HTTP/S, ARP, ICMP
- TCP Handshake vs UDP — diferença e implicações de segurança
- Subnetting e CIDR — MAC vs IP, endereçamento de redes
- VLANs e Tabelas de Roteamento básicas
- NIST CSF e ISO 27001 — noções básicas (o mercado corporativo cobra)

**Ferramentas**
- Wireshark — captura e análise de tráfego real
- Nmap — reconhecimento de redes e serviços
- Netcat — canivete suíço de rede
- Scapy — manipulação de pacotes via Python

**Fontes desta fase**
- Cisco Networking Academy — cursos de redes
- SecDay Academy — automação com Python

**O que entregar**
- Port Scanner em Python que identifica serviços rodando em portas
- Capturas de tráfego reais documentadas no LOG_DE_GUERRA.md
- Entender cada pacote que passa pela sua rede local

**📅 Rotina Semanal — Fase 2**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Cisco (redes) + anotar no VS Code |
| Terça + Quinta | Prática | Wireshark + Nmap + scripts de rede em Python |
| Sexta | Consolidação | Push no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Revisar capturas de tráfego e anotações |

> Começa a usar Wireshark e Nmap de verdade. Cada pacote que você capturar vai pro LOG.

---

## FASE 3 — ARTE DA OFENSIVA — RED `Meses 7–10`
> Mentalidade de invasor. Se a máquina não cair, você não para.

**O que aprender**
- OWASP Top 10
- Engenharia de exploits e CVE analysis
- Metodologia: Reconhecimento → Enumeração → Exploração → Pós-exploração
- OSINT e Engenharia Social — coleta de informação passiva e ativa
- Como escrever Relatórios de Pentest profissionais

**Ferramentas**
- Burp Suite — interceptação e manipulação de requisições web
- Metasploit — framework de exploração
- OSINT Framework, Maltego (básico)

**Plataformas**
- TryHackMe — caminho Jr Penetration Tester (do início ao fim)
- HackTheBox — últimas semanas da fase
- Quando travar: pesquise o write-up da máquina. É assim que profissionais aprendem.

**O que entregar**
- Caminho Jr Pentester do TryHackMe completo
- Write-ups das máquinas documentados no GitHub
- Pelo menos 1 relatório de pentest formatado profissionalmente
- LOG_DE_GUERRA com metodologia de cada invasão

**📅 Rotina Semanal — Fase 3**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Estudar OWASP, exploits, CVEs + anotar no VS Code |
| Terça + Quinta | Prática | TryHackMe / HackTheBox + scripts de ataque em Python |
| Sexta | Consolidação | Push write-up no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Revisar máquinas que não caíram + estudar write-ups |

> Se a máquina não cair na Terça, você volta pra ela na Quinta. Sem pular.

---

## FASE 4 — ARTE DA DEFESA — BLUE `Meses 11–13`
> Você só defende bem o que aprendeu a atacar.

**O que aprender**
- Hardening de sistemas Linux e Windows
- Análise de logs — distinguir tráfego normal de ataque
- Firewalls na prática — UFW e Iptables
- Resposta a Incidentes — como agir quando o ataque já aconteceu
- Forense Digital básico — memória, disco, artefatos
- IAM, MFA, SSO — gestão de identidade e acesso
- Cloud Security (AWS/Azure) — IAM, políticas, misconfigurações comuns
- Segurança em Contêineres — Docker e K8s básico
- DevSecOps — segurança integrada em CI/CD

**Ferramentas**
- UFW / Iptables
- Wazuh — SIEM open source, detecção de intrusão
- Splunk — análise de logs em escala
- AWS Free Tier / Azure Student — primeiros labs em cloud

**O que entregar**
- Hardening completo de cada máquina invadida na Fase 3
- SIEM configurado detectando exatamente os ataques que você executou
- Documentação de defesa como contrapartida dos write-ups de ataque

**📅 Rotina Semanal — Fase 4**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Estudar hardening, logs, SIEM, cloud + anotar no VS Code |
| Terça + Quinta | Prática | Configurar Wazuh/Splunk + aplicar hardening nas VMs + labs AWS |
| Sexta | Consolidação | Push documentação de defesa no GitHub + LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Rever configurações e testar se o SIEM detecta os ataques certos |

> Pega cada máquina que você invadiu na Fase 3 e fecha todas as brechas.

---

## FASE 5 — CONSIDERAÇÃO DE ELITE `Meses 14–18`
> Purple Team completo: você ataca, detecta, responde e endurece.

**O que aprender**
- Active Directory — estrutura, GPO, ataques (Pass-the-Hash, Kerberoasting) e defesa
- Cloud Security avançado — IAM profundo, políticas, arquitetura segura
- Engenharia Reversa — análise estática e dinâmica de binários
- Threat Intelligence — MITRE ATT&CK, IOCs, TTPs

**Ferramentas**
- Ghidra / radare2 — análise de binários e malware
- MITRE ATT&CK Navigator — mapeamento de táticas e técnicas
- Azure AD / AWS IAM — gestão de identidade em cloud

**O que entregar**
- Portfólio público no GitHub com projetos de Purple Team
- Writeups completos de cada simulação
- Ciclo completo por projeto: ataque → detecção → resposta → hardening → relatório

**Certificações**
- BTL1 — Blue Team Level 1 (valida o lado defensivo)
- eJPT — Entry Level Penetration Tester (eLearnSecurity)
- CompTIA Security+ — reconhecimento internacional de mercado
- OSCP — meta pós-protocolo, o ouro do Red Team

**📅 Rotina Semanal — Fase 5**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Active Directory, Engenharia Reversa, MITRE ATT&CK + anotações |
| Terça + Quinta | Prática | Simulações Purple Team completas + projetos de automação |
| Sexta | Consolidação | Push portfólio no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Estudar para certificações (BTL1 / eJPT / Security+) |

> Ciclo completo todo projeto: ataque → detecção → resposta → hardening → relatório.

---

## 🛡️ CÓDIGO DE CONDUTA DO OPERADOR

1. **Regra dos 15 min** — Travou? Pesquise por 15 minutos. Não resolveu? Pergunta imediatamente.
2. **LOG_DE_GUERRA.md** — Todo erro resolvido entra no log: data, problema, tentativas, solução.
3. **Ambiente impecável** — Scripts limpos, comentados e funcionais. Código sujo é vetor de falha.
4. **Automação sempre** — Fez manualmente duas vezes? Na terceira, cria o script Python.
5. **Git é sagrado** — Todo script vai pro GitHub com commit descritivo. Sem versionamento = código perdido.

---

## 📈 VISÃO DE LONGO PRAZO

```
Meses 1–18  →  Operador júnior com base técnica sólida e portfólio real
Ano 2–3     →  Especialização: Cloud Sec, Malware Analysis ou Red Team puro
Ano 3–5     →  Referência técnica na área escolhida
Ano 5+      →  Você define o próximo mapa
```

> Este roadmap tem prazo de validade. O Código de Conduta, não.
> As ferramentas mudam. A disciplina é permanente.
