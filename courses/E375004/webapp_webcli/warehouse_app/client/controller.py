"""
Client
"""
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

import requests

client_router = APIRouter(prefix="", tags=["web_client"])

templates = Jinja2Templates(directory="warehouse_app/client/templates")

HOST = 'http://127.0.0.1:8000/'


@client_router.get("/example", response_class=HTMLResponse)
def list_warehouses(request: Request):
    """ Example """

    return templates.TemplateResponse("example.html", {"request": request})


@client_router.get("/warehouse_list", response_class=HTMLResponse)
def list_warehouses(request: Request):
    """ List of all warehouses """

    path = 'warehouse/warehouse/'

    response = requests.get(url=HOST+path)
    if not response.ok:
        return templates.TemplateResponse("error.html", {"request": request, "status_code": response.status_code, "error_message": response.json()['detail']})

    return templates.TemplateResponse("warehouse_list.html", {"request": request, "warehouses": response.json()})


@client_router.get("/warehouse_add", response_class=HTMLResponse)
def add_warehouses(request: Request):
    """ Add a new warehouse to database """

    return templates.TemplateResponse("warehouse_add.html", {"request": request})


@client_router.post("/warehouse_add", response_class=HTMLResponse, status_code=200)
def add_warehouses(request: Request, name: str = Form(...), location: str = Form(...), capacity: str = Form(...)):
    """ Add a new warehouse to database """

    path = 'warehouse/'

    data = {
        'name': name,
        'location': location,
        'capacity': capacity,
        'items': []
    }

    response = requests.post(url=HOST+path, json=data)

    if not response.ok:
        return templates.TemplateResponse("error.html", {"request": request, "status_code": response.status_code, "error_message": response.json()['detail']})

    return templates.TemplateResponse("warehouse_add.html", {"request": request})


@client_router.get("/item_list", response_class=HTMLResponse)
def list_items(request: Request):
    """ List of all items """

    # TODO: YOUR CODE HERE

    return templates.TemplateResponse("item_list.html", {"request": request})


@client_router.get("/item_add", response_class=HTMLResponse)
def add_items(request: Request):
    """ Add a new item to database """

    # TODO: YOUR CODE HERE

    return templates.TemplateResponse("item_add.html", {"request": request})


@client_router.post("/item_add", response_class=HTMLResponse)
def add_items(request: Request, name: str = Form(...), location: str = Form(...), capacity: str = Form(...)):
    """ Add a new item to database """

    # TODO: YOUR CODE HERE

    return templates.TemplateResponse("item_add.html", {"request": request})
