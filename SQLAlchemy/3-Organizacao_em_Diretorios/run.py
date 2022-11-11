from infra.repository.livros_repository import LivrosRepository

repo = LivrosRepository()

repo.insert(autor="Autor A", titulo="Titulo A", genero="Genero A", ano=2000)
repo.insert(autor="Autor B", titulo="Titulo B", genero="Genero B", ano=2001)
repo.insert(autor="Autor C", titulo="Titulo C", genero="Genero C", ano=2002)

repo.delete(titulo="Titulo C")

data = repo.select()

print(data)
