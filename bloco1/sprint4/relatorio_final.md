# Relatório de Vulnerabilidades Exploradas — Sprint 4

## 1. SQL Injection (UNION-based)
- **Tipo:** Injection
- **Alvo:** PortSwigger Lab
- **Payload:** `' UNION SELECT @@version, NULL#`
- **Impacto:** Extração de dados do banco (versão MySQL)
- **Mitigação:** Usar prepared statements, input validation

## 2. Cross-Site Scripting (XSS Refletido)
- **Tipo:** XSS
- **Alvo:** PortSwigger Lab
- **Payload:** `<img src=x onerror=alert('xss')>`
- **Impacto:** Execução de JavaScript no navegador da vítima
- **Mitigação:** Sanitizar entrada, usar Content Security Policy (CSP)

## 3. IDOR (Escalação Horizontal de Privilégio)
- **Tipo:** Broken Access Control
- **Alvo:** PortSwigger Lab
- **Exploração:** Mudei `/my-account?id=wiener` pra `id=carlos`
- **Impacto:** Acesso a dados sensíveis de outro usuário (API key)
- **Mitigação:** Verificar permissão antes de retornar dados

## Lab 4 — SQLi Oracle (UNION SELECT com FROM dual)

- **Banco:** Oracle 11.2.0.2.0
- **Colunas:** 2 (descoberto com ORDER BY)
- **Coluna de texto:** 1ª coluna
- **Payload de teste:** `' UNION SELECT 'abc',NULL FROM dual--`
- **Payload de extração:** `' UNION SELECT banner,NULL FROM v$version--`
- **Resultado:** Versão completa do Oracle extraída

**Por que funciona:**
- UNION junta 2 queries
- FROM dual permite SELECT sem tabela real
- Coluna de texto renderiza dados na página
- Sem validação = dados sensíveis expostos

**Diferença Oracle vs MySQL:**
- MySQL usa `@@version`
- Oracle usa `v$version` (tabela de sistema)
- MySQL não precisa `FROM`, Oracle precisa `FROM dual`

## XSS Stored — Lab 5

- **Vulnerabilidade:** Stored XSS em comentário
- **Payload:** `<script>alert('xss')</script>`
- **Como:** Injetei no campo de comentário, site salvou no banco
- **Resultado:** Alert executou pra todos que viram o post

**Por que funciona:**
- Site aceita HTML sem validar
- Salva no banco LITERALMENTE
- Quando renderiza, JavaScript executa

**Impacto real:**
- Roubar cookies (sessão)
- Roubar dados sensíveis
- Redirecionar pra phishing
