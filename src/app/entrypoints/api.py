import os

from dotenv import load_dotenv
from fastapi import FastAPI

from src.app.adapters.db.gateway_facade import DbGatewayFacade
from src.app.adapters.db.sqlachemy import Db
from src.app.adapters.http import endpoints
from src.app.interfaces import db

def configure_db():
    url = os.getenv("DATABASE_URL", "")
    db_instance = Db(url=url.replace("postgresql:", "postgresql+asyncpg:"))
    db.DB = db
    db.DB_GATEWAY = DbGatewayFacade(session_factory=db_instance.get_session_factory())


def create_app() -> FastAPI:
    load_dotenv()
    configure_db()
    
    app = FastAPI()
    app.include_router(endpoints.router)
    return app
