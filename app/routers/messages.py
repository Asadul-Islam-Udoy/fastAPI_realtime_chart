from fastapi import APIRouter,WebSocket,Depends
from models.message import SingleMessages
from sqlalchemy.orm import Session
from db.database import get_db
from websocket.ConnectionManage import ConnectionManager
import json

message_router = APIRouter()

@message_router.websocket("/ws/chat/{sender_id}/{reciver_id}")
async def chat(websocket:WebSocket,sender_id:int,reciver_id:int,db:Session=Depends(get_db)):
    await ConnectionManager.connect(sender_id,websocket)
    try:
        while True:
            data = await websocket.receive_text()
            msg_data = json.loads(data)
            
            message = SingleMessages(
                sender_id = sender_id,
                reciver_id = reciver_id,
                context = msg_data["context"]
            )
            db.add(message)
            db.commit()
            await ConnectionManager.send_personal_message(
                json.dumps({
                    "sender_id":sender_id,
                    "reciver_id":reciver_id,
                    "content":msg_data["content"],
                    "timestamp":str(message.created_at)
                }),reciver_id
            )
    except:
        ConnectionManager.disconnect(sender_id)
    