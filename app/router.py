from fastapi import APIRouter, Depends
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.models import async_session, Data_1, Data_2, Data_3

router = APIRouter()


# Init session
def get_session():
    session = async_session()
    try:
        yield session
    finally:
        session.close()


@router.get("/data/{id}", response_model=[Data_1, Data_2, Data_3])
async def get_data(id: int, session: AsyncSession = Depends(async_session)):
    try:
        if 1 <= id <= 10 or 31 <= id <= 40:
            result = await session.query(Data_1) \
                .filter(Data_1.id == id)
            data = result.scalar_one()
            return data
        elif 11 <= id <= 20 or 41 <= id <= 50:
            result = await session.query(Data_2) \
                .filter(Data_2.id == id)
            data = result.scalar_one()
            return data
        elif 21 <= id <= 30 or 51 <= id < 60:
            result = await session.query(Data_3) \
                .filter(Data_3.id == id)
            data = result.scalar_one()
            return data
    except NoResultFound:
        return {"message": "Data not found"}

