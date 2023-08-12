from fastapi import APIRouter, Request, Response

from src.app.adapters.models import User
from src.app.interfaces import templates
from src.app.use_cases.user import create_user, get_users

router = APIRouter()


@router.get("/health")
async def health() -> str:
    return "iamok"


@router.get("/createUser", response_model=User)
async def index(email: str) -> User:
    return await create_user(user_email=email)


@router.get(path="/users", response_model=dict)
async def users(cursor: str | None = None) -> dict:
    (users, cursor, more) = await get_users(cursor)
    return {"users": users, "cursor": cursor, "more": more}


@router.get("/")
def home_page(request: Request) -> Response:
    return templates.HTMX_TEMPLATER.build_response("index.html", {"request": request})
