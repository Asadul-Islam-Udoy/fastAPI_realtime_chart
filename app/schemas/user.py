from pydantic import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    role:Optional[str] = "user"
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
    role:Optional[str] = "user"
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
    
class LoginResponse(BaseModel):
    id:int
    username: str
    email: str
    role: str
    token: AccessToken
   
class RefreshToken(BaseModel):
    refresh_token:str
        
