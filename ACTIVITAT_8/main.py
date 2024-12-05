from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = {}


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    stock: int
    is_available: bool = True  

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.dict()
    return {"id": item_id, "item": item}
