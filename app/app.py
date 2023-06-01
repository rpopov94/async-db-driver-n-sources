from fastapi import FastAPI

from .database.models import Base, engine, async_session, Data_1, Data_2, Data_3
from app.router import router

# Init fastapi
app = FastAPI()


# Insert data 1nd, 2nd and 3nd
async def insert_data():
    async with async_session() as session:
        data_1_list = []
        for i in range(1, 11):
            data = Data_1(id=i, name=f"Data_1 {i}")
            data_1_list.append(data)
        for i in range(31, 41):
            data = Data_1(id=i, name=f"Data_1 {i}")
            data_1_list.append(data)
        session.add_all(data_1_list)

        data_2_list = []
        for i in range(11, 21):
            data = Data_2(id=i, name=f"Data_2 {i}")
            data_2_list.append(data)
        for i in range(41, 51):
            data = Data_2(id=i, name=f"Data_2 {i}")
            data_2_list.append(data)
        session.add_all(data_2_list)

        data_3_list = []
        for i in range(21, 31):
            data = Data_3(id=i, name=f"Data_3 {i}")
            data_3_list.append(data)
        for i in range(51, 61):
            data = Data_3(id=i, name=f"Data_3 {i}")
            data_3_list.append(data)
        session.add_all(data_3_list)

        await session.commit()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    await insert_data()


@app.on_event("shutdown")
async def close():
    app.state.db.close()


app.include_router(router)
