from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Db:
    def __init__(self, url: str) -> None:
        self._engine = create_async_engine(
            url,
            echo=True,
        )

    def get_session_factory(self) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(self._engine, expire_on_commit=False)

    async def __delete__(self) -> None:
        if self._engine:
            await self._engine.dispose()
