from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
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
