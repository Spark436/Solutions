from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer, Date  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select
from dateutil import parser

Database = 'sqlite:///plusbus.db'
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    contact_info = Column(String)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Customer({self.id=}    {self.last_name=}    {self.contact_info=})"

    def convert_to_tuple(self):  # Convert Customer to tuple
        return self.id, self.last_name, self.contact_info

    def valid(self):  # is this object a valid record of a customer?
        return self.contact_info != "deleted"

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Customer
        person = Customer(id=tuple_[0], last_name=tuple_[1], contact_info=tuple_[2])
        return person

class Travel(Base):
    __tablename__ = "travels"
    id = Column(Integer, primary_key=True)
    route = Column(String)
    date = Column(Date)
    capacity = Column(Integer)

    def __repr__(self):
        return f"Travel({self.id=} {self.route=} {self.date=} {self.capacity=})"

    def convert_to_tuple(self):
        return self.id, self.route, self.date, self.capacity

    def valid(self):
        return self.capacity >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        date = parser.parse(tuple_[2])
        capacity = int(tuple_[3])
        travel_plan = Travel(id=tuple_[0], route=tuple_[1], date=date, capacity=capacity)
        return travel_plan

def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Customer
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

# print(select_all(Customer))
# print(Customer.convert_from_tuple((12, "test", 17)))
print(get_record(Customer, 1))