from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    address: str | None = None
    activated: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[UserBaseSchema]
