from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    username = Column(String,nullable=False)
    email = Column(String,unique=True,index=True,nullable=False)
    password = Column(String,nullable=False)
    role = Column(String,default="user")
    
    profile = relationship("Profile",back_populates="user",uselist=False)