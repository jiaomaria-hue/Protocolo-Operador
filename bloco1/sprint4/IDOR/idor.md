## IDOR — Lab 2

- **Vulnerabilidade:** ID do usuário controlado pelo parâmetro de requisição
- **Como explorei:** 
  1. Login como wiener
  2. Mudei `/my-account?id=wiener` pra `/my-account?id=carlos`
  3. Consegui ver perfil de carlos (escalação horizontal de privilégio)
- **Resultado:** Obtive API key de carlos
- **Por que funciona:** Sem validação de permissão → qualquer usuário vê dados de outro
- **Impacto:** Roubo de dados sensíveis de outros usuários
