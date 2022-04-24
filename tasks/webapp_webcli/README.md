# Webapp - database

Your task will be to implement, as we did for warehouse, the 
same functionality also for items. That means to create two pages **item_list** and **item_add**:

* **item_list** - page will show the list of all items (item name, item amount and name of their warehouse for each of them)
* **item_add** - page will be a form which allows the user to add a new item into database. Form will be accepting values: item name, item amount and name of the warehouse).
    * (optional = 2 extra points) In case item already exists in selected warehouse modify its amount instead of adding it to list.

Functions for your implementation are already prepared in the bottom of client/controller.py in this file (lines 66-90): 
[controller.py](/../../blob/master/courses/E375004/webapp_webcli/warehouse_app/client/controller.py)

HTML files are already prepared in: [templates](/../../blob/master/courses/E375004/webapp_webcli/warehouse_app/client/templates)