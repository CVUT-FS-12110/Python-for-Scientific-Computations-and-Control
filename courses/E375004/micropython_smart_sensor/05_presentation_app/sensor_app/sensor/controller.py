"""
Controller for `warehouse` part of API
"""
from typing import List
from fastapi import APIRouter, HTTPException
from datetime import datetime

from .dto import MeasurementDto

sensor_router = APIRouter(prefix="/sensor", tags=["warehouse"])


@sensor_router.post("/data")
async def accept_data(new_measurement: MeasurementDto):
    time = datetime.now()
    print(f"{time.strftime('%d/%m/%Y %H:%M:%S')} - {new_measurement.name}: temperature={new_measurement.temperature}°C")
    return {"message":"Data accepted"}
