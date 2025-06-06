from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class PostBase(BaseModel):
    text: str
    user_id: int

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    date_of_creation: datetime

    class Config:
        from_attributes = True