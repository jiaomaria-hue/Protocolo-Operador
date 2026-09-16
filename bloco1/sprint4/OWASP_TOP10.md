# OWASP Top 10 2025 — Resumo

## A01 — Broken Access Control
Controle de acesso quebrado. Usuário consegue acessar dados de outro usuário mudando ID na URL (IDOR). Exemplo: /usuario/123 → muda pra /usuario/456 → vê perfil de outro. Causa: site não verifica permissão.

## A02 — Misconfiguration
Servidor mal configurado. Admin console aberto, senhas padrão não trocadas, erros detalhados expostos. Causa: dev não seguiu checklist de segurança.

## A03 — Supply Chain Failures
Usa dependência/biblioteca com vulnerabilidade. Exemplo: Log4j 2.14 tem CVE crítico → sua app é hackeada via Log4j. Causa: não atualiza dependências velhas.

## A04 — Cryptographic Failures
Dados sem criptografia ou criptografia fraca. Exemplo: senha transmitida em HTTP (texto puro) em vez de HTTPS. Qualquer um na rede vê. Causa: dev não usou SSL/TLS.

## A05 — Injection
Injeta código via entrada. Exemplo: campo de busca `' OR 1=1--` → burla SQL query → retorna tudo. Causa: input não validado antes de usar em comando.

## A06 — Insecure Design
Arquitetura ruim desde o começo, sem pensar em segurança. Exemplo: sem limite de tentativas de login → brute force de senha funciona. Causa: dev não modelou ameaças.

## A07 — Authentication Failures
Falhas em autenticação. Senha fraca "123456", sem MFA, session que não expira. Exemplo: credential stuffing (tenta senhas de outro hack). Causa: autenticação descuidada.

## A08 — Data Integrity Failures
Dados/software modificados sem você saber. Exemplo: .exe hackeado → você baixa → roda malware. Causa: sem verificação de hash/assinatura.

## A09 — Logging & Monitoring Failures
Sem logs, ninguém vê ataque. Exemplo: hacker exfiltra dados a semana inteira → sem log → descobre só depois. Causa: não log eventos críticos ou logs não monitorados.

## A10 — Improper Exception Handling
Erros mal tratados expõem dados. Exemplo: stack trace na página → revela caminho do servidor, banco usado, versões. Causa: dev não tratou exceção.
