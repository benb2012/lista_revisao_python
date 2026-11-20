# Módulo responsável pelo banco de dados da Cineflix.
# Criar as tabelas de títulos e visualizações no SQLite.
# Importar os títulos do catalogo.json para o banco na primeira execução,
# evitando duplicar os registros quando o programa for aberto novamente.
# Implementar as operações necessárias para registrar visualizações,
# consultar históricos, contar os títulos mais assistidos
# e calcular o tempo assistido por perfil.
# Utilizar JOIN, GROUP BY e comandos SQL com parâmetros (?).

import sqlite3
import json


def conectar(arquivo="cineflix.db"):
    conn = sqlite3.connect(arquivo)

    conn.execute("PRAGMA foreign_keys = ON")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS titulos (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            tipo TEXT,
            genero TEXT,
            ano INTEGER,
            duracao_min INTEGER,
            classificacao TEXT,
            nota REAL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS visualizacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            perfil TEXT,
            titulo_id INTEGER,
            minutos INTEGER,
            data TEXT,
            FOREIGN KEY (titulo_id) REFERENCES titulos(id)
        )
    """)

    conn.commit()

    quantidade = conn.execute(
        "SELECT COUNT(*) FROM titulos"
    ).fetchone()[0]

    if quantidade == 0:
        with open("catalogo.json", "r", encoding="utf-8") as arquivo_json:
            catalogo = json.load(arquivo_json)

        for item in catalogo:
            conn.execute("""
                INSERT INTO titulos
                (id, titulo, tipo, genero, ano, duracao_min,
                 classificacao, nota)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                item["id"],
                item["titulo"],
                item["tipo"],
                item["genero"],
                item["ano"],
                item["duracao_min"],
                item["classificacao"],
                item["nota"]
            ))

        conn.commit()

    return conn


def listar_titulos(conn):
    return conn.execute("""
        SELECT * FROM titulos
        ORDER BY titulo
    """).fetchall()


def registrar_visualizacao(conn, perfil, titulo_id, minutos, data):
    titulo = conn.execute("""
        SELECT id FROM titulos
        WHERE id = ?
    """, (titulo_id,)).fetchone()

    if titulo is None:
        return False

    conn.execute("""
        INSERT INTO visualizacoes
        (perfil, titulo_id, minutos, data)
        VALUES (?, ?, ?, ?)
    """, (perfil, titulo_id, minutos, data))

    conn.commit()

    return True


def historico(conn, perfil):
    return conn.execute("""
        SELECT visualizacoes.data, titulos.titulo, visualizacoes.minutos
        FROM visualizacoes
        JOIN titulos ON titulos.id = visualizacoes.titulo_id
        WHERE visualizacoes.perfil = ?
        ORDER BY visualizacoes.data DESC
    """, (perfil,)).fetchall()


def mais_assistidos(conn):
    return conn.execute("""
        SELECT titulos.titulo, COUNT(visualizacoes.id) AS total
        FROM visualizacoes
        JOIN titulos ON titulos.id = visualizacoes.titulo_id
        GROUP BY titulos.id
        ORDER BY total DESC
        LIMIT 5
    """).fetchall()


def tempo_por_perfil(conn):
    return conn.execute("""
        SELECT perfil, SUM(minutos)
        FROM visualizacoes
        GROUP BY perfil
        ORDER BY perfil
    """).fetchall()