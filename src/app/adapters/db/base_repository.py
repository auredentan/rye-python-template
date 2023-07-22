from typing import AsyncIterator

from fastapi.concurrency import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class BaseRepository:
    session_factory: async_sessionmaker[AsyncSession]

    @asynccontextmanager
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        yield self.session_factory()
