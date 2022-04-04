"""
Warehouse application
"""
from fastapi import FastAPI

from warehouse_app.warehouse.controller import warehouse_router

app = FastAPI(title="Warehouse API")

app.include_router(warehouse_router)

@app.get("/")
def root():
    return {"message": "Hello, this route is useless for now!"}