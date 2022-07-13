from sqlalchemy import Column, Integer, String, TIMESTAMP
from . import BaseTable


class Reasons(BaseTable):
    __tablename__ = "reasons"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer)
    event_time = Column(TIMESTAMP(timezone=True), index=True)
    reason = Column(String(96))
