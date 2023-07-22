from typing import Annotated, Union

from fastapi import APIRouter
from fastapi.params import Body

from src.app.adapters.models import EventMachin, EventTruc, User
from src.app.use_cases.user import create_user, get_users

router = APIRouter()


@router.get("/createUser", response_model=User)
async def index(email: str) -> User:
    return await create_user(user_email=email)


@router.get(path="/users", response_model=list[User])
async def users() -> list[User]:
    return await get_users()


@router.post("/events")
async def events(
    event: Annotated[Union[EventTruc, EventMachin], Body(discriminator="type")]
) -> str:
    print(event)
    return ""
