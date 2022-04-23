from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

""" Database models for ORM """


class Warehouse(Base):
    __tablename__ = "warehouse"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    location = Column(String(30))
    capacity = Column(Integer)

    items = relationship("Item", back_populates="warehouse", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Warehouse(id={self.id!r}, name={self.name!r}, location={self.location!r}, capacity={self.capacity!r})"


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)

    warehouse_id = Column(Integer, ForeignKey("warehouse.id"), nullable=False)

    warehouse = relationship("Warehouse", back_populates="items")

    def __repr__(self):
        return f"Item(id={self.id!r}, name={self.name!r}, count={self.count!r})"
