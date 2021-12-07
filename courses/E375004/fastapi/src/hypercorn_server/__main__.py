import asyncio
import hypercorn
from hypercorn.asyncio import serve
import logging

from warehouse_app.app import app

logger = logging.getLogger()
logging.basicConfig(
    format='%(asctime)s - %(process)d-%(threadName)s-%(thread)d -- %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

app_config = hypercorn.config.Config()
app_config.use_reloader = True
asyncio.run(serve(app, app_config))
