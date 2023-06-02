from fastapi import FastAPI

from .database.models import Base, engine, async_session, Data_1, Data_2, Data_3
from app.router import router
from .t_data import insert_data

# Init fastapi
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    await insert_data()


@app.on_event("shutdown")
async def close():
    engine.close()


app.include_router(router)
