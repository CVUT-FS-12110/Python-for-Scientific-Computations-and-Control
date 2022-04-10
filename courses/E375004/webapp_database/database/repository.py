from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import sessionmaker

from .models import Base, Warehouse, Item
from .business_objects import ItemBto, WarehouseBto


class Repository:

    def __init__(self):
        """ Repository initialization """

        self._engine = create_engine("sqlite:///./database.db", echo=True, future=True)

        self._Session = sessionmaker(bind=self._engine)

        Base.metadata.create_all(self._engine)

    def warehouse_names(self) -> list[str]:
        """ Gets all unique names of warehouses
        Returns:
            list of names (strings)
        """
        with self._Session() as session:
            stmt = select(Warehouse)

            res = session.scalars(stmt)

            return [w.name for w in res]

    def create_warehouse(self, warehouse_bto: WarehouseBto) -> None:
        """ Creates new warehouse

        Returns:
            None
        """
        with self._Session() as session:
            warehouse = warehouse_bto.model()

            session.add(warehouse)
            session.commit()

    def get_warehouse_by_name(self, name: str) -> WarehouseBto:
        """ Gets warehouse by name

        Returns:
            selected warehouse (WarehouseBto)
        """
        with self._Session() as session:
            stmt = select(Warehouse).where(Warehouse.name == name)
            warehouse = session.scalars(stmt).one()

            warehouse_bto = WarehouseBto.bto(warehouse)
            return warehouse_bto

    def get_items_by_name(self, name: str) -> list[ItemBto]:
        """ Gets warehouse items by warehouse name

        Returns:
            list of items (ItemBto)
        """
        with self._Session() as session:
            stmt = select(Item).join(Item.warehouse).where(Warehouse.name == name)
            res = session.scalars(stmt)

            items = [ItemBto.bto(item) for item in res]

            return items

    def delete_warehouse_by_name(self, name: str) -> WarehouseBto:
        """ Delete warehouse by its name

        Returns:
            deleted warehouse (WarehouseBto)
        """
        # YOUR CODE HERE
        pass

    def update_warehouse_by_name(self, warehouse_bto: WarehouseBto) -> WarehouseBto:
        """ Update warehouse with new data from WarehouseBto object

        Returns:
            updated warehouse (WarehouseBto)
        """
        # YOUR CODE HERE
        pass


warehouse_database = Repository()
