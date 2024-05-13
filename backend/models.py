from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Gasto(Base):
    __tablename__ = 'gastos'

    gasto_id = Column(Integer, primary_key=True)
    descricao = Column(String)
    valor = Column(Float)
    data = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Gasto(id={self.gasto_id}, descricao={self.descricao}, valor={self.valor}, data={self.data})>"
