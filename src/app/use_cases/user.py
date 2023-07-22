import inject

from src.app.adapters.db.gateway_facade import DbGatewayFacade
from src.app.adapters.models import User


@inject.autoparams("db_facade")
async def create_user(
    user_email: str,
    db_facade: DbGatewayFacade,
) -> User:
    return await db_facade.user.create_user(user_email)


@inject.autoparams("db_facade")
async def get_users(
    db_facade: DbGatewayFacade,
):
    return await db_facade.user.get_users()
