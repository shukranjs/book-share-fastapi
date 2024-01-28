# app/core/database.py
import os
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@postgres/mydatabase")
database = Database(DATABASE_URL)

async def connect_to_database():
    await database.connect()

async def close_database_connection():
    await database.disconnect()
