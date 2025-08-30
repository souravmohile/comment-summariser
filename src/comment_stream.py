import os
import requests
from dotenv import load_dotenv
import websockets
import asyncio

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("TWITCH_ACCESS_TOKEN")
USERNAME = "sourav_mohile"
CHANNEL = "#IShowSpeed"

async def listen_to_chat():
    uri = "wss://irc-ws.chat.twitch.tv:443"
    async with websockets.connect(uri) as websocket:
        # Authentication
        await websocket.send(f"PASS oauth:{ACCESS_TOKEN}")
        await websocket.send(f"NICK {USERNAME}")
        
        # Join channel
        await websocket.send("JOIN {CHANNEL}")
        
        while True:
            message = await websocket.recv()
            print(message)

asyncio.run(listen_to_chat())
    