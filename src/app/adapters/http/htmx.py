from fastapi.templating import Jinja2Templates
from starlette.responses import Response

from src.app.interfaces.templates import IHtmxTemplater


class HtmxTemplater(IHtmxTemplater, Response):
    def __init__(self, directory: str) -> None:
        self.templates = Jinja2Templates(directory=directory)

    def build_response(
        self, name: str, context: dict = {}, headers: dict = {}
    ) -> Response:
        return self.templates.TemplateResponse(name, context, headers=headers)
