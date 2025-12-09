from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

fake_db = []

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.post("/items/")
async def create_item(item: Item):
    fake_db.append(item.model_dump())
    return item)

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