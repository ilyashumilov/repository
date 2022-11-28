import os

from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property

DeclarativeBase = declarative_base()

db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')


class StatModel(DeclarativeBase):
    __tablename__ = 'stat'

    id = Column(Integer, primary_key=True)
    date = Column('date', Date)
    views = Column('views', Integer)
    clicks = Column('clicks', Integer)
    cost = Column('cost', Float)

def Session():
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/{db_name}', echo=True)
    DeclarativeBase.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    return session

    