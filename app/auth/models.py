from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    username: str = Field(max_length=150)
    email: str = Field(max_length=255)
    password: str = Field(min_length=5, max_length=32)


