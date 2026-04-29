from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import plusbus_data as pbd
import plusbus_sql as pbsql




def booked_bus(travel):
    with Session(pbsql.engine) as session:
        