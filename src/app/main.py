from fastapi import FastAPI

from src.app.entrypoints.api import create_app

app: FastAPI = create_app()
