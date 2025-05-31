from pydantic_settings import BaseSettings
class Setting(BaseSettings):
    DATABASE_URL:str
    ACCESS_JWT_SECRET_KEY:str
    REFRESH_JWT_SECRET_KEY:str
    JWT_ALGORITH:str="HS256"
    ACCESS_TOKEN_EXPIRE_TIME:int
    REFRESH_TOKEN_EXPIRE_TIME:int
    class Config:
        env_file = ".env"
        
settings=Setting()