from database.connection import get_connection
from entities.entity import Livro

class DAOEntity:

    def create(self, livro):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO livro (titulo, sinopse, alugado) VALUES (?, ?, ?)", (livro.titulo, livro.sinopse, int(livro.alugado)))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()
            

    def find_all(self):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM livro")
            listaLivro = cursor.fetchall()
            listaResposta = []
            for unidade in listaLivro:
                listaResposta.append(Livro(unidade["titulo"], unidade["sinopse"], bool(unidade["alugado"]), unidade["id"]))
            return listaResposta
        finally:
            connection.close()


    def find_by_id(self, livro_id):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM livro WHERE id = ?", (livro_id,))
            buscado = cursor.fetchone()
            if buscado:
                return Livro(buscado["titulo"], buscado["sinopse"], bool(buscado["alugado"]), buscado["id"])
            else:
                return None
        finally:
            connection.close()

    def update(self, livro):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE livro SET titulo = ?, sinopse = ? WHERE id = ?", (livro.titulo, livro.sinopse, livro.id))
            connection.commit()
        finally:
            connection.close()
        

    def delete(self, livro_id):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM livro WHERE id = ?", (livro_id,))
            connection.commit()
        finally:
            connection.close()
            
    def alugar(self, livro_id):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE livro SET alugado = 1 WHERE id = ?", (livro_id,))
            connection.commit()
        finally:
            connection.close()
            
    def devolver(self, livro_id):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE livro SET alugado = 0 WHERE id = ?", (livro_id,))
            connection.commit()
        finally:
            connection.close()