from abc import ABC, abstractmethod
from typing import Generic, TypeVar

ResponseType = TypeVar("ResponseType")


class IHtmxTemplater(ABC, Generic[ResponseType]):
    @abstractmethod
    def build_response(
        self, name: str, context: dict = {}, headers: dict = {}
    ) -> ResponseType:
        """"""


HTMX_TEMPLATER: IHtmxTemplater
