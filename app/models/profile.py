from sqlalchemy import Column,Integer,String,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class Profile(Base):
    __tablename__="profiles"
    
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    email = Column(String)
    photo = Column(String)
    bio = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"))
    
    user = relationship("User",back_populates="profile")