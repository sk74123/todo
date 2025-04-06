from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/todo_db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()

@app.get("/health")
async def health_check():
    async with async_session() as session:
        result = await session.execute(text("SELECT 1"))
        return {"status": "ok", "db_check": result.scalar()}
