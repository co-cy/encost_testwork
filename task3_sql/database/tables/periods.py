from sqlalchemy import Column, Integer, TIMESTAMP, String
from . import BaseTable


class Periods(BaseTable):
    __tablename__ = "periods"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer)
    mode_start = Column(TIMESTAMP(timezone=True))
    mode_duration = Column(Integer)
    label = Column(String(32))
