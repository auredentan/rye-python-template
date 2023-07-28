import asyncpg
from sqlakeyset import ConfigurationError, custom_bookmark_type
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.app.interfaces.base import SingletonMeta


class SqlalchemyBase(DeclarativeBase):
    pass


class Db(SingletonMeta):
    def __init__(self, url: str) -> None:
        self._engine = create_async_engine(
            url,
            echo=True,
        )
        self.register_custom_bookmark()

    def get_session_factory(self) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(self._engine, expire_on_commit=False)

    async def __delete__(self) -> None:
        if self._engine:
            await self._engine.dispose()

    def register_custom_bookmark(self) -> None:
        def ser_uuid(uid: asyncpg.pgproto.pgproto.UUID) -> str:  # type: ignore
            return str(uid)

        def deser_uuid(uid: str) -> asyncpg.pgproto.pgproto.UUID:  # type: ignore
            return asyncpg.pgproto.pgproto.UUID(uid)  # type: ignore

        try:
            custom_bookmark_type(
                type=asyncpg.pgproto.pgproto.UUID,  # type: ignore
                code="uuidasyncpg",
                deserializer=deser_uuid,
                serializer=ser_uuid,
            )
        except ConfigurationError:
            pass
