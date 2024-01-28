# app/main.py
import os
from fastapi import FastAPI
from databases import Database

app = FastAPI()

# Use environment variables for database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@postgres/mydatabase")
database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup_database():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_database():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
