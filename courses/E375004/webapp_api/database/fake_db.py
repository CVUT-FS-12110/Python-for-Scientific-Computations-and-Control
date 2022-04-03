"""
Fake Database for warehouse web application
"""
from typing import List


class WarehouseDatabase:

    def __init__(self):
        self._warehouses = []

    def warehouse_names(self) -> List[str]:
        return [w['name'] for w in self._warehouses]
    
    def create_warehouse(self, name: str, location: str, capacity: int,
                         items: list):
        new_warehouse = {
            "name": name,
            "location": location,
            "capacity": capacity,
            "items": items,
        }
        self._warehouses.append(new_warehouse)

    def get_warehouse_by_name(self, name: str):
        result = None
        for w in self._warehouses:
            if w['name'] == name:
                result = w
                break
        return result

warehouse_database = WarehouseDatabase()
