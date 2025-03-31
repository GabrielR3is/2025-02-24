from database import Database
from produto_sql import *
from produto import Produto

def criar_tabela():
    """Cria a tabela produto se não existir"""
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_CREATE_TABLE)
        conexao.commit()

def inserir(produto: Produto) -> int:
    """
    Insere um novo produto no banco de dados
    Returns:
        int: ID do produto inserido
    """
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_INSERT, (produto.nome, produto.preco, produto.estoque))
        conexao.commit()
        return cursor.lastrowid

def atualizar(produto: Produto) -> bool:
    """
    Atualiza um produto existente
    Returns:
        bool: True se atualizou, False se não encontrou
    """
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_UPDATE, (produto.nome, produto.preco, produto.estoque, produto.id))
        conexao.commit()
        return cursor.rowcount > 0

def excluir(id: int) -> bool:
    """
    Exclui um produto pelo ID
    Returns:
        bool: True se excluiu, False se não encontrou
    """
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_DELETE, (id,))
        conexao.commit()
        return cursor.rowcount > 0

def obter_por_id(id: int) -> Produto:
    """
    Busca um produto pelo ID
    Returns:
        Produto: objeto produto ou None se não encontrou
    """
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_GET_BY_ID, (id,))
        resultado = cursor.fetchone()
        if resultado:
            return Produto(
                id=resultado['id'],
                nome=resultado['nome'],
                preco=resultado['preco'],
                estoque=resultado['estoque']
            )
        return None

def obter_por_pagina(limit: int, offset: int) -> list[Produto]:
    """
    Busca produtos com paginação
    Args:
        limit: quantidade de registros
        offset: deslocamento (página * limit)
    Returns:
        list[Produto]: lista de produtos
    """
    with Database.obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_GET_ALL_BY_PAGE, (limit, offset))
        resultados = cursor.fetchall()
        return [
            Produto(
                id=resultado['id'],
                nome=resultado['nome'],
                preco=resultado['preco'],
                estoque=resultado['estoque']
            )
            for resultado in resultados
        ]