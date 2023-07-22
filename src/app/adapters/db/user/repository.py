from typing import cast
from uuid import uuid4

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.adapters.db.base_repository import BaseRepository
from src.app.adapters.db.user import table as sql
from src.app.adapters.models import User


class UserRepository(BaseRepository):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self.session_factory = session_factory

    def to_dto(self, sql_item: sql.User) -> User:
        return User(
            id=sql_item.id,
            email=sql_item.email,
        )

    async def create_user(self, email: str) -> User:
        query = insert(sql.User).returning(sql.User)
        async with self.session_factory() as s:
            user = await s.execute(
                statement=query, params=[{"id": uuid4(), "email": email}]
            )
            returned_user = user.scalars().one()
            await s.commit()
            return self.to_dto(returned_user)

    async def get_users(self) -> list[User]:
        query = select(sql.User)
        async with self.session_factory() as s:
            user = await s.execute(statement=query)
            returned_users = user.scalars().all()
            await s.commit()
            return [self.to_dto(returned_user) for returned_user in returned_users]
