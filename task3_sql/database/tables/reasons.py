from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime
from . import BaseTable


class Reasons(BaseTable):
    __tablename__ = "reasons"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer)
    event_time = Column(TIMESTAMP(timezone=True), index=True)
    reason = Column(String(96))

    def __init__(self, endpoint_id: str, event_time: str, reason: str):
        self.endpoint_id = int(endpoint_id)
        self.event_time = datetime.strptime(event_time + "00", "%Y-%m-%d %H:%M:%S%z")
        self.reason = reason
