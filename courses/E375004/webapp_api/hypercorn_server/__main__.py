"""
Hypercorn ASGI
--------------
Python module for serving our applications via:
```
python -m hypercorn_server
```
"""
import asyncio

import hypercorn
from hypercorn.asyncio import serve

# from warehouse_app.helloworld_app import app
from warehouse_app.app import app

print("I am about to serve you web application!")

app_config = hypercorn.config.Config()
app_config.use_reloader = True
asyncio.run(serve(app, app_config))