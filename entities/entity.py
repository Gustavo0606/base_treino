class Livro:
    def __init__(self, titulo, sinopse="", alugado=False, id=None):
        self.id = id
        self.titulo = titulo
        self.sinopse = sinopse
        self.alugado = alugado
        
    def __str__(self):
        disponivel = ""
        descricao = ""
        if self.alugado:
            disponivel = "sim"
        else:
            disponivel = "não"
        if self.sinopse:
            descricao = self.sinopse
        else:
            descricao = "Sem sinopse"
        return f" id: {self.id}, titulo: {self.titulo}, sinopse: {descricao}, alugado: {disponivel}"
        