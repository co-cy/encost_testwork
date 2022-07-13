from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///college.db', echo=True)
BaseTable = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def init_tables():
    from . import tables

    BaseTable.metadata.create_all(engine)
