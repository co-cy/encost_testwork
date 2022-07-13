from sqlalchemy import Column, Integer, Float, TIMESTAMP
from datetime import datetime
from . import BaseTable


class Energy(BaseTable):
    __tablename__ = "energy"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer)
    event_time = Column(TIMESTAMP(timezone=True))
    kwh = Column(Float)

    def __init__(self, endpoint_id: str, event_time: str, kwh: str):
        self.endpoint_id = int(endpoint_id)
        self.event_time = datetime.strptime(event_time + "00", "%Y-%m-%d %H:%M:%S%z")
        self.kwh = float(kwh)
