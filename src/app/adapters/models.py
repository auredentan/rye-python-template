from typing import Literal

from pydantic import UUID4, BaseModel, Field


class User(BaseModel):
    id: UUID4
    email: str
    is_admin: bool = Field(
        default=True,
        serialization_alias="isAdmin",
    )


class EventTruc(BaseModel):
    type: Literal["truc"]
    name: str


class EventMachin(BaseModel):
    type: Literal["Machin"]
    name: str
    test: bool | None = True
