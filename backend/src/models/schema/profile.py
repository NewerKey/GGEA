import datetime
import uuid

import pydantic

from src.models.schema.base import BaseSchemaModel

# ? Question:   How is the photo being handled?
# ?             How do we validate it?
# ?             How is it being send to the client?


class ProfileInUpdate(BaseSchemaModel):
    first_name: str | None
    last_name: str | None
    photo: str | None


class ProfileInResponse(BaseSchemaModel):
    id: uuid.UUID
    first_name: str | None
    last_name: str | None
    photo: str | None
    win: int
    loss: int
    mmr: int
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
