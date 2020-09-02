from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///test1.db", echo=True)
metadata = MetaData()
users_table = Table('user', metadata,
                    Column('id', Integer, primary_key=True, autoincrement=True),
                    Column('firstname', String),
                    Column('lastname', String),
                    )
metadata.create_all(engine)


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


mapper(User, users_table)

Session = sessionmaker(bind=engine)
session = Session()
session.add(User('Alex', 'Varkalov'))
session.add_all([User('Alex', 'Petrov'), User('Ann', 'Ivanova')])
session.commit()

user = session.query(User).filter_by(
    firstname='Alex',
    lastname='Varkalov',
).all()

print(user[0].firstname)
