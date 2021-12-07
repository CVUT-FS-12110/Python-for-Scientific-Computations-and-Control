"""
App Fastapi implementation
"""
from fastapi import FastAPI, HTTPException
import logging
from typing import List
from ctx.database import warehouse_database
from .dto import WarehouseDto

logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/warehouse", response_model=List[str])
def get_warehouse_mastertable():
    """ Gets all unique names of warehouses

    Returns:
        list of names (strings), STATUS 200 (list can be empty)
    """
    return warehouse_database.warehouse_names()

@app.post("/warehouse")
def create_new_warehouse(new_warehouse: WarehouseDto):
    """ Creates new warehouse
    
    Returns:
        None, STATUS 404 - if name does not exists
        None, STATUS 200 - if warehouse was created   
    """
    if new_warehouse.name in warehouse_database.warehouse_names():
        msg = f"Warehouse named '{new_warehouse.name}' already exists!"
        return HTTPException(status_code=409, detail=msg)

    warehouse_database.create_warehouse(
        name=new_warehouse.name,
        location=new_warehouse.location,
        capacity=new_warehouse.capacity,
    )

@app.get("/warehouse/{warehouse_name}", response_model=WarehouseDto)
def get_warehouse_by_name(warehouse_name: str):
    """ Creates new warehouse
    
    Returns:
        None, STATUS 404 - if name does not exists
        selected warehouse (WarehouseDto), STATUS 200 - if warehouse exists   
    """
    current_warehouse = warehouse_database.get_warehouse_by_name(warehouse_name)

    if current_warehouse is None:
        msg = f"I haven't found warehouse with name '{warehouse_name}', sorry!"
        raise HTTPException(status_code=404, detail=msg)

    current_warehouse = WarehouseDto(
        name=warehouse_name,
        location=current_warehouse["location"],
        capacity=current_warehouse["capacity"],
    )
    return current_warehouse

# PART - HOMEWORK

@app.delete("/warehouse/{warehouse_name}", response_model=WarehouseDto)
def delete_warehouse_by_name(warehouse_name: str):
    """ Deletes warehouse by provided name

    Returns:
        None, STATUS 404 - if name does not exists
        deleted warehouse (WarehouseDto), STATUS 200 (that is default) - if warehouse was deleted    
    """
    # YOUR CODE HERE
    pass


@app.put("/warehouse/{warehouse_name}", response_model=WarehouseDto)
def update_warehouse_by_name(warehouse_name: str):
    """ Updates warehouse by provided name

    Returns:
        None, STATUS 404 - if name does not exists
        updated warehouse (WarehouseDto), STATUS 200 (that is default) - if warehouse was updated 
    """
    # YOUR CODE HERE
    pass




