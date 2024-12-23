from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class Users(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

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

    class Config:
        json_schema_extra = {
            "example": {
                "email": 'geekant@gmail.com',
                "password": "strong",

            }
        }

