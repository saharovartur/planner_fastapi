from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event
from beanie import Document, Link


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = 'users'

    class Config:
        json_schema_extra = {
            "example": {
                "email": 'geekant@gmail.com',
                "password": "strong",
                "events": [],

            }
        }


class UserSingIn(BaseModel):
    email: EmailStr
    password: str
