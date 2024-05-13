from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime


Base = declarative_base()
class Gasto(Base):
    __tablename__ = 'gastos'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    valor = Column(Float)
    data = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Gasto(id={self.id}, descricao={self.descricao}, valor={self.valor}, data={self.data})>"
    
# Configuração do banco de dados
DATABASE_URL = 'postgresql://<user>:<password>@<host>:<port>/<database>'
engine = create_engine(DATABASE_URL)

# Crie as tabelas no banco de dados
Base.metadata.create_all(engine)

# Crie uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

