from importlib import reload

from fastapi import FastAPI
from routers.V1 import vehicle_router
import uvicorn
from sqlmodel import SQLModel
from db.db import engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(vehicle_router.router)
app.include_router(vehicle_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)