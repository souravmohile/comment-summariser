# Comment summariser

Streamers on Twitch recieve hundreds of comments per minute, making it impossible for them to read them all and understand what their chat is saying efficiently. 

This project aims at solving that problem by generating summaaries and sentiment scores for live chats periodically so the streamer and the audience can quickly catch up on what the chat is saying.

## Scope:
The scope of this project is strictly for Twitch Live videos, we will not be dealing with on demand (VOD) or clips.

## Flow:
1. Fetching live chat data from Twitch IRC through a websocket connection. These chats are asynchronously read and batched into sets of 'x' number of comments. This will in the future be batched according to time and be saved in a Kafka DB. For now it uses a hacky solution where im dumping the chats into txt files. 
2. These text files are then stored in a data folder which is monitored by another script using a filewatcher. For every new file added we are sending the contents along with a prompt to an LLM on Groq Cloud. This will be replacd by two small language models which will be finetuned for summaristion and sentiment scoring specifically for twitch data.
3. Finally the results (Outputted in a JSON format) are then visualised in the frontend along with the twitch video and live chat.

## How to run:
1. Install requirements.txt
2. Run processor.py
3. Run comment_stream.py

## PS:
The frontend was not my focus or forte so around 80% of it is vibe coded with ChatGPT and Gemini Canvas.