## XSS Refletido — Lab 1

- **Payload:** `<img src=x onerror=alert('xss')>`
- **Resultado:** Alert executado no navegador
- **Por que funciona:** Entrada não sanitizada → HTML renderizado → JavaScript executado
- **Impacto:** Atacante consegue roubar cookies, dados, fazer phishing

## XSS explicado.

- Oque e xss?
O XSS é a injeção de código JavaScript malicioso em uma aplicação web confiável. Ele funciona porque o navegador confia cegamente em tudo o que o site envia, permitindo que o atacante tome o controle da sessão e das ações da vítima dentro daquela aplicação.

- Como funciona o XSS
O xss ele funciona manipulando um site que execute um codigo javascript malicioso para a pessoa que entrar na url. Quando o codigo e executado no navegador da pessoa ele compromete totalmente sua interacao com o app

- Tipos de ataques de XSS

XSS refletido, onde o script malicioso vem da solicitacao HTTP atual
Armazenado XSS, onde o script malicioso vem do banco de daods do site
XSS baseado em DOM, onde a vulnerabilidade existe no codigo do lado do client em vez do codigo do lado do servidor 

- Explicando cada tipos de ataque XSS
