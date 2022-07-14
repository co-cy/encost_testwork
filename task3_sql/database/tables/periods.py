from sqlalchemy import Column, Integer, TIMESTAMP, String
from datetime import datetime
from . import BaseTable


class Periods(BaseTable):
    __tablename__ = "periods"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer)
    mode_start = Column(TIMESTAMP(timezone=True))
    mode_duration = Column(Integer)
    label = Column(String(32))

    def __init__(self, endpoint_id: str, mode_start: str,  mode_duration: str, label: str):
        self.endpoint_id = int(endpoint_id)
        self.mode_start = datetime.strptime(mode_start + "00", "%Y-%m-%d %H:%M:%S%z")
        self.mode_duration = int(mode_duration)
        self.label = label
