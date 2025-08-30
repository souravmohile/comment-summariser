# import asyncio

# async def say_hello():
#     print("Hello...")
#     await asyncio.sleep(2)   # pretend this is waiting for something
#     print("...World!")

# async def main():
#     await say_hello()

# asyncio.run(main())
import requests

url = "https://id.twitch.tv/oauth2/token"

data = {
    "client_id": "egvmsh0memvcbkjvx3r92km2e98si3",
    "client_secret": "e1uvdvcaiekjlgbm0pzw76kz3ajjju",
    "code": "ma2ej6zmr0kg3ndvfanfxqy5rbmv4e",
    "grant_type": "authorization_code",
    "redirect_uri": "http://localhost"
}

response = requests.post(url, data=data)
print(response.json())

