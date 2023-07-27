from src.app.adapters.models import User
from src.app.interfaces import db


async def create_user(
    user_email: str,
) -> User:
    return await db.DB_GATEWAY.user.create_user(user_email)


async def get_users(
    cursor: str | None,
) -> tuple[list[User], str, bool]:
    return await db.DB_GATEWAY.user.get_users(cursor)
