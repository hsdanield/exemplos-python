from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# Configuracoes
engine = create_engine("mysql+pymysql://root:root@localhost:3306/dev")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Livros(Base):
    __tablename__ = "livros"

    autor = Column(String, nullable=False)
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme(titulo={self.titulo}, autor={self.autor}, genero={self.genero}, ano={self.ano})"


# SQL

# INSERT
data_insert = [
    Livros(autor="Autor A", titulo="Titulo A", genero="Genero A", ano=2018),
    Livros(autor="Autor B", titulo="Titulo B", genero="Genero B", ano=2019),
    Livros(autor="Autor C", titulo="Titulo C", genero="Genero C", ano=2020),
    Livros(autor="Autor D", titulo="Titulo D", genero="Genero D", ano=2021),
    Livros(autor="Autor E", titulo="Titulo E", genero="Genero E", ano=2022),
]
session.add(data_insert)
session.commit()

# DELETE
session.query(Livros).filter(Livros.titulo == "Titulo A").delete()
session.commit()

# UPDATE
session.query(Livros).filter(Livros.titulo == "Titulo E").update({"ano": 1999})
session.commit()

# SELECT
data = session.query(Livros).all()
print(data)

session.close()
