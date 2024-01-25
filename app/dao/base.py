from app.database import async_session_maker
from sqlalchemy import insert, select

class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id= model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        

    @classmethod
    async def add(cls, email: str, hashed_password: str):
        # Использование асинхронного менеджера контекста для сессии
        async with async_session_maker() as session:
            # Формирование и выполнение SQL-запроса на добавление пользователя
            query = insert(cls.model).values(email=email, hashed_password=hashed_password)
            await session.execute(query)
            # Фиксация изменений в базе данных
            await session.commit()
