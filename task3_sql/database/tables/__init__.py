from sqlalchemy.orm import declarative_base
BaseTable = declarative_base()

from . import operators
from . import reasons
from . import periods
from . import energy
