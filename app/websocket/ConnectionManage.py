from typing import Dict, List
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        # Key: user_id, Value: list of WebSocket connections
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)
        print(f"User {user_id} connected. Total connections: {len(self.active_connections[user_id])}")

    def disconnect(self, user_id: int, websocket: WebSocket = None):
        if user_id in self.active_connections:
            if websocket:
                if websocket in self.active_connections[user_id]:
                    self.active_connections[user_id].remove(websocket)
            else:
                # remove all if specific websocket not given
                self.active_connections[user_id].clear()

            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

            print(f"User {user_id} disconnected. Remaining connections: {len(self.active_connections.get(user_id, []))}")

    async def send_personal_message(self, message: str, user_id: int):
        if user_id in self.active_connections:
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_text(message)
                except Exception as e:
                    print(f"Failed to send message to user {user_id}: {e}")
manager = ConnectionManager();