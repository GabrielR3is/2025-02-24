# SQL para criar a tabela Produto
SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
)
"""

# SQL para inserir um produto
SQL_INSERT = """
INSERT INTO produto (nome, preco, estoque)
VALUES (?, ?, ?)
"""

# SQL para atualizar um produto
SQL_UPDATE = """
UPDATE produto 
SET nome = ?, preco = ?, estoque = ?
WHERE id = ?
"""

# SQL para excluir um produto
SQL_DELETE = """
DELETE FROM produto
WHERE id = ?
"""

# SQL para buscar um produto pelo ID
SQL_GET_BY_ID = """
SELECT id, nome, preco, estoque
FROM produto
WHERE id = ?
"""

# SQL para buscar produtos com paginação
SQL_GET_ALL_BY_PAGE = """
SELECT id, nome, preco, estoque
FROM produto
LIMIT ? OFFSET ?
"""