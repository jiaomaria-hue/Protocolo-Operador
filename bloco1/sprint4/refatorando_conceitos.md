# Conceitos WEB (cookies, sessao e burpsuite)
## Cookie
- É um ID guardado NO SEU NAVEGADOR (client-side)
- Existe porque HTTP não tem memória entre requisições — sem cookie, o site esqueceria que você logou
- Exemplo prático que já vi: Admin=false/true no lab de IDOR

## Sessão
- É o registro real (quem você é, permissões) guardado NO SERVIDOR (server-side)
- O cookie só carrega o ID; o servidor usa esse ID pra buscar a sessão correspondente
- Por isso roubar um cookie (via XSS) permite se passar por alguém sem saber a senha

# Burpsuite

## Proxy
- Intercepta requisicoes em tempo real
- Pode muda-la quando quiser em repeater
- Exemplo: De uma pagina de login voce pode mudar de admin=false pra true no repeter

## Repeter
- Pode mudar e enviar requisicoes quando quiser
