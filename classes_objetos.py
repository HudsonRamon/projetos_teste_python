

class Livro():
    def __init__(self, cod, titulo, autor):
        
        self.codigo = cod
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False
        
class Biblioteca():
    def __init__(self):
        self.lista_livros = [] 
        
    def guardar_livro(self, obj_livro):
        
        self.lista_livros.append(obj_livro)
        
    def emprestimo(self, nome_aluno, cod_livro):
        livro = False
        
        for book in self.lista_livros:
            if(book.codigo == cod_livro):
                livro = book
                break
        if(livro):
            
            if(not livro.emprestado):
                
                livro.emprestado = True
                print(' Livro "' + livro.titulo + '" emprestado para ' + nome_aluno)
            else:
                print('O livro "' + livro.titulo + '" já foi emprestado para outra pessoa.')
        else:
            print("Não há livro com esse código.")
            
    def recebimento(self, cod_livro):
        livro = False
        for book in self.lista_livros:
            if(book.codigo == cod_livro):
                livro = book
                break
        if(livro):
            livro.emprestado = False
            print('Livro "' + livro.titulo + '" foi devolvido.')
        else:
            print("Não há livro com esse código.")


livro01  = Livro(123, "Dom Casmurro", "Machado de Assis")
livro02 = Livro(456, "Todos os contos", "Clarisse Lispector")
livro03 = Livro(789, "O alienista", "Machado de Assis")
biblioteca = Biblioteca()


biblioteca.guardar_livro(livro01)
biblioteca.guardar_livro(livro02)
biblioteca.guardar_livro(livro03)


while True:

    
    opt = str(input('Deseja pegar emprestado (E) ou devolver (D) um livro? [E/D] ')).upper()[0]
    print()
    
    if(opt == 'E'):
        
        aluno = str(input('Qual o seu nome? '))
        cod = int(input('Digite o código do livro para pegar emprestado ' + aluno +': '))
        print()
        biblioteca.emprestimo(aluno, cod)
    elif(opt == 'D'):
       
        cod = int(input('Digite o código do livro que será devolvido: '))
        print()
        biblioteca.recebimento(cod)
        
    print()
   
    res = str(input('Mais alguma coisa? [S/N] ')).upper()[0]
    print()
    
    if(res not in 'N'):
        continue
    else:
        break

