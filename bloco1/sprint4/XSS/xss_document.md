## XSS Refletido — Lab 1

- **Payload:** `<img src=x onerror=alert('xss')>`
- **Resultado:** Alert executado no navegador
- **Por que funciona:** Entrada não sanitizada → HTML renderizado → JavaScript executado
- **Impacto:** Atacante consegue roubar cookies, dados, fazer phishing
