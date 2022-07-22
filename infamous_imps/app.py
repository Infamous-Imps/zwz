from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """Item class"""

    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    """Base function"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item):
    """Read item"""
    return {"item_id": item_id, "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Add item"""
    return {"item_name": item.name, "item_id": item_id}
