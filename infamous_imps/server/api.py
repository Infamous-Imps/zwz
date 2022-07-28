import uuid

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


class ConnectionManager:
    """Manages connection related functions"""

    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Internal method to connect to websocket"""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Internal method to disconnect to websocket"""
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """Internal method to sent message to websocket"""
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        """Internal method to broadcast to websocket"""
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


def process_data(data: dict) -> bool:
    """Process data received"""
    print("Method:", data["method"])
    print("Device UID:", data["device_uid"])
    return True


def get_client_id():
    """Get random client id"""
    return str(uuid.uuid4())


@app.websocket("/ws")
async def connection(websocket: WebSocket):
    """Connection handler for /ws"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            result = process_data(data)
            if result:
                await websocket.send_json({"client_id": get_client_id()})
    except WebSocketDisconnect:
        manager.disconnect(websocket)


@app.websocket("/ws/{client_id}")
async def client_connect(websocket: WebSocket, client_id: int):
    """Connection handler for /ws/{client_id}"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
