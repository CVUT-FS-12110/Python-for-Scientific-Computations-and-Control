from database.repository import warehouse_database, ItemBto, WarehouseBto

if __name__ == "__main__":
    names = warehouse_database.warehouse_names()

    if not "ebay" in names:
        warehouse_database.create_warehouse(
            WarehouseBto(
                name="ebay",
                location="San Jose",
                capacity=5000,
                items=[ItemBto(name="laptop", amount=1000),
                       ItemBto(name="radio", amount=5)],
            )
        )
    ebay = warehouse_database.get_warehouse_by_name('ebay')
    print(ebay)

    items_of_ebay = warehouse_database.get_items_by_name('ebay')
    print(items_of_ebay)

    # YOUR DEBUG CODE HERE
