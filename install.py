from database.connection import get_connection

def install():
    connection = get_connection()

    try:

        connection.execute("""
        CREATE TABLE IF NOT EXISTS livro(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR NOT NULL,
        sinopse VARCHAR,
        alugado INTEGER NOT NULL DEFAULT 0)
""")

        contagem = connection.execute("SELECT COUNT (*) AS total FROM livro")
        if contagem.fetchone()["total"] == 0:
            connection.execute("INSERT INTO livro(titulo, sinopse, alugado) VALUES (?, ?, ?)", ('O Principe', 'obra política de Nicolau Maquiavel', 0))
            connection.execute("INSERT INTO livro(titulo, sinopse, alugado) VALUES (?, ?, ?)", ('Metamorfose', 'obra crítica de Franz Kafka', 1))
        
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")