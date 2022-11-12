from infra.configs.base import Base
from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey


class State(Base):
    __tablename__ = "tb_state"

    id_state = Column(BigInteger, primary_key=True)
    ibge_code = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    dt_create = Column(DateTime, nuallble=False)
    dt_update = Column(DateTime, nuallble=False)
    id_country = Column(BigInteger, ForeignKey("tb_country.id_country"))

    def __repr__(self):
        return f"""State(
                    id_state={self.id_state},
                    ibge_code={self.ibge_code},
                    dt_create={self.dt_create},
                    dt_update={self.dt_update},
                    id_country={self.id_country}
                )"""
