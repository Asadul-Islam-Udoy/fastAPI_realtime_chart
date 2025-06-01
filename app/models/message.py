from db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String,Integer,Column,ForeignKey,DateTime,func

class SingleMessages(Base):
    __tablename__ = "single_messages"
    
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    sender_id = Column(Integer,ForeignKey("profiles.id"))
    reciver_id = Column(Integer,ForeignKey("profiles.id"))
    content = Column(String)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),onupdate=func.now())
    
    sender = relationship("Profile",foreign_keys=[sender_id],back_populates="send_messages")
    reciver = relationship("Profile",foreign_keys=[reciver_id],back_populates="reciver_messages")