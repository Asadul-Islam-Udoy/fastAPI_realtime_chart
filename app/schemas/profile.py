from pydantic import BaseModel,EmailStr
from typing import Optional

class ProfileCreate(BaseModel):
    user_id:int
    email:EmailStr
    bio:Optional[str] = None
    photo:Optional[str] = None

class ProfileShow(BaseModel):
    user_id:int
    email:EmailStr
    bio:Optional[str] = None
    photo:Optional[str] = None
    
    class Config:
        orm_model = True