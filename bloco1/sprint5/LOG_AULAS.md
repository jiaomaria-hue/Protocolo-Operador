# LOG DE AULAS — OSINT & RECON (Curso Solyd Offensive Security)

---

## Aula 1 — Introdução à coleta de informações
- **Conceito Chave:** Fundamentos da coleta de informações de fontes abertas e públicas sem a necessidade de interação direta/invasiva com o alvo (*passive reconnaissance*).
- **Objetivo:** Mapeamento do cenário de ataque, criação de perfil do alvo e identificação de superfícies de exposição antes de qualquer ação ofensiva direcional.

---

## Aula 2 — Google Hacking
- **Conceito Chave:** Uso de operadores avançados de busca (Dorks) para catalogar e filtrar informações públicas que o mecanismo de busca do Google indexou.
- **Funcionamento Técnico:** O Google não "grava tudo"; ele varre (*crawl*) e cataloga (*indexa*) dados acessíveis na web pública para consultas rápidas.
- **Principais Operadores e Sintaxes:**
  - `site:` Restringe a busca a um domínio específico (ex: `site:github.com`).
  - `intext:` Busca palavras especificamente no corpo/texto do conteúdo da página.
  - `inurl:` Filtra por termos presentes no endereço/URL da página.
  - `intitle:` Filtra pelo título presente na aba do navegador (ex: `intitle:"index of"` para identificar diretórios expostos sem arquivo `index` padrão).
  - `filetype:` Filtra extensões de arquivos específicos (ex: `pdf`, `sql`, `txt`, `doc`).

---

## Aula 3 — Google Hacking Database (GHDB)
- **Conceito Chave:** Repositório público mantido pelo Exploit-DB que reúne Dorks categorizadas e criadas pela comunidade de segurança.
- **Uso Prático:** Identificação automatizada de vulnerabilidades conhecidas, painéis administrativos, arquivos de configuração e diretórios sensíveis expostos.
- **Teste Prático Realizado:**
  - **Dork Utilizada:** `intitle:"index of /concrete/Password"` (GHDB ID 8424).
  - **Resultado:** Localização de diretório de arquivos expostos em servidor de terceiros.
- **Aspectos Éticos e Procedimentais (Purple Team / Pentest):**
  - **Reconhecimento vs. Exploração:** A identificação do diretório exposto via busca passiva constitui recon válido. O acesso ou download do conteúdo dos arquivos sem permissão configura acesso não autorizado.
  - **Fator Autorização:** A distinção entre atuação ética e infração reside estritamente na autorização formal por escrito (escopo de pentest/contrato).
  - **Responsible Disclosure & Bug Bounty:** Diante da descoberta não solicitada de exposição em terceiros, o procedimento adequado é a notificação responsável à equipe de TI/segurança da organização (via `security.txt` ou contatos oficiais) ou submissão via programas de Bug Bounty.

---

## Aula 4 — Bing Hacking
- **Sintaxe:** `ip:"<ENDEREÇO_IP>"` (no mecanismo de busca Bing).
- **Achado Prático / Aprendizado:** Ao executar o operador contra um IP (ex: `ip:"45.33.32.156"`), identificou-se uma volumosa listagem de domínios atrelados ao mesmo endereço.
- **Aplicação em OSINT:** A técnica de reverse IP mapeia não apenas servidores compartilhados, mas também **domínios irmãos da MESMA organização** (ex: `nmap.org`, `seclists.org`, `sectools.org`, `insecure.org`), expondo a superfície de ataque completa do alvo.

---

## Aula 5 — Coletando e-mails de organizações com Hunter.io
- **Conceito Chave:** Descoberta e mapeamento de endereços de e-mail corporativos vinculados a um domínio alvo (`nome@empresa.com`).
- **Aplicação em OSINT/Red Team:** Mapeamento de contatos e identificação do padrão de nomenclatura de e-mails para simulações de Engenharia Social / Phishing autorizados.
- **Decisão de OpSec (Segurança Operacional):** **Teste prático não realizado na ferramenta.** O Hunter.io exige cadastro utilizando número de telefone pessoal. Por diretrizes de OpSec (não expor dados pessoais a terceiros durante investigações), a ferramenta foi avaliada apenas teoricamente.
- **Alternativa Futura:** Ferramentas de linha de comando sem coleta de dados pessoais (ex: `theHarvester`, previsto no roadmap).

---

## Aula 6 — Identificando e-mails em vazamentos de dados
- **Conceito Chave:** Checagem de exposição de credenciais e pegada digital (*digital footprint*) por meio de bases agregadas de vazamentos de dados públicos.
- **Ferramenta Utilizada:** *Have I Been Pwned* (HIBP).
- **Como Funciona:** Consolida bilhões de registros vazados em incidentes de segurança cibernética e permite a consulta passiva por e-mail ou telefone.
- **Objetivo em OSINT:**
  1. Mapeamento de presença e cadastro do alvo em serviços web.
  2. Identificação das categorias de dados expostas em cada vazamento.
  3. Base analítica para avaliar padrões de criação e reutilização de senhas.
- **Nota Técnica:** O HIBP reporta a ocorrência do vazamento e as categorias expostas por razões éticas. Para cruzamento e análise avançada de credenciais cruas em investigações autorizadas, utilizam-se serviços dedicados (ex: DeHashed, LeakCheck).

## Aula 7 — theHarvester (Prática)

- **Comando:** theHarvester -d nmap.org -b all
- **Resultado:** 441 hosts, 16 IPs, 3 ASNs, 1 e-mail padrão

**Análise crítica do output:**
- Muitos hosts com nomes sem relação aparente ao Nmap (ex: koronaekszerkft-hu.nmap.org, vaccinehub-dev.nmap.org)
- Testei resolução DNS: TODOS retornam o MESMO IP (50.116.1.184) que o domínio principal nmap.org
- **Conclusão:** nmap.org usa Wildcard DNS — qualquer subdomínio inventado resolve pro mesmo servidor
- **Implicação de segurança:** Wildcard DNS mal configurado é vetor de abuso (phishing com subdomínios falsos, mascaramento de tráfego)
- **Lição:** Resultado de ferramenta de OSINT sempre precisa de VALIDAÇÃO manual antes de virar conclusão em relatório
