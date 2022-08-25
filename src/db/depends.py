from sqlalchemy.ext.asyncio import AsyncSession
from .base import AsyncSessionLocal


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as async_session:
        yield async_session