# import asyncio

# async def say_hello():
#     print("Hello...")
#     await asyncio.sleep(2)   # pretend this is waiting for something
#     print("...World!")

# async def main():
#     await say_hello()

# asyncio.run(main())
import requests
from src import config

url = "https://id.twitch.tv/oauth2/token"

# data = {
#     "client_id": "egvmsh0memvcbkjvx3r92km2e98si3",
#     "client_secret": "e1uvdvcaiekjlgbm0pzw76kz3ajjju",
#     "code": "imvwdtcxnaipbv4dyybwk4ndkmoi80",
#     "grant_type": "authorization_code",
#     "redirect_uri": "http://localhost"
# }

# response = requests.post(url, data=data)
# print(response.json())

def get_access_token():
    url = "https://id.twitch.tv/oauth2/token"

    refresh_data = {
        'grant_type': 'refresh_token',
        'refresh_token': config.REFRESH_TOKEN,
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET
    }

    # Send the POST request
    response = requests.post(url, data=refresh_data)

    return response.json()["access_token"]