"""
Very simple API 
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/", response_model=dict)
def hello_world():
    """ This is my first endpoint """
    return {"message": "Hello world!", "note": "This is my first API endpoint."}
