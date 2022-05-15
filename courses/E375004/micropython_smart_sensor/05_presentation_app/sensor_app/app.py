"""
Sensor application
"""
from fastapi import FastAPI

from sensor_app.sensor.controller import sensor_router

app = FastAPI(title="Sensor API")

app.include_router(sensor_router)

@app.get("/")
async def root():
    print("root endpoint")
    return {"message": "Hello, this route is useless for now!"}