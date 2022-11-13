from infra.configs.base import Base
from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from infra.entities.country import Country


class State(Base):
    __tablename__ = "tb_state"

    id_state = Column(BigInteger, primary_key=True)
    initials = Column(String, nullable=False)
    ibge_code = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    dt_create = Column(DateTime, nullable=False)
    dt_update = Column(DateTime, nullable=False)
    id_country = Column(BigInteger, ForeignKey("tb_country.id_country"))

    def __repr__(self):
        return f"""State(
                    id_state={self.id_state},
                    ibge_code={self.ibge_code},
                    initials={self.initials},
                    name={self.name},
                    dt_create={self.dt_create},
                    dt_update={self.dt_update},
                    id_country={self.id_country}
                )"""
