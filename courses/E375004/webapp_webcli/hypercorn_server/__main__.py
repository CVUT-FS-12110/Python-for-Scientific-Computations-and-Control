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

from warehouse_app.app import app


app_config = hypercorn.config.Config()
app_config.use_reloader = True
asyncio.run(serve(app, app_config))
