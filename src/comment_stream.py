import os
import websockets
import asyncio
import sys
import requests
import config

# Set the event loop policy for Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def get_access_token():
    url = "https://id.twitch.tv/oauth2/token"

    refresh_data = {
        'grant_type': 'refresh_token',
        'refresh_token': config.TWITCH_REFRESH_TOKEN,
        'client_id': config.TWITCH_CLIENT_ID,
        'client_secret': config.TWITCH_CLIENT_SECRET
    }

    # Send the POST request
    response = requests.post(url, data=refresh_data)

    return response.json()["access_token"]

async def listen_to_chat():

    config.uri = "wss://irc-ws.chat.twitch.tv:443"
    async with websockets.connect(config.uri) as websocket:

        # Authentication
        await websocket.send(f"PASS oauth:{get_access_token()}")
        await websocket.send(f"NICK {config.USERNAME}")
        
        # Join channel
        await websocket.send(f"JOIN {config.CHANNEL}")
        
        # Get messages
        while True:

            try:
                message = await websocket.recv()
                # print(message)
                if message.startswith("PING"):
                    await websocket.send("PONG :tmi.twitch.tv")

                if "PRIVMSG" in message:
                    
                    # Get only the message content
                    chat_content = message.split("PRIVMSG", 1)[1].split(":", 1)[1].strip()

                    # Increment counter for each new chat message
                    config.counter += 1
                    print(config.counter)

                    # Add each new message to the buffer
                    config.buffer.append(chat_content)

                    # Create batches of x messages
                    if config.counter == config.max_count:

                        # Setting a version for each new batch of messages
                        config.chat_version += 1
                        with open(f"data/chat_version{config.chat_version}.txt", "w", encoding="utf8") as chat_file:
                            for i in config.buffer:
                                chat_file.write(i + "\n")

                        # Reset message counter
                        config.counter = 0

                        # Clear the buffer for each new batch
                        config.buffer.clear()

            except websockets.ConnectionClosedOK:
                print("Connection closed cleanly.")
            except asyncio.CancelledError:
                print("Task was cancelled, shutting down.")
            finally:
                print("Cleanup done.")    