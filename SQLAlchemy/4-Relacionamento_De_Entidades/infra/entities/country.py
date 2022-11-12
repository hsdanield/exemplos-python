from infra.configs.base import Base
from sqlalchemy import Column, String, BigInteger, DateTime


class Country(Base):
    __tablename__ = "tb_country"

    id_country = Column(
        BigInteger,
        primary_key=True,
    )
    initials = Column(String, nullable=False)
    name = Column(String, nullable=False)
    dt_create = Column(DateTime, nullable=False)
    dt_update = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"""City(id_country={self.id_country},
                    initials={self.initials},
                    name={self.name},
                    dt_create={self.dt_create},
                    dt_update={self.dt_create})
                """
