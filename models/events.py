from typing import List, Optional

from sqlmodel import JSON, SQLModel, Field, Column


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": 'Learn fastAPI',
                "image": "https://linktomyimage.com/image.png",
                "description": "We will discuss fastapi",
                "tags": ["python", "fastapi", "web", "backend"],
                "location": "Zoom"

            }
        }


class EventUpdate(SQLModel):
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
