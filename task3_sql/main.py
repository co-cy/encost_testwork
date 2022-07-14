from database.tables.operators import Operators
from database.tables.reasons import Reasons
from database.tables.periods import Periods
from database.tables.energy import Energy
from parsing import parsing_file

parsing_file("../encost_tasks/3. sql/operators.csv", Operators)
parsing_file("../encost_tasks/3. sql/reasons.csv", Reasons)
parsing_file("../encost_tasks/3. sql/periods.csv", Periods)
parsing_file("../encost_tasks/3. sql/energy.csv", Energy)
