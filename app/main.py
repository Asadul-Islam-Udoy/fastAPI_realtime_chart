from models import *
from fastapi import FastAPI
from db.database import Base,engine
from helpers.checkconnection import CheckConnection
from routers.users import router

Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=CheckConnection)

app.include_router(router,prefix="/api/v1/users",tags=["Users"])