from beanie import Document
from typing import List, Optional
from pydantic import BaseModel


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": 'Learn fastAPI',
                "image": "https://linktomyimage.com/image.png",
                "description": "We will discuss fastapi",
                "tags": ["python", "fastapi", "web", "backend"],
                "location": "Zoom"

            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": 'Learn fastAPI',
                "image": "https://linktomyimage.com/image.png",
                "description": "We will discuss fastapi",
                "tags": ["python", "fastapi", "web", "backend"],
                "location": "Zoom"

            }
        }
