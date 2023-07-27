from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.app.adapters.db.user.repository import UserRepository
from src.app.adapters.db.user.service import UserService
from src.app.interfaces.base import SingletonMeta


class DbGatewayFacade(SingletonMeta):
    _user_repository: UserRepository

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._user_repository = UserRepository(session_factory)

    @property
    def user(self) -> UserService:
        return UserService(self._user_repository)
