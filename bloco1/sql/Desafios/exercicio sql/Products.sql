CREATE TABLE produtos (
    nome TEXT,
    preco REAL
);
INSERT INTO produtos (nome, preco) VALUES ('arroz', 8.5);
INSERT INTO produtos (nome, preco) VALUES ('feijao', 5.4);
INSERT INTO produtos (nome, preco) VALUES ('guarana', 7.4);
SELECT nome FROM produtos WHERE preco >= 6;
UPDATE produtos SET preco = 6.0 WHERE nome = 'feijao';
DELETE FROM produtos WHERE nome = 'feijao';
DELETE FROM 