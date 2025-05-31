from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import UserShow,UserCreate,UserLogin,AccessToken,RefreshToken
from repositories.users import UserRepository
from core.security import verify_password,create_access_token,create_refresh_token,create_refresh_token,decode_refresh_token
router = APIRouter()

respo = UserRepository()

@router.post('/register',response_model=UserShow)
def register(user:UserCreate,db:Session=Depends(get_db)):
    db_user = respo.get_single_user(db,user.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Email already exist")
    return respo.create(db,user)


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
    