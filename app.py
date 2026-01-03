from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

# Cache pour stock
CACHE_STOCK = {
    "data": None,
    "updated_at": None
}

# Cache pour weather
CACHE_WEATHER = {
    "data": None,
    "updated_at": None
}

# -------------------
# STOCK
# -------------------

# POST depuis Roblox
@app.post("/api/pvbr/stock")
async def update_stock(payload: dict):
    CACHE_STOCK["data"] = payload
    CACHE_STOCK["updated_at"] = datetime.utcnow().isoformat()
    return {"success": True}

# GET pour récupérer le stock
@app.get("/api/pvbr/stock")
async def get_stock():
    return {
        "success": True,
        "updated_at": CACHE_STOCK["updated_at"],
        "stock": CACHE_STOCK["data"]
    }

# -------------------
# WEATHER
# -------------------

# POST depuis Roblox
@app.post("/api/pvbr/weather")
async def update_weather(payload: dict):
    CACHE_WEATHER["data"] = payload
    CACHE_WEATHER["updated_at"] = datetime.utcnow().isoformat()
    return {"success": True}

# GET pour récupérer la météo
@app.get("/api/pvbr/weather")
async def get_weather():
    return {
        "success": True,
        "updated_at": CACHE_WEATHER["updated_at"],
        "weather": CACHE_WEATHER["data"]
    }
