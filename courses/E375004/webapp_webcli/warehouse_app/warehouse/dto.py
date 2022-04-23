"""
DTOs (Data Transfer Objects) for `warehouse` controller
"""
from typing import List
from pydantic import BaseModel

class WarehouseItemDto(BaseModel):
    name: str
    amount: int

class WarehouseDto(BaseModel):
    name: str
    location: str
    capacity: int
    items: List[WarehouseItemDto]
