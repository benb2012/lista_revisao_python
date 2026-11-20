# Módulo responsável pela comunicação com o banco de dados SQLite.
# Criar a tabela produtos e implementar as operações do banco:
# cadastrar, listar, buscar, registrar entrada e saída de mercadorias.
# Também calcular produtos abaixo do estoque mínimo e valor total do estoque.
# Utilizar comandos SQL com parâmetros (?) e conn.commit() nas alterações.
# Este módulo será utilizado pelo arquivo estoque.py.

import sqlite3


def conectar(arquivo="estoque.db"):
    conn = sqlite3.connect(arquivo)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL,
            quantidade INTEGER,
            minimo INTEGER
        )
    """)

    conn.commit()

    return conn


def cadastrar(conn, nome, categoria, preco, quantidade=0, minimo=5):
    cursor = conn.execute("""
        INSERT INTO produtos
        (nome, categoria, preco, quantidade, minimo)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, categoria, preco, quantidade, minimo))

    conn.commit()

    return cursor.lastrowid


def listar(conn):
    return conn.execute("""
        SELECT * FROM produtos
        ORDER BY nome
    """).fetchall()


def buscar(conn, texto):
    return conn.execute("""
        SELECT * FROM produtos
        WHERE nome LIKE ?
        ORDER BY nome
    """, ("%" + texto + "%",)).fetchall()


def entrada(conn, id, quantidade):
    cursor = conn.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE id = ?
    """, (quantidade, id))

    conn.commit()

    return cursor.rowcount > 0


def saida(conn, id, quantidade):
    produto = conn.execute("""
        SELECT quantidade FROM produtos
        WHERE id = ?
    """, (id,)).fetchone()

    if produto is None:
        return "Produto não encontrado."

    if quantidade <= 0:
        return "A quantidade deve ser maior que zero."

    if quantidade > produto[0]:
        return f"Estoque insuficiente: há {produto[0]} unidade(s)."

    conn.execute("""
        UPDATE produtos
        SET quantidade = quantidade - ?
        WHERE id = ?
    """, (quantidade, id))

    conn.commit()

    return "Saída registrada."


def estoque_baixo(conn):
    return conn.execute("""
        SELECT * FROM produtos
        WHERE quantidade < minimo
        ORDER BY nome
    """).fetchall()


def valor_total(conn):
    resultado = conn.execute("""
        SELECT SUM(preco * quantidade)
        FROM produtos
    """).fetchone()

    if resultado[0] is None:
        return 0

    return resultado[0]