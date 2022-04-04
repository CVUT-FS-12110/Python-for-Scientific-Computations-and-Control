"""
Controller for `warehouse` part of API
"""
from typing import List
from fastapi import APIRouter, HTTPException

from database.fake_db import warehouse_database
from .dto import WarehouseDto, WarehouseItemDto

warehouse_router = APIRouter(prefix="/warehouse", tags=["warehouse"])

@warehouse_router.get("/", response_model=List[str])
def get_warehouse_names():
    """ Gets all unique names of warehouses
    Returns:
        list of names (strings), STATUS 200 (list can be empty)
    """
    return warehouse_database.warehouse_names()

@warehouse_router.post("/")
def create_new_warehouse(new_warehouse: WarehouseDto):
    """ Creates new warehouse
    
    Returns:
        None, STATUS 409 - if name does already exists
        None, STATUS 200 - if warehouse was created   
    """
    if new_warehouse.name in warehouse_database.warehouse_names():
        msg = f"Warehouse named '{new_warehouse.name}' already exists!"
        return HTTPException(status_code=409, detail=msg)
    
    warhouse_items = [{"name": i.name, "amount": i.amount}
                      for i in new_warehouse.items]

    warehouse_database.create_warehouse(
        name=new_warehouse.name,
        location=new_warehouse.location,
        capacity=new_warehouse.capacity,
        items=warhouse_items,
    )

@warehouse_router.get("/{warehouse_name}", response_model=WarehouseDto)
def get_warehouse_by_name(warehouse_name: str):
    """ Gets warehouse by name
    
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
        items=[WarehouseItemDto(name=i['name'], amount=i['amount']) for i in current_warehouse['items']]
    )
    return current_warehouse

@warehouse_router.get("/warehouse/{warehouse_name}/item", response_model=List[WarehouseItemDto])
def get_all_items_by_warehouse_name(warehouse_name: str):
    """ Gets warehouse items by warehouse name
    
    Returns:
        None, STATUS 404 - if name does not exists
        list of items (WarehouseItemDto), STATUS 200 - if warehouse exists   
    """
    items = warehouse_database.get_items_by_name(warehouse_name)

    if items is None:
        msg = f"I haven't found warehouse with name '{warehouse_name}', sorry!"
        raise HTTPException(status_code=404, detail=msg)
    
    result = [WarehouseItemDto(name=i['name'], amount=i['amount']) for i in items]
    return result

@warehouse_router.delete("/warehouse/{warehouse_name}", response_model=WarehouseDto)
def delete_warehouse_by_name(warehouse_name: str):
    """ Deletes warehouse by provided name

    Returns:
        None, STATUS 404 - if name does not exists
        deleted warehouse (WarehouseDto), STATUS 200 (that is default)
            if warehouse was deleted    
    """
    # YOUR CODE HERE
    # do not forget to implement method in `warehouse_database`
    pass

@warehouse_router.put("/warehouse/{warehouse_name}", response_model=WarehouseDto)
def update_warehouse_by_name(warehouse_name: str, updated_warehouse: WarehouseDto):
    """ Updates warehouse by provided name

    Returns:
        None, STATUS 404 - if name does not exists
        updated warehouse (WarehouseDto), STATUS 200 (that is default)
            if warehouse was updated 
    """
    # YOUR CODE HERE
    # do not forget to implement method in `warehouse_database`
    pass


