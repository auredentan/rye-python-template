import os
import pathlib

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.app.adapters.db.gateway_facade import DbGatewayFacade
from src.app.adapters.db.sqlachemy import Db
from src.app.adapters.http import endpoints
from src.app.adapters.http.htmx import HtmxTemplater
from src.app.interfaces import db, templates


def configure_db() -> None:
    url = os.getenv("DATABASE_URL", "")
    db_instance = Db(url=url.replace("postgresql:", "postgresql+asyncpg:"))
    db.DB = db_instance
    db.DB_GATEWAY = DbGatewayFacade(session_factory=db_instance.get_session_factory())


def configure_static(app: FastAPI) -> None:
    current_dir = pathlib.Path(__file__).parent.resolve()
    templates_dir = str((current_dir / "templates"))
    static_dir = str((current_dir / "static"))
    templates.HTMX_TEMPLATER = HtmxTemplater(templates_dir)
    app.mount("/static", StaticFiles(directory=static_dir), name="static")


def create_app() -> FastAPI:
    load_dotenv()
    configure_db()

    app = FastAPI()
    configure_static(app)

    app.include_router(endpoints.router)
    return app
