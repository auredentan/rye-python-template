from src.app.adapters.models import User

from .repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    async def create_user(self, email: str) -> User:
        return await self._repository.create_user(email)

    async def get_users(self) -> list[User]:
        return await self._repository.get_users()
