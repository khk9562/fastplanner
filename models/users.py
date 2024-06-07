# from pydantic import BaseModel, EmailStr
# from typing import Optional, List
# from models.events import Event

# class User(BaseModel):
#     email: EmailStr
#     password: str
#     events: Optional[List[Event]] = []

#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "fastapi@packt.com",
#                 "password": "password!!!",
#                 "events": [],
#             }
#         }

# class UserSignIn(BaseModel):
#     email: EmailStr
#     password: str

#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "fastapi@packt.com",
#                 "password": "password!!!",
#             }
#         }

from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "password!!!",
                "events": [],
            }
        }

# class UserSignIn(BaseModel):
#     email: EmailStr
#     password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str



