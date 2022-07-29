import time

from dba import add_message, add_user, delete_user, update_user_name
from fastapi import FastAPI

app = FastAPI()


@app.post("/chat/{server}")
async def chat(server: str, user: str, message: str):
    """Post new message to server"""
    timestamp = time.time()
    add_message(server, timestamp, user, message)
    print(server, user, message)


@app.post("/api/cv1/player/delete/{name}&hash={hashed}")
async def del_user(name: str, hashed: str):
    """Delete user from the server"""
    delete_user(name, hashed)


@app.post("/api/v1/player/create/{name}?password={hashed}")
async def new_user(name: str, hashed: str):
    """Adds user to the server"""
    add_user(name, hashed)


@app.post("/api/cv1/player/update/{name}?name={new_name}?password={hashed}")
async def update_user(name, new_name, hashed):
    """Update user credentials"""
    update_user_name(name, hashed, new_name)
