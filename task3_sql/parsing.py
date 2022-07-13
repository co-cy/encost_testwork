from database.tables.energy import Energy
from database import session
from csv import reader


def parsing_energy(filename: str):
    with open(filename, "r") as file:
        file.readline()
        for row in reader(file, delimiter=';'):
            energy = Energy(*row)
            session.add(energy)
        session.commit()