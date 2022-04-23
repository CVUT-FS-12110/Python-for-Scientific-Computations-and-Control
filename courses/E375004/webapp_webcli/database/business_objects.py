from pydantic import BaseModel

from .models import Warehouse, Item

""" Inter layer objects for transfer of data between database and api controller """


class ItemBto(BaseModel):
    name: str = None
    amount: int = None

    def model(self) -> Item:
        item = Item(
            name=self.name,
            amount=self.amount,
        )
        return item

    @staticmethod
    def bto(item: Item) -> 'ItemBto':
        return ItemBto(
            name=item.name,
            amount=item.amount,
        )


class WarehouseBto(BaseModel):
    name: str
    location: str
    capacity: int
    items: list[ItemBto]

    def model(self) -> Warehouse:
        warehouse = Warehouse(
            name=self.name,
            location=self.location,
            capacity=self.capacity,
            items=[item.model() for item in self.items],
        )
        return warehouse

    @staticmethod
    def bto(warehouse: Warehouse) -> 'WarehouseBto':
        return WarehouseBto(
            name=warehouse.name,
            location=warehouse.location,
            capacity=warehouse.capacity,
            items=[ItemBto.bto(item) for item in warehouse.items]
        )
