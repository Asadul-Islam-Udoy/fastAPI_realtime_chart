from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta
from core.config import settings

pwd_contex = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password:str)->str:
    return pwd_contex.hash(password)

def verify_password(new_password:str,old_password:str)->bool:
    return pwd_contex.verify(new_password,old_password)

def create_access_token(data:dict)->str:
    to_encode = data.copy()
    exprie = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp":exprie})
    return jwt.encode(to_encode,settings.ACCESS_JWT_SECRET_KEY,settings.JWT_ALGORITH)

def create_refresh_token(data:dict)->str:
    to_encode = data.copy()
    exprie = datetime.utcnow()+timedelta(hours=settings.REFRESH_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp":exprie})
    return jwt.encode(to_encode,settings.REFRESH_JWT_SECRET_KEY,settings.JWT_ALGORITH)

def decode_refresh_token(token:str):
    try:
        payload = jwt.decode(token,settings.REFRESH_JWT_SECRET_KEY,settings.JWT_ALGORITH)
        return payload
    except JWTError:
        return None