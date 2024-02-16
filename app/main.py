from fastapi import FastAPI

from app.database import Base, engine
from app.auth.routers import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["home"])
def home():
    return {"data": "welcome home!"}


app.include_router(auth_router)
