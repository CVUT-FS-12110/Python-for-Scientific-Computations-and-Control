"""
DTOs (Data Transfer Objects) for `warehouse` controller
"""
from typing import List
from pydantic import BaseModel

class WarehouseItemDto(BaseModel):
    name: str
    amount: int

class WarehouseDto(BaseModel):
    name: str # this is our unique identifier!
    location: str
    capacity: int
    items: List[WarehouseItemDto]
