"""
DTOs (Data Transfer Objects) for `warehouse` controller
"""
from typing import List
from pydantic import BaseModel
from database.repository import WarehouseBto, ItemBto


class WarehouseItemDto(BaseModel):
    name: str
    amount: int

    def model(self) -> ItemBto:
        item = ItemBto(
            name=self.name,
            amount=self.amount,
        )
        return item

    @staticmethod
    def dto(item: ItemBto) -> 'WarehouseItemDto':
        return WarehouseItemDto(
            name=item.name,
            amount=item.amount,
        )


class WarehouseDto(BaseModel):
    name: str
    location: str
    capacity: int
    items: List[WarehouseItemDto]

    def model(self) -> WarehouseBto:
        warehouse = WarehouseBto(
            name=self.name,
            location=self.location,
            capacity=self.capacity,
            items=[item.model() for item in self.items],
        )
        return warehouse

    @staticmethod
    def dto(warehouse: WarehouseBto) -> 'WarehouseDto':
        return WarehouseDto(
            name=warehouse.name,
            location=warehouse.location,
            capacity=warehouse.capacity,
            items=[WarehouseItemDto.dto(item) for item in warehouse.items]
        )
