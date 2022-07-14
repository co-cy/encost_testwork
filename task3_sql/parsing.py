from database.tables.operators import Operators
from database.tables.reasons import Reasons
from database.tables.periods import Periods
from database.tables.energy import Energy
from database import session
from typing import Type
from csv import reader


def parsing_file(filename: str, type_table: Type[Operators | Energy | Periods | Reasons]):
    with open(filename, "r", encoding="utf-8") as file:
        file.readline()  # Skip first line with legend
        for row in reader(file, delimiter=';'):
            session.add(type_table(*row))
        session.commit()
