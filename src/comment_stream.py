import os
import websockets
import asyncio
import sys
import config

# Set the event loop policy for Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def listen_to_chat():

    config.uri = "wss://irc-ws.chat.twitch.tv:443"
    async with websockets.connect(config.uri) as websocket:

        # Authentication
        await websocket.send(f"PASS oauth:{config.ACCESS_TOKEN}")
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
                        config.version += 1
                        with open(f"data/chat_version{config.version}.txt", "w", encoding="utf8") as chat_file:
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

if __name__ == "__main__":
    try:
        asyncio.run(listen_to_chat())
    except KeyboardInterrupt:
        print("Program interrupted by user, shutting down...")
