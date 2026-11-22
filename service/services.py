from repository.dao_entity import DAOEntity
from entities.entity import Livro

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo, sinopse=""):
        if not titulo or not titulo.strip():
            raise ValueError("Titulo obrigatório")
        resposta_sinopse = ""
        if sinopse:
            resposta_sinopse = sinopse.strip()
        retorno_livro = Livro(titulo.strip(), resposta_sinopse, alugado=False)
        return self.repository.create(retorno_livro)
            
        

    def list(self):
        return self.repository.find_all()

    def get(self, livro_id):
        livro_encontrado = self.repository.find_by_id(livro_id)
        if livro_encontrado:
            return livro_encontrado
        raise ValueError("Não existe livro com esse id")
        

    def update(self, livro_id, titulo, sinopse=""):
        resposta_sinopse = ""
        resposta_titulo = ""
        if not titulo or not titulo.strip():
            raise ValueError("Titulo obrigatório")
        resposta_titulo = titulo.strip()
        if sinopse:
            resposta_sinopse = sinopse.strip()
        livro_encontrado = self.get(livro_id)
        livro_encontrado.titulo = resposta_titulo
        livro_encontrado.sinopse = resposta_sinopse
        self.repository.update(livro_encontrado)
           

    def delete(self, livro_id):
        self.get(livro_id)
        self.repository.delete(livro_id)
        
    def alugar(self, livro_id):
        livro_encontrado = self.get(livro_id)
        if livro_encontrado.alugado:
            raise ValueError("Livro já alugado")
        self.repository.alugar(livro_id)
        
    def devolver(self, livro_id):
        livro_encontrado = self.get(livro_id)
        if not(livro_encontrado.alugado):
            raise ValueError("Livro já disponível")
        self.repository.devolver(livro_id)