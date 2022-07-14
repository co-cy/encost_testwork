from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .tables import BaseTable

engine = create_engine('sqlite:///local_test')
Session = sessionmaker(bind=engine)
BaseTable.metadata.create_all(engine)
session = Session()
