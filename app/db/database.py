from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()