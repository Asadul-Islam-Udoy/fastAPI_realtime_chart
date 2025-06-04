from fastapi import APIRouter,WebSocket,Depends,WebSocketDisconnect
from models.message import SingleMessages
from sqlalchemy.orm import Session
from db.database import get_db
from websocket.ConnectionManage import manager
import json

message_router = APIRouter()

@message_router.websocket("/ws/chat/{sender_id}/{reciver_id}")
async def chat(websocket:WebSocket,sender_id:int,reciver_id:int,db:Session=Depends(get_db)):
    await manager.connect(sender_id,websocket)
    try:
        while True:
            data = await websocket.receive_text()
            msg_data = json.loads(data)
            message = SingleMessages(
                sender_id = sender_id,
                reciver_id = reciver_id,
                content = msg_data["content"]
            )
            db.add(message)
            db.commit()
            payload = json.dumps({
                "sender_id": sender_id,
                "reciver_id": reciver_id,
                "content": msg_data["content"],
                "timestamp": str(message.created_at)
            })

            # Send to both sender and receiver
            await manager.send_personal_message(payload, reciver_id)
            await manager.send_personal_message(payload, sender_id)

    except WebSocketDisconnect:
        print(f"User {sender_id} disconnected")
        manager.disconnect(sender_id)
    except Exception as e:
        print(f"WebSocket error for user {sender_id}:", e)
        manager.disconnect(sender_id)
        
        
        
@message_router.get("/chat/history/{user_id}/{friend_id}")
def get_chat_history(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    messages = db.query(SingleMessages).filter(
        ((SingleMessages.sender_id == user_id) & (SingleMessages.reciver_id == friend_id)) |
        ((SingleMessages.sender_id == friend_id) & (SingleMessages.reciver_id == user_id))
    ).order_by(SingleMessages.created_at.asc()).all()
    
    return [
        {
            "id": msg.id,
            "sender_id": msg.sender_id,
            "reciver_id": msg.reciver_id,
            "content": msg.content,
            "timestamp": msg.created_at.isoformat()
        } for msg in messages
    ]
