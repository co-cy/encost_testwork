from parsing import parsing_energy
import database

database.init_tables()
parsing_energy("../encost_tasks/3. sql/energy.csv")
