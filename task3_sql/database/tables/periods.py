from sqlalchemy import Column, Integer, TIMESTAMP, String
from task3_sql.database import BaseTable


class Periods(BaseTable):
    __tablename__ = "periods"

    endpoint_id = Column(Integer, primary_key=True)
    mode_start = Column(TIMESTAMP(timezone=True))
    mode_duration = Column(Integer)
    label = Column(String(32))
