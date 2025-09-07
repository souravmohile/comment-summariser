import asyncio
from comment_stream import listen_to_chat
from processor import watch_file

async def main():
    print("Starting processor ...")
    
    # Start watch_file immediately
    watcher_task = asyncio.create_task(watch_file())
    
    # Optional: small delay to ensure it's fully started
    await asyncio.sleep(1)

    print("Starting comment stream...")
    chat_task = asyncio.create_task(listen_to_chat())

    # Wait for both tasks
    await asyncio.gather(watcher_task, chat_task)

asyncio.run(main())
