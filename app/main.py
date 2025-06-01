from models import *
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.database import Base,engine
from helpers.checkconnection import CheckConnection
from routers.users import router
from routers.messages import router
Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=CheckConnection)

app.mount("/public",StaticFiles(directory="public"),name="public")

app.include_router(router,prefix="/api/v1/users",tags=["Users"])
app.include_router(router,prefix="/api/v1/message",tags=["SingleMessages"])