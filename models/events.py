# from pydantic import BaseModel
# from typing import List, Optional


# class Event(BaseModel):
#     id: int
#     title: str
#     image: str
#     description: str
#     tags: List[str]
#     location: str

#     class Config:
#         schema_extra = {
#             "example": {
#                 "id": 1,
#                 "title": "Event 1",
#                 "image": "+9*6---------------------------------3https://linktomyimage.com/image.png",
#                 "description": "This is a description",
#                 "tags": ["python", "fastapi", "book", "launch"],
#                 "location": "Google Meet"
#             }
#         }

# from sqlmodel import JSON, SQLModel, Field, Column
# from typing import List, Optional

# class Event(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     title: str
#     image: str
#     description: str
#     tags: List[str] = Field(sa_column=Column(JSON))
#     location: str

#     class Config:
#         arbitrary_types_allowed = True
#         schema_extra = {
#             "example": {
#                 "title" : "이게 제목",
#                 "image" : "https://linktomyimage.com/image.png",
#                 "description" : "이게 설명",
#                 "tags" : ["python", "fastapi", "book", "launch"],
#                 "location":"Google Meet"
#             }
#         }


# class EventUpdate(SQLModel):
#     title: Optional[str] = None
#     image: Optional[str] = None
#     description: Optional[str] = None
#     tags: Optional[List[str]] = None
#     location: Optional[str] = None

#     class Config:
#         schema_extra = {
#             "example": {
#                 "title" : "이게 제목",
#                 "image" : "https://linktomyimage.com/image.png",
#                 "description" : "이게 설명",
#                 "tags" : ["python", "fastapi", "book", "launch"],
#                 "location":"Google Meet"
#             }
#         }


from pydantic import BaseModel
from beanie import Document
from typing import List, Optional

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    creator: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title" : "이게 제목",
                "image" : "https://linktomyimage.com/image.png",
                "description" : "이게 설명",
                "tags" : ["python", "fastapi", "book", "launch"],
                "location":"Google Meet"
            }
        }
    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "title" : "이게 제목",
                "image" : "https://linktomyimage.com/image.png",
                "description" : "이게 설명",
                "tags" : ["python", "fastapi", "book", "launch"],
                "location":"Google Meet"
            }
        }