"""
DEFINE MODEL
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)

    def __repr__(self):
        return f"Person(id={self.id!r}, name={self.name!r})"


"""
CONNECT DATABASE
"""
from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True, future=True)


"""
CREATE DATABASE
"""
Base.metadata.create_all(engine)


"""
PREPARE SESSION-MAKER
"""
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)


"""
BASIC OPERATIONS - Insert
"""
with Session() as session:
    person = Person(
        name="Alice",
    )
    session.add(person)

    person = Person(
        name="Bob",
    )
    session.add(person)

    session.commit()

    person = Person(
        name="Carlos",
    )
    session.add(person)


"""
BASIC OPERATIONS - Read
"""
from sqlalchemy import select
with Session() as session:
    stmt = select(Person)

    for person in session.execute(stmt).scalars():
        print(person)


"""
BASIC OPERATIONS - Update
"""
with Session() as session:
    stmt = select(Person).where(Person.name == "Alice")
    person = session.scalars(stmt).one()

    person.name = "Arnold"

    session.commit()


"""
BASIC OPERATIONS - Delete
"""
with Session() as session:
    person = session.get(Person, 1)

    session.delete(person)
    session.commit()

