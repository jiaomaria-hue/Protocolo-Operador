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
