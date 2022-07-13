from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .tables import BaseTable

engine = create_engine('sqlite:///college.db')
Session = sessionmaker(bind=engine)
session = Session()
BaseTable.metadata.create_all(engine)
