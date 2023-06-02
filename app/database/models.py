import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs


# load enviroments
load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")


# define models
class Base(AsyncAttrs, DeclarativeBase):
    pass


class Data_1(Base):
    __tablename__ = "data_1"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))


class Data_2(Base):
    __tablename__ = "data_2"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))


class Data_3(Base):
    __tablename__ = "data_3"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))


# Create engine
engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)
