from pydantic import BaseModel
from datetime import datetime
class CreateMessage(BaseModel):
    sender_id : int
    reciver_id :int
    content : str
    
class SingleMessageShow(BaseModel):
    sender_id : int
    reciver_id :int
    content : str
    created_at:datetime
    
    class Config:
        orm_model = True