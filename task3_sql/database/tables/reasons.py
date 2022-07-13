from sqlalchemy import Column, Integer, String, TIMESTAMP
from task3_sql.database import BaseTable


class Reasons(BaseTable):
    __tablename__ = "reasons"

    endpoint_id = Column(Integer, primary_key=True)
    event_time = Column(TIMESTAMP(timezone=True), index=True)
    reason = Column(String(96))
