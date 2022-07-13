from sqlalchemy import Column, Integer, TIMESTAMP, String
from task3_sql.database import BaseTable


class Operators(BaseTable):
    __tablename__ = "operators"

    endpoint_id = Column(Integer, primary_key=True)
    login_time = Column(TIMESTAMP(timezone=True))
    logout_time = Column(TIMESTAMP(timezone=True))
    operator_name = Column(String(64))
