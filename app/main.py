# app/main.py
from fastapi import FastAPI
from databases import Database

app = FastAPI()

database = Database("postgresql://myuser:mypassword@postgres/mydatabase")


@app.on_event("startup")
async def startup_database():
    await database.connect()


@app.on_event("shutdown")
async def shutdown_database():
    await database.disconnect()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
