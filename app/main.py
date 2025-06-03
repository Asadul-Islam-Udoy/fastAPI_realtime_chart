from models import *
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.database import Base,engine
from helpers.checkconnection import CheckConnection
from fastapi.middleware.cors import CORSMiddleware
from routers.users import user_router
from routers.messages import message_router
Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=CheckConnection)

orginns=[
  "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orginns,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/public",StaticFiles(directory="public"),name="public")

app.include_router(user_router,prefix="/api/v1/users",tags=["Users"])
app.include_router(message_router,prefix="/api/v1/messages",tags=["SingleMessages"])