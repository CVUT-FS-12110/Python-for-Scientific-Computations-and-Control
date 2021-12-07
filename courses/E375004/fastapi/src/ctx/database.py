"""
Database for warehouses
"""
import logging

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        logger.debug("Creating empty database")
        self._warehouses = {}

    def warehouse_names(self):
        return list(self._warehouses.keys())
    
    def create_warehouse(self, name: str, location: str, capacity: int):
        """ Creates new warehouse """
        self._warehouses[name] = {
            "location": location,
            "capacity": capacity,
            "items": [],
        }
    
    def get_warehouse_by_name(self, name: str):
        """ Return warehouse if exists, else returns None """
        return self._warehouses.get(name, None)


warehouse_database = Database() #this is what we are going to import
warehouse_database.create_warehouse( #create testcase we can delete it later
    name="TestWarehouse",
    location="Prague",
    capacity=1000,
)