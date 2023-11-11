import sqlite3

# Classe para lidar com o banco de dados
class BD:

    # Construtor
    def __init__(self, banco_dados):
        self.conectarbanco(banco_dados)

    def conectarbanco(self, banco_dados):
        self.banco = sqlite3.connect(banco_dados)
        self.cursor = self.banco.cursor()

        self.criartabelafilmes()

    def criartabelafilmes(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                duracao TEXT NULL,
                diretor TEXT NULL,
                estudio TEXT NULL,
                classificacao TEXT NULL,
                ano DATE NULL
            )
        """)

    def inserir(self, tabela, valores):
        sql = f"INSERT INTO {tabela}"

        for chave, valor in valores:
            print(chave)