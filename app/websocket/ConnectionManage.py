from fastapi import WebSocket
from typing import Dict

class ConnectionManager:
    def __init__(self):
        self.active_connection:Dict[int,WebSocket]={}
        
    async def connect(self,user_id:int,websocket:WebSocket):
        await websocket.accept()
        self.active_connection[user_id] = websocket
        
    def disconnect(self,user_id:int):
        self.active_connection.pop(user_id,None)
        
    async def send_personal_message(self,message:str,user_id:int):
        if user_id in self.active_connection:
            await self.active_connection[user_id].send_text(message)
manager = ConnectionManager()