from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
            print("Menu de Livros")
            print(" 1: cadastrar ; 2:Listar ; 3: atualizar ; 4: buscar ; 5: excluir ; 6:alugar ; 7:devolver; 0:encerrar")
            escolha = input("Escolha uma das opções: ").strip()
            
            if escolha == "0":
                print("encerrando")
                break
            elif escolha == "1":
                self._cadastrar()
            elif escolha == "2":
                self._listar()
            elif escolha == "3":
                self._atualizar()
            elif escolha == "4":
                self._buscar()
            elif escolha == "5":
                self._excluir()
            elif escolha == "6":
                self._alugar()
            elif escolha == "7":
                self._devolver()
            else:
                print("opção inválida")
            
            
    def _cadastrar(self):
        try:
            titulo = input("Digite o título do livro: ")
            sinopse = input("Digite a sinopse do livro(opcional): ")
            id_gerado = self.services.create(titulo, sinopse)
            print(f"Livro cadastrado, ID: {id_gerado}")
        except ValueError as error:
            print(f"erro: {error}")
    def _listar(self):
        livros = self.services.list()
        if not livros:
            print("Sem livros cadastrados")
        else:
            for livro in livros:
                print(livro)
    
    def _atualizar(self):
        try:
            livro_id = int(input("Digite o ID do livro: "))
            titulo = input("Digite o novo título do livro: ")
            sinopse = input("Digite a nova sinopse do livro(opcional): ")
            self.services.update(livro_id, titulo, sinopse)
            print("livro atualizado com sucesso")
        except ValueError as error:
            print(f"Erro: {error}")

    def _buscar(self):
        try:
            livro_id = int(input("Digite o ID do livro: "))
            livro = self.services.get(livro_id)
            print(livro)
        except ValueError as error:
            print(f"Erro: {error}")
    
    def _excluir(self):
        try:
            livro_id = int(input("Digite o ID do livro: "))
            livro = self.services.get(livro_id)
            print(livro)
            confirmar = input("Confirmar exclusão? (S/N): ").strip().upper()
            if confirmar == "S":
                self.services.delete(livro_id)
                print("Livro deletado com sucesso")
            else:
                print("Ato de deletar cancelado")
        except ValueError as error:
            print(f"Erro: {error}")

    def _alugar(self):
        try:
            livro_id = int(input("Digite o ID do livro: "))
            livro = self.services.alugar(livro_id)
            print("Livro alugado com sucesso")
        except ValueError as error:
            print(f"Erro: {error}")
    
    def _devolver(self):
        try:
            livro_id = int(input("Digite o ID do livro: "))
            livro = self.services.devolver(livro_id)
            print("Livro devolvido com sucesso")
        except ValueError as error:
            print(f"Erro: {error}")
            
            
                    
                
                
                
            
        