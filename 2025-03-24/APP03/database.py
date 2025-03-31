import sqlite3

class Database:
    @classmethod
    def obter_conexao(cls):
        """
        Obtém uma conexão com o banco de dados SQLite.
        Returns:
            sqlite3.Connection: Conexão com o banco de dados
        """
        conexao = sqlite3.connect('dados.db')
        conexao.row_factory = sqlite3.Row
        return conexao