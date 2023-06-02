from app.database.models import Data_3, Data_2, Data_1, async_session


# Insert data 1nd, 2nd and 3n
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