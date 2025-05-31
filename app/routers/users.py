import os
import shutil
from fastapi import APIRouter,Depends,HTTPException,status,UploadFile,File
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import UserShow,UserCreate,UserLogin,AccessToken,RefreshToken
from schemas.profile import ProfileShow
from repositories.users import UserRepository
from core.security import verify_password,create_access_token,create_refresh_token,create_refresh_token,decode_refresh_token

router = APIRouter()

respo = UserRepository()

UPLOAD_URL="public/users_images"

# register user router
@router.post('/register',response_model=UserShow)
def register(user:UserCreate,db:Session=Depends(get_db)):
    db_user = respo.get_single_user(db,user.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Email already exist")
    return respo.create(db,user)

# login user router
@router.post('/login',response_model=AccessToken)
def login(user:UserLogin,db:Session=Depends(get_db)):
    user_db = respo.get_single_user(db,user.email)
    if not user_db or not verify_password(user.password,user_db.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    data = {"sub":user_db.email}
    return{
        "access_token":create_access_token(data),
        "refresh_token":create_refresh_token(data),
        "token_type":"bearer"
    }
    
    
# refresh token router  
@router.post("/refresh",response_model=AccessToken)
def refresh(token_data:RefreshToken):
    try:
       payload = decode_refresh_token(token_data.refresh_token)
       email = payload.get("sub")
       if not email:
           raise HTTPException(status_code=401,detail="Invalid token")
       data = {"sub":email}
       return{
        "access_token":create_access_token(data),
        "refresh_token":create_refresh_token(data),
        "token_type":"bearer"
        }
    except Exception:
        raise HTTPException(status_code=401,detail="Invalid refresh token")
    
# update profile  router  
@router.put("/update/profile/{user_id}",response_model=ProfileShow)
def update_profile(user_id:int,bio:str=File(None),file:UploadFile=File(None),db:Session=Depends(get_db)):
    profile  = respo.get_single_user_by_userid(db,user_id)
    if not profile:
        raise HTTPException(status_code=401,detail="User is not found")
    if bio is not None:
        profile.bio = bio
    if file:
        filename = f"user_{user_id}_{file.filename}"
        file_path = os.path.join(UPLOAD_URL,filename)
        
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
            
        profile.photo = f"/users_images/{filename}"
    db.commit()
    db.refresh(profile)
    return profile