from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = 'postgresql://root:root@database:5432/expensetrack?client_encoding=utf8'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)  # Esta linha cria as tabelas no banco de dados
