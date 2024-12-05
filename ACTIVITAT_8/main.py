from fastapi import FastAPI, HTTPException
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
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.dict()
    return {"id": item_id, "item": item}
