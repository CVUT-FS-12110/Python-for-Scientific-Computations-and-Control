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

from sensor_app.app import app

app_config = hypercorn.config.Config()
app_config.use_reloader = True
app_config.bind = ["0.0.0.0:10070"]
asyncio.run(serve(app, app_config))