from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("TWITCH_ACCESS_TOKEN")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

USERNAME = "sourav_mohile"
CHANNEL = "#jasontheween"

uri = "wss://irc-ws.chat.twitch.tv:443"


buffer = []

counter = 0
version = 0

max_count = 50

