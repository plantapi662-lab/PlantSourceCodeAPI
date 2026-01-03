from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

CACHE = {
    "data": None,
    "updated_at": None
}

# POST depuis Roblox
@app.post("/api/pvbr/stock")
async def update_stock(payload: dict):
    CACHE["data"] = payload
    CACHE["updated_at"] = datetime.utcnow().isoformat()
    return {"success": True}

# GET pour récupérer le stock
@app.get("/api/pvbr/stock")
async def get_stock():
    return {
        "success": True,
        "updated_at": CACHE["updated_at"],
        "stock": CACHE["data"]
    }
