from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse
from pydantic import BaseModel
import sqlite3

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/my_endpoint/")
async def my_new_endpoint():
    return {"message": "Hello World. I have created this endpoint myself"}


@app.get("/plaintext/", response_class=PlainTextResponse)
async def plain_text():
    return "Hello World\nI have created this endpoint myself"


@app.get("/html/", response_class=HTMLResponse)
async def html():
    return "<h1>Hello World</h1><p>I have created this endpoint myself</p>"


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/greetings")
async def read_item(name: str = "Alice"):
    return f"The name is {name}"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return f"Item created: {item}"


conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()
conn.close()


@app.get("/users")
async def get_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users')
    users_list = c.fetchall()

    return users_list


class User(BaseModel):
    name: str
    age: int


@app.post("/users")
async def create_user(user: User):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (user.name, user.age))

    conn.commit()
    conn.close()

    return f"Created new user: {user}"
