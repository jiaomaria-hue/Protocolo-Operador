# Relatório de Avaliação de Segurança / Penetration Test

**Alvo:** Blue (TryHackMe)

**Endereço IP:** `10.64.161.235`

**Classificação do Alvo:** Máquina Interna de Testes (Windows 7 / Server 2008 R2)

**Classificação de Risco Geral:** CRÍTICO

---

## 1. Sumário Executivo

Durante a avaliação de segurança realizada na máquina alvo, foi identificada uma vulnerabilidade crítica no serviço de partilha de ficheiros e impressoras (SMBv1). A falha permitiu a execução remota de código (RCE) sem necessidade de autenticação, resultando no comprometimento total do sistema e na obtenção do nível máximo de privilégios (`NT AUTHORITY\SYSTEM`).

---

## 2. Escopo e Metodologia

O teste foi conduzido seguindo as fases da metodologia PTES (*Penetration Testing Execution Standard*):

1. Reconhecimento e Mapeamento de Portas
2. Análise de Vulnerabilidades
3. Exploração Inicial (Initial Access)
4. Estabilização e Elevação de Privilégios (Post-Exploitation)
5. Coleta de Evidências (Hashes e Banners)

---

## 3. Detalhamento Técnico das Etapas

### Fase 1: Reconhecimento e Coleta de Informações

Através do mapeamento de rede, identificou-se que o alvo mantinha abertas as portas associadas ao protocolo SMB:

* **Portas ativas:** `135/tcp`, `139/tcp`, `445/tcp`
* **Sistema Operacional identificado:** Windows (build legada incompatível com os padrões atuais de segurança).

### Fase 2: Análise de Vulnerabilidade

A varredura confirmou a presença da vulnerabilidade **MS17-010 (EternalBlue)** no protocolo SMBv1, que permite a injeção e execução de código no espaço de memória do *kernel* do sistema operacional.

### Fase 3: Exploração Inicial (Initial Access)

* **Módulo Utilizado:** `exploit/windows/smb/ms17_010_eternalblue`

* **Parâmetro de Alvo (`RHOSTS`):** `10.64.161.235`

* **Payload Inicial:** `windows/x64/shell/reverse_tcp`

* **Resultado:** Conexão reversa estabelecida com sucesso, gerando uma *Command Shell* remota no alvo.

### Fase 4: Pós-Exploração e Estabilização de Sessão

Para garantir o gerenciamento avançado da máquina e contornar a instabilidade da *shell* básica:

1. **Conversão de Shell para Meterpreter:**
* Módulo: `post/multi/manage/shell_to_meterpreter`

* Parâmetro: `SESSION 1`



2. **Migração de Processo:**
* Para garantir a persistência da sessão e evitar quedas, foi realizada a migração do processo ativo (`PID 1832`) para o processo do sistema **`LogonUI.exe`** (`PID 1996`).




3. **Privilégios Confirmados:** `NT AUTHORITY\SYSTEM` (Grau máximo de controle no sistema operacional).



### Fase 5: Extração de Credenciais e Quebra de Hashes

Com o nível de acesso obtido, utilizou-se a funcionalidade `hashdump` para extrair as credenciais armazenadas na base SAM do Windows.

* **Hash Extraído (Usuário Jon):**
`Jon:1002:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d`
* **Identificação do Hash NTLM:** `ffb43f0de35be4d9917ac0cc8ad57f8d`
* **Ataque de Dicionário (Cracking Offline):**
* **Ferramenta:** John the Ripper (`--format=NT`)
* **Wordlist:** `rockyou.txt`
* **Senha Revelada:** `alqfna22`



### Fase 6: Localização de Evidências (Flags)

1. **Flag 1 (Raiz do Disco):** `C:\flag1.txt`
2. **Flag 2 (Base de Configuração/SAM):** `C:\Windows\System32\config\flag2.txt`
3. **Flag 3 (Documentos do Usuário):** `C:\Users\Jon\Documents\flag3.txt`

---

## 4. Plano de Remediação e Recomendações (Defesa)

1. **Desativação do Protocolo SMBv1:** O uso do SMBv1 deve ser completamente desativado em toda a rede interna por ser um protocolo obsoleto e vulnerável.
2. **Aplicação de Patches (Atualização do Sistema):** Aplicar o boletim de segurança **MS17-010** fornecido pela Microsoft.
3. **Segregação de Rede e Firewall:** Bloquear o acesso direto às portas `139` e `445` a partir de redes externas ou não confiáveis.
4. **Política de Senhas:** Exigir senhas complexas e alterar credenciais que constem em listas públicas de vazamentos.
