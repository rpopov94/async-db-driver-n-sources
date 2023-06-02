import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from app.database.models import Data_1, Data_2, Data_3
from app.app import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.mark.asyncio
async def test_get_data_success(client, mocker):
    session_mock = mocker.AsyncMock(spec=AsyncSession)

    session_mock.query.return_value.filter.return_value.\
        scalar_one.return_value = Data_1(id=1, name="Test Data")

    mocker.patch('app.main.async_session', return_value=session_mock)

    response = await client.get("/data/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Data"}


@pytest.mark.asyncio
async def test_get_data_not_found(client, mocker):
    session_mock = mocker.AsyncMock(spec=AsyncSession)

    session_mock.query.return_value.filter.\
        return_value.scalar_one.side_effect = NoResultFound()

    mocker.patch('app.main.async_session', return_value=session_mock)

    response = await client.get("/data/999")

    assert response.status_code == 200
    assert response.json() == {"message": "Data not found"}