from sqlalchemy_views import CreateView
from sqlalchemy.sql import select
from sqlalchemy import Table
from . import *

period_view = Table("period_view", BaseTable)


def create_table(session):
    select([energy.Energy.endpoint_id, periods.Periods.mode_start,
            "INPUT mode_start + mode_duration", periods.Periods.mode_duration,
            periods.Periods.label, reasons.Reasons.reason, operators.Operators.operator_name])