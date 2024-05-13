from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://root:root@database:5432/expensetrack'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()
