from infra.configs.base import Base
from sqlalchemy import Column, String, Integer


class Livros(Base):
    __tablename__ = "livros"

    autor = Column(String, nullable=False)
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme(titulo={self.titulo}, autor={self.autor}, genero={self.genero}, ano={self.ano})"
