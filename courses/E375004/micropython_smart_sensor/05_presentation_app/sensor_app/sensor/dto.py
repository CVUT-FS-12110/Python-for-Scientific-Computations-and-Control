"""
DTOs (Data Transfer Objects) for `sensor` controller
"""
from typing import List
from pydantic import BaseModel

class MeasurementDto(BaseModel):
    name: str
    temperature: float
