from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

fake_db = []

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/weather")
async def get_weather():
    return {
        "location": "Berlin",
        "temperature_celsius": 24,
        "condition": "Sunny",
        "forecast": "Clear skies all day"
    }

@app.post("/items")
async def create_item(item: Item):
    fake_db.append(item.dict())
    return {"message": "Item created successfully", "item": item}

@app.get("/items")
async def read_items():
    return {"items": fake_db}