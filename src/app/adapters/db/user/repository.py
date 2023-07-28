from uuid import uuid4

from sqlakeyset.asyncio import select_page
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

    async def get_users(self, cursor: str | None) -> tuple[list[User], str, bool]:
        query = select(sql.User).order_by(sql.User.id)
        async with self.session_factory() as s:
            page = await select_page(s, query, per_page=2, page=cursor)
            return (
                [self.to_dto(row[0]) for (_, row) in page.paging.items()],
                page.paging.bookmark_next,
                page.paging.has_next,
            )
