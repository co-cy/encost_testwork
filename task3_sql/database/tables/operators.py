from sqlalchemy import Column, Integer, TIMESTAMP, String
from datetime import datetime
from . import BaseTable


class Operators(BaseTable):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer)
    login_time = Column(TIMESTAMP(timezone=True))
    logout_time = Column(TIMESTAMP(timezone=True))
    operator_name = Column(String(64))

    def __init__(self, endpoint_id: str, login_time: str,  logout_time: str, operator_name: str):
        self.endpoint_id = int(endpoint_id)
        login_time = login_time[:-3] + login_time[-2:]
        logout_time = logout_time[:-3] + logout_time[-2:]
        if login_time:
            self.login_time = datetime.strptime(login_time, "%Y-%m-%d %H:%M:%S.%f %z")
        if logout_time:
            self.logout_time = datetime.strptime(logout_time, "%Y-%m-%d %H:%M:%S.%f %z")
        self.operator_name = operator_name
