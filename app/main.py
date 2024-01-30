from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .api.helpers.database import get_db, create_all

app = FastAPI()


@app.on_event("startup")
async def startup_app(db: Session = Depends(get_db)):
    create_all()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
