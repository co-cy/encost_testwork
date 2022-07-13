from sqlalchemy import Column, Integer, TIMESTAMP, String
from . import BaseTable


class Operators(BaseTable):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer)
    login_time = Column(TIMESTAMP(timezone=True))
    logout_time = Column(TIMESTAMP(timezone=True))
    operator_name = Column(String(64))
