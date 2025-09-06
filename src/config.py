from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("TWITCH_ACCESS_TOKEN")
REFRESH_TOKEN = os.getenv("TWITCH_REFRESH_TOKEN")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

USERNAME = "sourav_mohile"
CHANNEL = "#KaiCenat"

uri = "wss://irc-ws.chat.twitch.tv:443"


buffer = []

counter = 0

chat_version = 0
prompt_version = 1

max_count = 70

