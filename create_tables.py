import asyncio
from app.core.database import engine
from app.models.job import JobDB
from sqlmodel import SQLModel

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Таблицы успешно созданы!")

asyncio.run(main())