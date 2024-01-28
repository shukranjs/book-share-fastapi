# app/main.py
from fastapi import FastAPI
from app.core.database import connect_to_database, close_database_connection

app = FastAPI()

@app.on_event("startup")
async def startup_app():
    await connect_to_database()

@app.on_event("shutdown")
async def shutdown_app():
    await close_database_connection()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
