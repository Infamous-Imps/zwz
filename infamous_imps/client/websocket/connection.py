# import asyncio
import json
import uuid
from pathlib import Path

import websockets


def encode_msg(msg: dict) -> str:
    """Encode function"""
    return json.dumps(msg, ensure_ascii=False)


def decode_msg(text: str) -> dict:
    """Decode function"""
    return json.loads(text)


def get_uid(new: bool = False) -> str:
    """Generate uid"""

    def read_uid() -> str:
        """Read json from file"""
        with file.open(encoding="UTF-8") as source:
            data = json.load(source)
        return data["uid"]

    def write_uid(uid) -> None:
        """Write json to file"""
        with file.open("w", encoding="UTF-8") as target:
            json.dump({"uid": uid}, target)

    file = Path("config.json")
    if file.exists():
        if not new:
            return read_uid()
    uid = str(uuid.uuid1())
    write_uid(uid)
    return uid


async def connect():
    """Connect to server"""
    uri = "ws://localhost:8000/ws"
    data = {"method": "connect", "device_uid": get_uid()}
    async with websockets.connect(uri) as ws:
        await ws.send(encode_msg(data))
        res = decode_msg(await ws.recv())
        print("Client ID:", res["client_id"])
