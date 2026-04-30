from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import plusbus_data as pbd
import plusbus_sql as pbsql




def booked_seats(travel_id):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.travel_id == travel_id))
    seats = 0
    for record in records:
        seats += record.travel_id
    return seats

        