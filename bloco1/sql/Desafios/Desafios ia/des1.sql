CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    categoria TEXT,
    preco REAL,
    stock INTEGER
);

CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cidade TEXT NOT NULL,
    pontos INT
);

SELECT * FROM produtos