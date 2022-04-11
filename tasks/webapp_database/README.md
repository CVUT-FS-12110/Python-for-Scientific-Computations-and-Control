# Webapp - database

Your task will be to implement two methods for our Repository class:

* update warehouse by name - shloud read out the object from database, assign it with new values and commit the changes. Should return WarehouseBto object with updated data.
* delete warehouse by name - should find object in database and delete it from it. Return WarehouseBto of deleted object.

In both implementations you should check for possible errors (missing warehouse in database). This check will not be implemented inside Repository methods but in the scope from where you call repository methods (API or database_cli). For the check it is highly recommended to use already implemented repository methods


Methods for your implementation are laready prepared in the bottom of Repository class in this file (lines 70-86): 
[repository.py](/../../blob/master/courses/E375004/webapp_database/database/repository.py)
