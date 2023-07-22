import os

import inject
from dotenv import load_dotenv
from fastapi import FastAPI

from src.app.adapters.db.gateway_facade import DbGatewayFacade
from src.app.adapters.db.sqlachemy import Db
from src.app.adapters.http import endpoints


def configure_db(binder: inject.Binder):
    url = os.getenv("DATABASE_URL")
    db = Db(url=url.replace("postgresql:", "postgresql+asyncpg:"))
    binder.bind(
        DbGatewayFacade, DbGatewayFacade(session_factory=db.get_session_factory())
    )


def create_app() -> FastAPI:
    load_dotenv()
    inject.configure(configure_db)

    app = FastAPI()
    app.include_router(endpoints.router)
    return app
