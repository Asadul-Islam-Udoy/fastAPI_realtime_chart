from pydantic import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    role:str
    password:str

class ProfileShowModel(BaseModel):
    user_id:int
    email:EmailStr
    bio:Optional[str] = None
    photo:Optional[str] = None
    
class UserShow(BaseModel):
    id:int
    username:str
    email:EmailStr
    role:str
    profile:Optional[ProfileShowModel]=None
   
    class Config:
        orm_model = True

class UserLogin(BaseModel):
   email:EmailStr
   password:str 
   
class AccessToken(BaseModel):
    access_token:str
    refresh_token:str
    token_type:str="bearer"
    
class RefreshToken(BaseModel):
    refresh_token:str
        
