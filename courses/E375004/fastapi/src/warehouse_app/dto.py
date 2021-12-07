""" Data Transfer Objects """
from pydantic import BaseModel

class WarehouseDto(BaseModel):
    name: str # this is our unique identifier!
    location: str
    capacity: int