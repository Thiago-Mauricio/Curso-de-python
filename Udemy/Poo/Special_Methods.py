class Book(object):
    def __init__(self, titulo, autor, paginas):
        print('Um livro foi criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}"

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Livro destruido')
    
livro1 = Book('Python', 'Thiago', 100)
print(livro1)
print(len(livro1))
del livro1