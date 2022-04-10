### define example model

```Python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    def __repr__(self):
        return f"Person(id={self.id!r}, name={self.name!r})"
```

### connect database
```Python
from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True, future=True)
```

### create database
```Python
Base.metadata.create_all(engine)
```

### insert
```Python
with Session() as session:
    person = Person(
        name="Alice",
    )
    session.add(person)
    session.commit()
```

### read
```Python
from sqlalchemy import select
with Session() as session:
    stmt = select(Person)

    for person in session.execute(stmt).scalars():
        print(person)
```

### update
```Python
with Session() as session:
    stmt = select(Person).where(Person.name == "Alice")
    
    person = session.scalars(stmt).one()
    person.name = "Arnold"
    
    session.commit()
```

### delete
```Python
with Session() as session:    
    person = session.get(Person, 1)
    
    session.delete(person)
    session.commit()
```
