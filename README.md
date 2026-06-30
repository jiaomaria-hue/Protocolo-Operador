# 🛡️ Protocolo-Operador
### Purple Team / Security Engineering · Joao · Palmas, TO

> *"A perfeição na segurança cibernética não é um desenho bonitinho. É um ciclo de guerra infinito."*

---

## 👤 Sobre

Repositório oficial do meu protocolo de 18 meses para me tornar um operador de elite em cibersegurança.
Aqui estão meus scripts, anotações, write-ups, projetos e LOG_DE_GUERRA.

| | |
|---|---|
| **Foco** | Purple Team / Security Engineering |
| **Localização** | Palmas, Tocantins — BR |
| **Sistema** | Zorin OS |
| **Fase atual** | Fase 1 — Domínio da Máquina |
| **Iniciado em** | 28/05/2026 |

---

## ⚡ Missão de Ativação

- [x] Criar repositório Protocolo-Operador no GitHub
- [x] Criar `olamundo.py` e rodar no terminal
- [x] Criar `LOG_DE_GUERRA.md` com entrada: `28/05/2026 — Iniciado Protocolo de Elite`
- [x] Assistir Aula 1 da SecDay Academy no YouTube

---

## 🗺️ Roadmap — 18 Meses

### FASE 1 — Domínio da Máquina `Meses 1–3`
> Onde você sai de usuário para Operador.

**O que aprender**
- Linux terminal — permissões, usuários, processos. Zero mouse.
- Python puro — lógica, funções, arquivos, tratamento de erros
- Bash scripting básico
- Git + GitHub desde o Dia 1
- Tríade CIA — Confidencialidade, Integridade, Disponibilidade
- Criptografia básica — SHA, AES, RSA

**Fontes**
- SecDay Academy — trilha Bases Fundamentais (16 aulas)
- Cisco Networking Academy — Introdução à Cibersegurança

**Critérios para passar de fase**
- [ ] Navega no terminal sem usar o mouse para nada
- [ ] Tem pelo menos 5 scripts Python funcionando no GitHub
- [ ] `firewall_logic.py` completo e funcionando
- [ ] VirtualBox instalado com pelo menos 1 VM rodando
- [ ] LOG_DE_GUERRA.md com pelo menos 10 entradas reais
- [ ] Consegue explicar Tríade CIA e criptografia básica

**Rotina semanal**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Aula SecDay ou Cisco + anotar no VS Code |
| Terça + Quinta | Prática | Scripts Python + comandos no terminal |
| Sexta | Consolidação | Push no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Revisar erros da semana ou descansar |

---

### FASE 2 — Vigilância da Rede `Meses 4–6`
> Entender como os dados se movem é entender o campo de batalha.

**O que aprender**
- Modelo OSI — 7 camadas na ponta da língua
- TCP/IP, DNS, DHCP, HTTP/S, ARP, ICMP
- TCP Handshake vs UDP
- Subnetting e CIDR
- VLANs e Tabelas de Roteamento
- NIST CSF e ISO 27001 básico

**Ferramentas:** Wireshark, Nmap, Netcat, Scapy

**Critérios para passar de fase**
- [ ] Explica as 7 camadas do OSI de cabeça
- [ ] Port Scanner em Python funcionando no GitHub
- [ ] Capturou tráfego real com Wireshark e documentou no LOG
- [ ] Consegue usar Nmap para mapear a própria rede local
- [ ] Sabe calcular subnet básica (CIDR)

**Rotina semanal**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Cisco (redes) + anotar no VS Code |
| Terça + Quinta | Prática | Wireshark + Nmap + scripts de rede em Python |
| Sexta | Consolidação | Push no GitHub + atualizar LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Revisar capturas de tráfego e anotações |

---

### FASE 3 — Arte da Ofensiva — RED `Meses 7–10`
> Mentalidade de invasor. Se a máquina não cair, você não para.

**O que aprender**
- OWASP Top 10
- Engenharia de exploits e CVE analysis
- Metodologia: Reconhecimento → Enumeração → Exploração → Pós-exploração
- OSINT e Engenharia Social
- Relatórios de Pentest profissionais

**Ferramentas:** Burp Suite, Metasploit, OSINT Framework

**Plataformas:** TryHackMe (Jr Pentester) → HackTheBox

**Critérios para passar de fase**
- [ ] Caminho Jr Pentester do TryHackMe completo
- [ ] Pelo menos 3 máquinas resolvidas no HackTheBox
- [ ] Write-ups de todas as máquinas no GitHub
- [ ] Pelo menos 1 relatório de pentest profissional escrito
- [ ] Executa metodologia completa sem consultar

**Rotina semanal**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | OWASP, exploits, CVEs + anotar no VS Code |
| Terça + Quinta | Prática | TryHackMe / HackTheBox + scripts de ataque |
| Sexta | Consolidação | Push write-up no GitHub + LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Máquinas que não caíram + estudar write-ups |

---

### FASE 4 — Arte da Defesa — BLUE `Meses 11–13`
> Você só defende bem o que aprendeu a atacar.

**O que aprender**
- Hardening Linux e Windows
- Análise de logs — normal vs ataque
- Firewalls: UFW e Iptables
- Resposta a Incidentes
- Forense Digital básico
- IAM, MFA, SSO
- Cloud Security (AWS/Azure)
- Segurança em Contêineres (Docker/K8s)
- DevSecOps básico

**Ferramentas:** UFW/Iptables, Wazuh, Splunk, AWS Free Tier

**Critérios para passar de fase**
- [ ] Hardening completo das máquinas invadidas na Fase 3
- [ ] SIEM detectando os ataques que você mesmo executou
- [ ] Pelo menos 1 lab em cloud documentado
- [ ] Consegue analisar um log e identificar o ataque

**Rotina semanal**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | Hardening, logs, SIEM, cloud + anotar |
| Terça + Quinta | Prática | Configurar Wazuh/Splunk + hardening nas VMs |
| Sexta | Consolidação | Push documentação no GitHub + LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Testar se o SIEM detecta os ataques certos |

---

### FASE 5 — Consideração de Elite `Meses 14–18`
> Purple Team completo: você ataca, detecta, responde e endurece.

**O que aprender**
- Active Directory — ataques (Pass-the-Hash, Kerberoasting) e defesa
- Cloud Security avançado — IAM, arquitetura segura
- Engenharia Reversa — análise estática e dinâmica
- Threat Intelligence — MITRE ATT&CK, IOCs, TTPs

**Ferramentas:** Ghidra, radare2, MITRE ATT&CK Navigator, Azure AD / AWS IAM

**Critérios para passar de fase**
- [ ] Pelo menos 1 simulação Purple Team completa documentada
- [ ] Portfólio público no GitHub organizado
- [ ] Pelo menos 1 certificação tirada (BTL1 ou eJPT)
- [ ] Consegue mapear um ataque no MITRE ATT&CK Navigator

**Certificações**
- BTL1 — Blue Team Level 1
- eJPT — Entry Level Penetration Tester
- CompTIA Security+
- OSCP — meta pós-protocolo

**Rotina semanal**

| Dia | Foco | O que fazer |
|---|---|---|
| Segunda + Quarta | Teoria | AD, Eng. Reversa, MITRE ATT&CK + anotações |
| Terça + Quinta | Prática | Simulações Purple Team + projetos de automação |
| Sexta | Consolidação | Push portfólio no GitHub + LOG_DE_GUERRA.md |
| Sábado / Domingo | Revisão | Estudar para certificações |

---

## 💻 Progressão de Linguagens

```
Fase 1      →  Python           (automação, scripts, exploits simples)
Fase 2–3    →  Bash             (terminal Linux, aprofundar)
Fase 2–3    →  SQL              (SQL Injection é OWASP Top 10 — obrigatório)
Fase 3      →  Ruby (leve)      (ler módulos do Metasploit)
Fase 4      →  PowerShell       (obrigatório para AD e ambientes Windows)
Fase 5      →  C / C++          (engenharia reversa, leitura de malware)
Fase 5+     →  Assembly x86/x64 (só se especializar em Reverse Engineering)
```

> Regra: você não aprende linguagem por curiosidade. Aprende quando um problema exige.

---

## 📚 Fontes de Estudo

| Fonte | Como usar | Fase |
|---|---|---|
| SecDay Academy — 16 aulas (YouTube) | Fundação Linux e Redes | Fase 1–2 |
| Cisco Networking Academy | Redes + Intro Cibersegurança (certificado gratuito) | Fase 1–2 |
| TryHackMe — Jr Pentester | Campo de batalha prático | Fase 3+ |
| HackTheBox | Prática avançada, ambientes reais | Final Fase 3+ |

---

## 🛡️ Código de Conduta do Operador

1. **Regra dos 15 min** — Travou? Pesquise por 15 minutos. Não resolveu? Pergunta imediatamente.
2. **LOG_DE_GUERRA.md** — Todo erro resolvido entra no log: data, problema, tentativas, solução.
3. **Ambiente impecável** — Scripts limpos, comentados e funcionais. Código sujo é vetor de falha.
4. **Automação sempre** — Fez manualmente duas vezes? Na terceira, cria o script Python.
5. **Git é sagrado** — Todo script vai pro GitHub com commit descritivo. Sem versionamento = código perdido.

---

## 📁 Estrutura do Repositório

```
Protocolo-Operador/
├── README.md
├── LOG_DE_GUERRA.md
├── fase-1/
│   ├── olamundo.py
│   ├── firewall_logic.py
│   └── scripts/
├── fase-2/
│   ├── port_scanner.py
│   └── capturas/
├── fase-3/
│   ├── write-ups/
│   └── relatorios/
├── fase-4/
│   ├── hardening/
│   └── siem-configs/
└── fase-5/
    ├── purple-team/
    └── automacao/
```

---

## 📈 Visão de Longo Prazo

```
Meses 1–18  →  Operador júnior com base técnica sólida e portfólio real
Ano 2–3     →  Especialização: Cloud Sec, Malware Analysis ou Red Team puro
Ano 3–5     →  Referência técnica na área escolhida
Ano 5+      →  Você define o próximo mapa
```

> Este roadmap tem prazo de validade. O Código de Conduta, não.
> As ferramentas mudam. A disciplina é permanente.
