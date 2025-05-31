import asyncio
from fastapi import FastAPI
from sqlalchemy import text
from db.database import engine
from contextlib import asynccontextmanager
from starlette.concurrency import run_in_threadpool



@asynccontextmanager
async def CheckConnection(app:FastAPI):
        def check_db():
            with engine.connect() as conn:
              conn.execute(text("SELECT 1"))  
        try:
           await run_in_threadpool(check_db)
           print("Database connection successfully!")
        except Exception as e:
           print("❌ Database connection fails!")
           
           
        try:
          print("App lifespan started.")
          yield
        except asyncio.CancelledError:
          print("CancelledError caught during shutdown.")
        finally:
          print("App lifespan ended.")
        